import logging
import os
from youtube import Youtube
import spotify

if __name__ == '__main__':
    LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG').upper()
    logging.basicConfig(level=LOGLEVEL)

    # youtube_client_secrets_file = "youtube-access-shaked-personal.json"
    # youtube = Youtube(youtube_client_secrets_file)

    # # playlist_ids = youtube.get_playlists_ids()

    # playlist_ids = ['PLJclgFOW9FR4Y59_fiZzHx_tJCrb8WLXT',
    #                 'PLJclgFOW9FR5CgCCp0mDUx39YOleVch3R',
    #                 'PLJclgFOW9FR46XTiX8lkmgIJ98gpW_Hs8',
    #                 'PLJclgFOW9FR6tIviqxqTIjmzd988U5ULW']

    # playlist_name_list = youtube.get_playlist_name_by_ids(playlist_ids)
    # print(playlist_name_list)
    

    # spotify_user_id = ''
    # spotify_token = ''
    # spotify(spotify_user_id, spotify_token)

    ## to_spotify(html_file)
