import requests
import pandas as pd

def spotify_setup(CLIENT_ID, CLIENT_SECRET):
    try:
        auth_response = requests.post('https://accounts.spotify.com/api/token', {'grant_type':'client_credentials', 'client_id':CLIENT_ID, 'client_secret':CLIENT_SECRET})
        auth_response_data = auth_response.json()
        access_token = auth_response_data['access_token']
        global headers
        headers = {'Authorization':'Bearer {token}'.format(token=access_token)}
        print('Setup complete')
    except:
        print('Remember to paste your client ID and secret into the code')

def find_tracks(search_string):
    try:
        r = requests.get('https://api.spotify.com/v1/search?q=' + search_string + '&type=track', headers=headers)
        info = r.json()
    except:
        print('Error with search string:', search_string)
        print('Did you run spotify_setup(CLIENT_ID, CLIENT_SECRET) first?')
        info = None
    return info

def get_track_info(track_id):
    try:
        r = requests.get('https://api.spotify.com/v1/tracks/' + track_id, headers=headers)
        info = r.json()
    except:
        print('Error with track id:', track_id)
        print('Did you run spotify_setup(CLIENT_ID, CLIENT_SECRET) first?')
        info = None
    return info

def get_track_features(track_id):
    try:
        r = requests.get('https://api.spotify.com/v1/audio-features/' + track_id, headers=headers)
        info = r.json()
    except:
        print('Error with track id:', track_id)
        print('Did you run spotify_setup(CLIENT_ID, CLIENT_SECRET) first?')
        info = None
    return info

def get_playlist(playlist_id):
    tracks = []
    for x in range(50):  
        offset = x*100  # it only returns 100 tracks at a time
        try:
            r = requests.get('https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks?offset=' + str(offset), headers=headers)
            for item in r.json()['items']:
                tracks.append([item['track']['artists'][0]['name'], item['track']['name'], item['track']['id'], item['track']['album']['release_date']])
        except:
            print(offset)
            break
    pl = pd.DataFrame(tracks, columns=['artist', 'track', 'id', 'release_date'])

    track_features = {}
    for row in pl.itertuples():
        print(row[1], row[2]) # artist and track
        id = row[3]
        features = get_track_features(id)
        track_features[id] = features

    from IPython.display import clear_output
    clear_output()

    tf = pd.DataFrame(track_features).T
    playlist = pd.merge(pl, tf, on='id')
    return playlist