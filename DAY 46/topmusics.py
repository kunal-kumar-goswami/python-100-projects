import requests

def get_top_tracks_of_year(year):
    api_key = 'your_lastfm_api_key'  # Get your API key from https://www.last.fm/api
    url = f'https://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key={api_key}&format=json&from={year}-01-01&to={year}-12-31'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['tracks']['track']
    else:
        print(f"Error fetching data from Last.fm: {response.status_code}")
        return []

# Get Spotify links for the top tracks (fallback if no access to Spotify API)
def generate_spotify_links(top_tracks):
    spotify_links = []
    for track in top_tracks:
        song_name = track['name']
        artist_name = track['artist']['name']
        # Creating a Spotify URL by searching for the song and artist
        search_url = f"https://open.spotify.com/search/{song_name} {artist_name}"
        spotify_links.append(search_url)
    return spotify_links

# Main function to create the playlist for the given year
def main(year):
    print(f"Fetching top 100 songs for the year {year}...\n")
    top_tracks = get_top_tracks_of_year(year)

    if not top_tracks:
        print(f"No data found for the year {year}")
        return

    # Generate Spotify links
    spotify_links = generate_spotify_links(top_tracks)

    # Display the top 10 tracks (change this to 100 for the full list)
    print(f"Top 10 Tracks of {year}:")
    for idx, track in enumerate(top_tracks[:10]):
        song_name = track['name']
        artist_name = track['artist']['name']
        print(f"{idx+1}. {song_name} by {artist_name}")
        print(f"   Spotify Link: {spotify_links[idx]}")
    
    print("\nNote: The full list can be accessed by searching the links.")

# Example Usage: Get the playlist for a specific year
if __name__ == "__main__":
    year = int(input("Enter the year to fetch the top 100 songs: "))
    main(year)
