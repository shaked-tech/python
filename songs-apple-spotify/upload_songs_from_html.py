import requests
import json
import sys
import re
import datetime

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

def verify_response(response):
    if response.status_code == 401:
        print(f'Unauthorized response, got: {response}')
        print(f'verify \'user-id\' is correct and token has the needed permissions')
        exit(1)
    elif response.status_code != (200 or 201):
        print(f'errored responce, got: {response}')
        exit(2)
    else:
        pass

def songs_to_spotify(html_file):
    r = re.compile(r"[()\'feat.\']")
    # CURRENTDATE = datetime.datetime.now().strftime("%m-%Y")
    HTML_FILE = html_file
    PLAYLIST_NAME = re.sub(r'-|_', ' ', re.sub('.html', '', HTML_FILE)).title()
    endpoint_url = "https://api.spotify.com/v1/search"
    token = "BQCh34MxAEmaY_uBx7-2Cb4fGUUJgu8Cy4XAXl1AZZrXQomZdyAvYJ9AElULNU36MT325S1_dIFzZZTc85apkVR22s9oAbClWowE0GT47ddIIrR8u_Lxqfr62fV6e-Nn_c4dxeTBjY3vNCNxkB3xIZRI8tU1TnSJLNZlLrLwalk4JXKQpjTDzuA4VxX05VotFrCdbw5Te24MXY2ib2vwhUQ9Iiqa6HbGpbukbvyhzkw"
    user_id = "zh5eiddy1j60thppxw5z29ubs"
    uris = [] 

    # OUR FILTERS
    limit=1
    # market="US"
    # seed_genres="indie"
    # target_danceability=0.9
    # seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
    # seed_tracks='55SfSsxneljXOk5S3NVZIW'

    with open(HTML_FILE) as f:
        html = f.read()

    parsed_html = BeautifulSoup(html, features="html.parser")

    ## create a parsed html page: ##
    # with open(f'parsed-{HTML_FILE}', 'w') as f:
        # f.write(parsed_html.prettify())

    items_list = (parsed_html.find_all('div', attrs={'class':'songs-list-row__song-name'})) #.find_all('span')
    songs_list = [r.sub('', item.text) for item in items_list]

    # LIST SEARCHED SONGS
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
    request_body = json.dumps({
            "name": "Yuvals Example Playlist",
            "description": "My first programmatic playlist",
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