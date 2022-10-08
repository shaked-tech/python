import requests
import json
from jsonpath_ng import jsonpath, parse
import sys
import re
import os
import datetime

# youtube - user authorized
# import google_auth_oauthlib.flow
# import googleapiclient.discovery
# import googleapiclient.errors

# credentials file
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def verify_response(response):
    if response.status_code == 401:
        print(f'Unauthorized response, got: {response.status_code}')
        print(f'verify \'user-id\' is correct and \'spotify_token\' has the needed permissions')
        exit(1)
    if ((response.status_code != 201) and (response.status_code != 200)):
        print(type(response.status_code))
        print(f'errored response, got: {response.status_code}')
        exit(2)
    else:
        pass

def from_youtube(client_secrets_file):
    # Using credentials file:
    # If modifying these scopes, delete the file token.json.
    SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
    api_service_name = "youtube"
    api_version = "v3"
    credentials = None
    
    if os.path.exists('token.json'):
        credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    youtube = build(
        api_service_name, api_version, credentials=credentials
    )

    request = youtube.playlists().list(
        part="snippet,contentDetails",
        maxResults=25,
        mine=True
    )

    response = request.execute()
    response_json = json.loads(json.dumps(response))
    jsonpath_expression = parse('items[*].snippet.title')
    titles_list = [match.value for match in jsonpath_expression.find(response_json)]
    print(titles_list)

    # TODO: 
    # 1. Get list from each playlist
    # 2. Update to_spotify function to use info (from 1) instead of html

def to_spotify(html_file):
    r = re.compile("[|]|(|)|feat.|/|\\\\")
    # CURRENTDATE = datetime.datetime.now().strftime("%m-%Y")
    HTML_FILE_FULL_PATH = html_file
    HTML_FILE_PATH = os.path.dirname(HTML_FILE_FULL_PATH)
    HTML_FILE_NAME = os.path.basename(HTML_FILE_FULL_PATH)

    PLAYLIST_NAME = re.sub('.html', '', HTML_FILE_NAME)
    PLAYLIST_NAME = re.sub(r'-|_', ' ', PLAYLIST_NAME).title()


    spotify_user_id = ""
    spotify_token = ""
    uris = []

    ## FILTERS
    limit=1
    # market="US"
    # seed_genres="indie"
    # target_danceability=0.9
    # seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
    # seed_tracks='55SfSsxneljXOk5S3NVZIW'

    with open(HTML_FILE_FULL_PATH) as f:
        html = f.read()

    parsed_html = BeautifulSoup(html, features="html.parser")

    ## Beautify html page:
    # with open(f'{HTML_FILE_NAME_PATH}/parsed-{HTML_FILE_NAME}', 'w') as f:
        # f.write(parsed_html.prettify())

    items_list = (parsed_html.find_all('div', attrs={'class':'songs-list-row__song-name'})) #.find_all('span')
    songs_list = [r.sub('', item.text) for item in items_list]
    print(f'{len(songs_list)} songs in {PLAYLIST_NAME}')

    # CREATE PLAYLIST
    endpoint_url = f"https://api.spotify.com/v1/users/{spotify_user_id}/playlists"
    print(f"Creating playlist {PLAYLIST_NAME}:")
    request_body = json.dumps({
            "name": f"{PLAYLIST_NAME}",
            "description": f"Python uploaded {PLAYLIST_NAME}",
            "public": False
            })
    response = requests.post(url = endpoint_url, 
                             data = request_body, 
                             headers={"Content-Type":"application/json", 
                                      "Authorization":f"Bearer {spotify_token}"})
    verify_response(response)
    playlist_id = response.json()['id']
    
    # LIST SEARCHED SONGS
    endpoint_url = "https://api.spotify.com/v1/search"
    print("Searching songs:")
    not_found_list = []
    for song in songs_list: 
        # preform query
        query = f'{endpoint_url}?q={song}&limit={limit}&type=track'

        # get matched songs
        response = requests.get(query, 
                    headers={"Content-Type":"application/json", 
                                "Authorization":f"Bearer {spotify_token}"})

        verify_response(response)
        json_response = response.json()
        try:
            for i,j in enumerate(json_response['tracks']['items']):
                uris.append(j['uri'])
                # print('Recommended Song: ', end='')
                print(f"\"{j['name']}\" by {j['artists'][0]['name']}")
        except:
            not_found_list += [song]

    # UPLOAD SONGS TO PLAYLIST
    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    # split requests into chunks
    n = 100
    uris = [uris[i:i + n] for i in range(0, len(uris), n)]
    for l in uris:
        request_body = json.dumps({"uris" : l})
        response = requests.post(url = endpoint_url, data = request_body, 
                                headers={"Content-Type":"application/json",
                                        "Authorization":f"Bearer {spotify_token}"})
        verify_response(response)

    print(f'Done, Checkout your new playlist: {PLAYLIST_NAME}')
    print(f'could not find {len(not_found_list)} songs: {not_found_list}')

if __name__ == '__main__':
    client_secrets_file = "youtube-access-shaked-personal.json"
    # html_file = sys.argv[1]
    from_youtube(client_secrets_file)
    # to_spotify(html_file)










# def from_youtube(client_secrets_file):
# youtube - user authorized
    # scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    # # Disable OAuthlib's HTTPS verification when running locally.
    # # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # api_service_name = "youtube"
    # api_version = "v3"

    # # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     client_secrets_file, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials
    # )

    # request = youtube.playlists().list(
    #     part="snippet,contentDetails",
    #     maxResults=25,
    #     mine=True
    # )

    # response = request.execute()
    
    # response_json = json.loads(response)
    # jsonpath_expression = parse('items[*].snippet.title')

    # titles_list = [match.value for match in jsonpath_expression.find(response_json)]
    # print(titles_list)
    # youtube.playlists()
