# Youtube:
## Prerequisits:
#### enable youtube v3 api:
https://console.cloud.google.com/apis/library/youtube.googleapis.com?project={project id}

## Youtube api creadentials json file: 
ref: https://developers.google.com/people/quickstart/python
https://www.youtube.com/watch?v=E4lX2lnKsPM

1. go to https://console.cloud.google.com/apis/credentials?project={project}
2. 'create credentials' --> 'OAuth client ID' --> select 'Desktop app' + enter name --> Create 
3. update json path 

2. add mail under test users: https://console.cloud.google.com/apis/credentials/consent?project={project id}
ref: https://developers.google.com/identity/protocols/oauth2/production-readiness/brand-verification?hl=en#submit-app-for-verification

# Spotify:
## Spotify user id:
1. login to spotify
2. Getting user id:
    a. In spotify app or web, click icon on top right
    b. click 'Account'
    c. In opened page, under 'Account overview' copy 'Username' string into the sctipt (line 35)  
## Spotify secret token:
1. login into: https://developer.spotify.com/console/get-recommendations/
2. At the bottom of the page click 'GET TOKEN', mark:
    - playlist-modify-private # For private playlists
    - playlist-modify-public # For public playlists
3. copy token in 'OAuth Token' box and past it into the script (line 36)


# Run python script :)
`python main.py`


