import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

# Set up authentication using Client Credentials Flow
CLIENT_ID = "f1b7f2f0c5ca4e3ca5ba43f0f015a329"
CLIENT_SECRET = "fe2889902dee4d28bdf701dd936ae6d9"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_songs_from_year(year):
    # Fetch top 50 tracks of that year
    results = sp.search(q=f"year:{year}", type="track", limit=50)
    songs = []
    
    for track in results['tracks']['items']:
        song_details = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'uri': track['uri']
        }
        songs.append(song_details)
    
    return songs

def create_playlist(name, description, year):
    user_id = "your_spotify_user_id"  # Your Spotify user ID
    playlist = sp.user_playlist_create(user_id, name, description=description)
    songs = get_songs_from_year(year)
    
    # Prepare song URIs to add to playlist
    song_uris = [song['uri'] for song in songs]
    
    # Add songs to the playlist
    sp.playlist_add_items(playlist['id'], song_uris)
    return playlist['id']

# Example: Create a playlist for the year 1990
year = 1990
playlist_name = f"Musical Time Machine - {year}"
playlist_description = f"A playlist filled with songs from {year}."

playlist_id = create_playlist(playlist_name, playlist_description, year)
print(f"Playlist created! You can listen to it here: https://open.spotify.com/playlist/{playlist_id}")

