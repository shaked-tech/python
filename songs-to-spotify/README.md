# Youtube:
## Prerequisits:
#### Enable youtube v3 api:
https://console.cloud.google.com/apis/library/youtube.googleapis.com?project={project id}

## Youtube api access: 
ref: https://developers.google.com/people/quickstart/python
https://www.youtube.com/watch?v=E4lX2lnKsPM

### Credentials file access (Recommended):
1. go to https://console.cloud.google.com/apis/credentials?project={project}
2. 'create credentials' --> 'OAuth client ID' --> select 'Desktop app' + enter name --> Create 
3. update json path 

### User authorised access:
ref: https://developers.google.com/identity/protocols/oauth2/production-readiness/brand-verification?hl=en#submit-app-for-verification
#### Add user mail address under test users:
https://console.cloud.google.com/apis/credentials/consent?project={project id}


# Spotify:
## Spotify user id:
1. login to spotify
2. Getting user id:
    a. Login to your spotify application or web, click icon on top right
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





# Apple Music
## Apple secret token 
Apple requires you to have a developers or admin user, and charges 99$ to create one ... good luck
- https://developer.apple.com/documentation/applemusicapi/generating_developer_tokens
- https://developer.apple.com/documentation/applemusicapi
