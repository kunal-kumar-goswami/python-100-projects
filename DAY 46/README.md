<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2046/day46banner.png" alt="Day 46 - Musical Time Machine Banner" width="100%">
</p>

# Day 46 - Musical Time Machine 🎵⏳

A "time machine" app: type in a date, and the script scrapes that week's Billboard Hot 100 chart, searches Spotify for each track, and builds a brand-new private Spotify playlist made entirely of songs from that exact date.

## 🗂️ Project Structure

```
DAY 46/
├── main.py
├── musical_timemachine.py
├── sportify_playlist.py
├── topmusics.py
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

- **Date input:** Prompts the user for a date in `YYYY-MM-DD` format.
- **Scraping Billboard:** Builds the Billboard Hot 100 URL for that date, fetches it with a spoofed `User-Agent` header (to avoid being blocked), and parses song titles out with `BeautifulSoup` using a CSS selector (`li ul li h3`).
- **Spotify authentication:** Uses `spotipy`'s `SpotifyOAuth` to authenticate with `playlist-modify-private` scope, caching the token locally in `token.txt` so re-authentication isn't needed on every run.
- **Matching songs on Spotify:** For each scraped title, searches Spotify filtered by track name and release year, grabbing the first match's URI — songs with no match are skipped with a printed notice.
- **Creating the playlist:** Creates a new private playlist named `"{date} Billboard 100"` under the authenticated user's account, then adds all found song URIs to it in one batch call.

## 🐛 Notes on the current code

- **Client credentials placeholders:** `client_id=YOUR-CLIENT-ID` and `client_secret=YOUR-CLIENT-SECRET` in the code as shown are unquoted placeholder names, not actual strings — these need to be either real string values (`"your_actual_client_id"`) or, better, pulled from environment variables (`os.environ.get("SPOTIFY_CLIENT_ID")`) so real credentials never end up hardcoded in a public repo.
- **`token.txt` shouldn't be committed:** since it caches an OAuth token tied to your Spotify account, it's worth adding to `.gitignore`.
- **Billboard scraping is fragile:** like Day 45's Hacker News scraper, this relies on Billboard's current HTML structure (`li ul li h3`) — if their markup changes, the selector will need updating.

## 🧠 Concepts Practiced

- Web scraping with `BeautifulSoup` and spoofed request headers
- OAuth authentication flow with `spotipy`
- Working with the Spotify Web API (search, create playlist, add items)
- Token caching to avoid repeated logins
- Error handling for missing search results (`IndexError`)
- Chaining a scraping step into an API-driven workflow

## 🚀 Run It

```bash
pip install -r requirements.txt
python main.py
```

---
⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
