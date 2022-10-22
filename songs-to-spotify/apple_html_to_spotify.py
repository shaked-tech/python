import getopt, sys
from signal import raise_signal
from bs4 import BeautifulSoup
from os import listdir, environ
from os.path import isfile, join
from re import compile
from spotify import Spotify

# regex string editing song name for reliable search
RE = compile("^[ \t]|[|]|(|)|feat.|/|\\\\|\n|[ \t]+$")

def print_help():
    print("""
    Python script to parse and list songs from apply playlist html files,
    and upload them to a given Spotify account. 

    -h, --help             Print script options.
    -a, --apple=songs      Format of html to use when reading html files.
    -H, --htmldir=''       Directory path to read html files from, file must end with '.html' file extention.
                           note that if one of -n|--playlistname flags are not provided, the defult name will be the given dir of html files.
    -f, --htmlfile=''      Html file to read from.
    -r, --readfile=''      File to read an existing song list from (line seperated format).
    -w, --writefile=''     File to write created song list to.
    -o, --output=info      Output level, one of: DEBUG, INFO, WARNING, ERROR, CRITICAL.     
    -n, --playlistname={subdir of htmlfile}    Name override to give to the created playlist.

    e.g. 
      $ python apple_html_to_spotify.py --apple playlist -H HtmlDir/path -n myNewPlaylist -o debug
    """)

def main():
    if not APPLE_PLAYLIST_FORMAT:
        raise getopt.error(f"APPLE_PLAYLIST_FORMAT if empty, one of: '-a|--apple' flags must be given")

    songs_parsed_list = []
    artists_parsed_list = []
    complete_songs_artists_list = []
    if HTML_DIR:
        songs_files = [(HTML_DIR + f'/{f}') for f in listdir(HTML_DIR) if isfile(join(HTML_DIR, f)) and f.endswith('.html')]
    else:
        songs_files = [SONG_FILE]


    for file in songs_files:
        print(f"reading from file {file}")
        with open(file) as f:
            html_file = f.read()

        parsed_html = BeautifulSoup(html_file, features="html.parser")

        ## Playlist:
        if APPLE_PLAYLIST_FORMAT == 'Playlist':
            song_list = (parsed_html.find_all('div', attrs={'class':'songs-list-row__song-name'}))
            artist_list = (parsed_html.find_all('div', attrs={'class':'songs-list__col--artist'}))
            # album_list = (parsed_html.find_all('div', attrs={'class':'songs-list__col--album'}))
        ## Songs (all):
        elif APPLE_PLAYLIST_FORMAT == 'songs':
            song_list = (parsed_html.find_all('div', attrs={'data-testid':'library-track__song'}))
            artist_list = (parsed_html.find_all('div', attrs={'data-testid':'library-track__artist'}))
            # album_list = (parsed_html.find_all('div', attrs={'data-testid':'library-track__album'}))
        else:
            raise getopt.error("APPLE_PLAYLIST_FORMAT not set")
        
        songs_parsed_list.extend([RE.sub('', item.text) for item in song_list])
        artists_parsed_list.extend([RE.sub('', item.text) for item in artist_list])

        if len(songs_parsed_list) == 0:
            raise("Somthing went wrong finding songs from html files. Please verify **search option is set correctly (Songs / Playlists)")
        if len(songs_parsed_list) != len(artists_parsed_list):
            raise("lists differant lengths, aborting")

        for i in range(len(songs_parsed_list)):
            if not songs_parsed_list[i].isascii():
                songs_parsed_list[i][::-1]
            if not artists_parsed_list[i].isascii():
                artists_parsed_list[i][::-1]
            complete_songs_artists_list.append(f"{songs_parsed_list[i]} {artists_parsed_list[i]}")

    # Create unique list
    complete_songs_artists_list = list(set(complete_songs_artists_list))

    ## write list to file:
    if SONGS_WRITE_FILE:
        with open(join(HTML_DIR, SONGS_WRITE_FILE), 'w+') as f:
            for i in range(len(complete_songs_artists_list)):
                f.write(complete_songs_artists_list[i] + '\n')
    ## read list from file:
    if SONGS_READ_FILE:
        with open(join(HTML_DIR, SONGS_READ_FILE, 'r')) as f:
            complete_songs_artists_list = [song.replace('\n', '') for song in f.readlines()]


    spotify_user_id = ''
    spotify_token = ''
    spotify = Spotify(spotify_user_id, spotify_token)

    if PLAYLIST_NAME_OVERRIDE:
        playlist_name = PLAYLIST_NAME_OVERRIDE
    else:
        playlist_name = HTML_DIR.split('/')[-1]
    spotify.songs_to_spotify_playlist(playlist_name, complete_songs_artists_list)

def verify_arg(Argument, Value):
    if Value == '':
        raise getopt.error(f"custom raise: option {Argument} requires argument")

def parse_args():
    # Remove 1st argument from the
    argumentList = sys.argv[1:]
    # Options
    options = "hr:w:o:a:d:H:n:"
    long_options = ["help", "readfile=", "writefile=", "output=", "apple=", "htmldir=", "playlistname="]
    try:
        # Parsing argument
        arguments, _ = getopt.getopt(argumentList, options, long_options)
        # Catch help
        if "-h" in argumentList or "--help" in argumentList:
            print_help()
            exit(0)
                
        # Checking each argument
        for currentArgument, currentValue in arguments:            
            verify_arg(currentArgument, currentValue)
            if currentArgument in ("-r", "--readfile"):
                global SONGS_READ_FILE
                SONGS_READ_FILE = currentValue

            elif currentArgument in ("-w", "--writefile"):
                global SONGS_WRITE_FILE
                SONGS_WRITE_FILE = currentValue
                
            elif currentArgument in ("--apple"):
                if currentValue != "songs" and currentValue != "playlist":
                    raise getopt.error(f"custom raise: invalid value '{currentValue}' for option {currentArgument}")
                global APPLE_PLAYLIST_FORMAT
                APPLE_PLAYLIST_FORMAT = currentValue
                
            elif currentArgument in ("-d", "--htmldir"):
                global HTML_DIR
                HTML_DIR = currentValue

            elif currentArgument in ("-f", "--htmlfile"):
                global SONG_FILE
                SONG_FILE = currentValue

            elif currentArgument in ("-n", "--playlistname"):
                global PLAYLIST_NAME_OVERRIDE
                PLAYLIST_NAME_OVERRIDE = currentValue

            elif currentArgument in ("-o", "--output="):
                if currentValue.upper() not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
                    raise getopt.error(f"custom raise: invalid value {currentValue}, for option '{currentArgument}'")
                environ["LOGLEVEL"] = currentValue
                            
    except getopt.error as err:
        print (str(err))

if __name__ == '__main__':
    parse_args()
    if not environ["LOGLEVEL"]:
        environ["LOGLEVEL"] = 'info'
    # main()


