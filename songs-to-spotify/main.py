import logging as log
import os
from youtube import Youtube
from spotify import Spotify

if __name__ == '__main__':
    LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
    log.basicConfig(level=LOGLEVEL)

    youtube_client_secrets_file = "youtube-access-shaked-personal.json"
    youtube = Youtube(youtube_client_secrets_file)

    spotify_user_id = 'qi8ub1qrzxh6rryhfwqfmvkip' # shaked
    spotify_token = 'BQDVP-iCFnrS8p40kvPHcd9Tp2MkBFQyyxH-kj5N8MG2CuOFfcR-uo2eCqZTxrWSFU4Ll6GM-biOaSVAJoq2Yz_qhgEB2PljKRv7lP8T4s1SPWBuQH9aae4fI_g22296M9wGf95S-0II8O6QqOph7FhuWjt-scASFPtD8Ur9KM7ZMMr-CqIAPUaf2LQ6AMK6DJG2znJ_6um4l-EswVlwGFdKAVWHswZxvgaDbGF6LmmX3ltW-SIyMR4xdKjy_bTs'
    spotify = Spotify(spotify_user_id, spotify_token)

    ## playlist_ids = youtube.get_playlists_ids()

    # playlist_ids = ['PLJclgFOW9FR4Y59_fiZzHx_tJCrb8WLXT',
    #                 'PLJclgFOW9FR5CgCCp0mDUx39YOleVch3R',
    #                 'PLJclgFOW9FR46XTiX8lkmgIJ98gpW_Hs8',
    #                 'PLJclgFOW9FR6tIviqxqTIjmzd988U5ULW']

    playlist_ids = ['PLJclgFOW9FR4Y59_fiZzHx_tJCrb8WLXT']
    for playlist_id in playlist_ids:
        playlist_name_id_list = youtube.get_playlist_name_by_ids(playlist_ids)
        playlist_name = list(playlist_name_id_list[0].values())[0]

        songs_list = youtube.get_songs_by_playlist_id(playlist_id)
        spotify.to_spotify(playlist_name, songs_list)


    ## to_spotify(html_file)
