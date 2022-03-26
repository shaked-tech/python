import requests
import json
import sys
import re
import os
import datetime

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def verify_response(response):
    if response.status_code == 401:
        print(f'Unauthorized response, got: {response.status_code}')
        print(f'verify \'user-id\' is correct and token has the needed permissions')
        exit(1)
    if ((response.status_code != 201) and (response.status_code != 200)):
        print(type(response.status_code))
        print(f'errored response, got: {response.status_code}')
        exit(2)
    else:
        pass

def songs_to_spotify(html_file):
    r = re.compile("[|]|(|)|feat.|/|\\\\")
    # CURRENTDATE = datetime.datetime.now().strftime("%m-%Y")
    HTML_FILE_FULL_PATH = html_file
    HTML_FILE_PATH = os.path.dirname(HTML_FILE_FULL_PATH)
    HTML_FILE_NAME = os.path.basename(HTML_FILE_FULL_PATH)

    PLAYLIST_NAME = re.sub('.html', '', HTML_FILE_NAME)
    PLAYLIST_NAME = re.sub(r'-|_', ' ', PLAYLIST_NAME).title()

    endpoint_url = "https://api.spotify.com/v1/search"
    # token from: https://developer.spotify.com/console/get-recommendations/
    token = "BQAj0hW2ifb0Sd_BsWD1CL6gP5OkJDzRN5dyYldYvzTL4v3BRB8iQOFVMrzbLQYPzt7P3oiiTONyiqQ4Dr1Y5y8kERf8CLghc3P5P9iDf5mmUwxTx5AIMVYJvlC7RYyjFI9QZLXiG8IC6zvVv2JL4A_ocp2sGM8ZyDAaXxfFLiSRvt6c4ytm1w8WLQiUHLznv1N6gVyyuKfVHwDsg3EBZrCFQGKyfWn58v2BOxumBjw"
    user_id = "zh5eiddy1j60thppxw5z29ubs"
    uris = [] 

    # OUR FILTERS
    limit=1
    # market="US"
    # seed_genres="indie"
    # target_danceability=0.9
    # seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
    # seed_tracks='55SfSsxneljXOk5S3NVZIW'

    with open(HTML_FILE_FULL_PATH) as f:
        html = f.read()

    parsed_html = BeautifulSoup(html, features="html.parser")

    ## create a parsed html page: ##
    # with open(f'{HTML_FILE_NAME_PATH}/parsed-{HTML_FILE_NAME}', 'w') as f:
        # f.write(parsed_html.prettify())

    items_list = (parsed_html.find_all('div', attrs={'class':'songs-list-row__song-name'})) #.find_all('span')
    songs_list = [r.sub('', item.text) for item in items_list]
    print(f'{len(songs_list)} songs in {PLAYLIST_NAME}')
    exit(0)
    # LIST SEARCHED SONGS
    print("Searching songs:")
    not_found_list = []
    for song in songs_list: 
        # preform query
        query = f'{endpoint_url}?q={song}&limit={limit}&type=track'

        # get matched songs
        response = requests.get(query, 
                    headers={"Content-Type":"application/json", 
                                "Authorization":f"Bearer {token}"})

        verify_response(response)
        json_response = response.json()
        try:
            for i,j in enumerate(json_response['tracks']['items']):
                uris.append(j['uri'])
                # print('Recommended Song: ', end='')
                print(f"\"{j['name']}\" by {j['artists'][0]['name']}")
        except:
            not_found_list += [song]
    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"


    # CREATE PLAYLIST
    print(f"Creating playlist {PLAYLIST_NAME}:")
    request_body = json.dumps({
            "name": f"{PLAYLIST_NAME}",
            "description": f"Python uploaded {PLAYLIST_NAME}",
            "public": False
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {token}"})
    verify_response(response)

    playlist_id = response.json()['id']
    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    # UPLOAD SONGS TO PLAYLIST
    request_body = json.dumps({"uris" : uris})
    response = requests.post(url = endpoint_url, data = request_body, 
                             headers={"Content-Type":"application/json",
                                      "Authorization":f"Bearer {token}"})
    verify_response(response)

    print(f'Done, Checkout your new playlist: {PLAYLIST_NAME}')
    print(f'could not find {len(not_found_list)} songs: {not_found_list}')

if __name__ == '__main__':
    html_file = sys.argv[1]
    songs_to_spotify(html_file)