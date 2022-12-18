from os import environ
from youtube import Youtube
from spotify import Spotify

if __name__ == '__main__':
    LOGLEVEL = environ.get('LOGLEVEL', 'INFO').upper()

    youtube_client_secrets_file = "youtube-access-shaked-personal.json"
    youtube = Youtube(youtube_client_secrets_file)

    spotify_user_id = ''
    spotify_token = ''
    spotify = Spotify(spotify_user_id, spotify_token)

    playlist_ids = youtube.get_playlists_ids()
    for playlist_id in playlist_ids:
        playlist_name_id_list = youtube.get_playlist_name_by_ids(playlist_ids)
        playlist_name = list(playlist_name_id_list[0].values())[0]

        songs_list = youtube.get_songs_by_playlist_id(playlist_id)
        spotify.songs_to_spotify_playlist(playlist_name, songs_list)
