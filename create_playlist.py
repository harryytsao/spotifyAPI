import requests

SPOTIFY_CREATE_PLAYLIST_URL = "https://api.spotify.com/v1/users/Haroldinho/playlists" 
ACCESS_TOKEN = 'BQAXvzDUImFcpl_p8Z0KE6zoh9NbzZ2OnLy8SodwXRY8Rr71PJ8vJI7V1qUJW3GwqrMq1yHNHaaCYdXF3xXAoM8jvdt0lfnvTukVfE-HLpROSEz8CLpnjb0VrYHEfvOuMryWPpQYdx5641VetDhlSwcuwZPvls3w4Jp4N6Yxh2bNQo-oLU4_EOkCPUCLN-FirG6xV0Ob7dFYQzYhY0uJmvVaNBEjoNQgFZyCaFKLAi9-9w'

def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f'Bearer {ACCESS_TOKEN}'
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def main():
    playlist = create_playlist_on_spotify(
        name ="My Private Playlist",
        public=False
    )
    print(f'Playlist: {playlist}')


if __name__ == '__main__':
    main()