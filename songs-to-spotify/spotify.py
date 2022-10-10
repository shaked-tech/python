import requests
import json
import re
import logging as log

class Spotify:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

    def verify_response(self, response):
        if response.status_code == 401:
            print(f'Unauthorized response, got: {response.status_code}')
            print(f'verify \'user-id\' is correct and \'self.token\' has the needed permissions')
            exit(1)
        elif ((response.status_code != 201) and (response.status_code != 200)):
            print(f'errored response, got: {response.status_code}')
            exit(2)
        return


    # TODO: Update to_spotify function to use info (from 1) instead of html
    def to_spotify(self, playlist_name, songs_list):
        RE = re.compile("[|]|(|)|feat.|/|\\\\")
        uris = []
        ## FILTERS
        limit=1
        # market="US"
        # seed_genres="indie"
        # target_danceability=0.9
        # seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
        # seed_tracks='55SfSsxneljXOk5S3NVZIW'
        
        # CREATE PLAYLIST
        create_playlist_url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        print(create_playlist_url)
        log.info(f"Creating playlist '{playlist_name}':")
        request_body = json.dumps({
                "name": playlist_name,
                "description": f"Python uploaded {playlist_name}",
                "public": False
                })
        response = requests.post(url = create_playlist_url, 
                                 data = request_body, 
                                 headers={"Content-Type":"application/json", 
                                         "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)
        log.debug("playlist created")
        playlist_id = response.json()['id']
        
        # LIST SEARCHED SONGS
        search_url = "https://api.spotify.com/v1/search"
        not_found_list = []
        print("Searching songs:")
        for song in songs_list: 
            # preform query
            query = f'{search_url}?q={song}&limit={limit}&type=track'

            # get matched songs
            response = requests.get(query, 
                                    headers={"Content-Type":"application/json", 
                                             "Authorization":f"Bearer {self.token}"})

            response_json = response.json()
            track_list = response_json.get('tracks')['items'][0]
            track_uri = track_list['uri']
            track_name = track_list['name']
            track_artist = track_list['artists'][0]['name']

            if ((response.status_code != 201) and (response.status_code != 200)):
                not_found_list += [song]
                log.info(f"\"{track_name}\" by {track_artist}, Was not found")
            else:
                uris.append(track_uri)
                log.debug(f"\"{track_name}\" by {track_artist}")

        
        # UPLOAD SONGS TO PLAYLIST
        upload_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

        # split requests into chunks
        n = 100
        uris = [uris[i:i + n] for i in range(0, len(uris), n)]
        for l in uris:
            request_body = json.dumps({"uris" : l})
            response = requests.post(url=upload_url,
                                     data=request_body, 
                                     headers={"Content-Type":"application/json",
                                             "Authorization":f"Bearer {self.token}"})
            self.verify_response(response)

        print(f'Done, Added {len(songs_list) - len(not_found_list)} Checkout your new playlist: {playlist_name}')
        if len(not_found_list) != 0:
            print(f'Though could not find {len(not_found_list)} songs: {not_found_list}')
