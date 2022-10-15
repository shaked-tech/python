import requests
import json
import logging as log

class Spotify:
    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token
        self.not_found_list = []

    def verify_response(self, response):
        status_code = response.status_code
        if ((status_code != 201) or (status_code != 200)):
            if status_code == 401:
                print(f'verify \'user-id\' is correct')
            elif status_code == 403:
                print(f'Make sure the token your using has the needed permissions (scopes)')
            else:
                print(f'errored response, got: {status_code}')
            raise(response.json())
        return True

    def get_user_playlists_ids(self): # 
        me_playlists_url = f'https://api.spotify.com/v1/users/{self.user_id}/playlists'

        response = requests.get(url = me_playlists_url, 
                                headers={"Content-Type":"application/json",
                                         "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)

        playlists_ids = [item['id'] for item in response.json()['items']] ## TEST
        return playlists_ids

    def get_playlists_name_by_id(self, playlist_id):
        playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
        response = requests.get(playlist_url,
                                headers={"Content-Type":"application/json", 
                                         "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)

        playlist_name = response.json()['name']
        return playlist_name

    def get_track_id_by_name(self, track_name):
        limit=1
        search_url = f'https://api.spotify.com/v1/search?q={track_name}&limit={limit}&type=track'

        response = requests.get(search_url, 
                                headers={"Content-Type":"application/json", 
                                            "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)
        response_json = response.json()

        if response_json['tracks']['total'] == 0:
            print(f"\"{track_name}\", Was not found")
            log.info(f"\"{track_name}\", Was not found")
            self.not_found_list.append(track_name)
            return False
        
        track_list = response_json.get('tracks')['items'][0]
        track_uri = track_list['uri']
        track_name = track_list['name']
        track_artist = track_list['artists'][0]['name']

        print(f"Found \"{track_name}\" by {track_artist}")
        log.info(f"Found \"{track_name}\" by {track_artist}")
        return track_uri

    def get_total_liked_tracks(self):
        my_tracks_url = 'https://api.spotify.com/v1/me/tracks?offset=0&limit=1'

        response = requests.get(my_tracks_url,
                                headers={"Content-Type":"application/json", 
                                        "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)
        json_response = response.json()

        print(json_response)
        total = json_response['total']
        print('You have {} liked tracks.'.format(total))
        return total

    def get_all_liked_tracks(self):
        total_retrieved = 0
        ids = []

        total = self.get_total_liked_tracks()
        while total_retrieved < total:
            query = f'https://api.spotify.com/v1/me/tracks?offset={total_retrieved}&limit=50'
            response = requests.get(query, 
                                    headers={"Content-Type":"application/json", 
                                            "Authorization":f"Bearer {self.token}"})
            self.verify_response(response)
            json_response = response.json()

            for i,j in enumerate(json_response['items']):
                ids.append(j['track']['id'])
                total_retrieved += 1
        return ids
            
    def get_tracks_ids_in_playlist(self, playlist_id):
        get_playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
        response = requests.get(get_playlist_url, 
                                headers={"Content-Type":"application/json", 
                                        "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)
        json_response = response.json()

        ids = [item['track']['id'] for item in json_response['items']]
        return ids

    def like_track_by_id(self, id): # scope: user-library-modify required
        like_track_url = f'https://api.spotify.com/v1/me/tracks?ids={id}'

        response = requests.put(like_track_url,
                                headers={"Content-Type":"application/json", 
                                        "Authorization":f"Bearer {self.token}"})
        self.verify_response(response)
        return True

    def like_all_tracks_in_playlist(self, playlist_id): # scope: user-library-modify, playlist-read-private required
        count = 0
        ids = self.get_tracks_ids_in_playlist(playlist_id)
        for id in ids:
            self.like_track_by_id(id)
            print('.', end=' ', flush=True)
            count += 1
        print(f"Liked {count} Songs!")
        return True

    def create_playlist(self, playlist_name):
        create_playlist_url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        print(create_playlist_url)
        print(f"Creating playlist '{playlist_name}':")
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
        return playlist_id

    def upload_tracks_to_playlist(self, playlist_id, tracks_uris_list):
        upload_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        # Split requests into chunks
        n = 100

        uris = [uris[i:i + n] for i in range(0, len(uris), n)]
        for l in uris:
            request_body = json.dumps({"uris" : l})
            response = requests.post(url=upload_url,
                                     data=request_body, 
                                     headers={"Content-Type":"application/json",
                                             "Authorization":f"Bearer {self.token}"})
            self.verify_response(response)

        playlist_name = self.get_playlists_name_by_id()
        print(f'Done, Added {len(tracks_uris_list) - len(self.not_found_list)} Checkout your new playlist: {playlist_name}')

    def tracks_to_spotify_playlist(self, playlist_name, tracks_list):
        tracks_uris = []

        # Create Playlist
        playlist_id = self.create_playlist(playlist_name)
        
        # List Searched Songs
        print("Searching songs:")
        for track_name in tracks_list: 
            track_uri = self.get_track_id_by_name(track_name)
            if track_uri:
                tracks_uris.append(track_uri)
            
        # Upload Songs To Playlist
        self.upload_tracks_to_playlist(playlist_id, tracks_uris)

        if len(self.not_found_list):
            print(f'Though could not find {len(self.not_found_list)} songs: {self.not_found_list}')
