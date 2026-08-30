<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2093/day93banner.png" alt="Day 93 - Web Scraping Banner" width="100%">
</p>

# Day 93 - Professional Portfolio: Web Scraping — Chocolate Bar Ratings Scraper 🍫🕸️

A web scraping script that pulls the full Chocolate Bar Ratings database from Flavors of Cacao, filters it down to bars made from a specific country's cocoa beans, and pushes the matching records into a Google Sheet via the Sheety API — turning a public HTML table into structured, queryable data.

## 🗂️ Project Structure

```
DAY 93/
└── main.py
```

## ⚙️ How It Works

- **Fetching the page:** `requests.get()` downloads the raw HTML of the Flavors of Cacao database page, which `BeautifulSoup` then parses with the built-in `html.parser`.
- **Locating the table:** `soup.find_all('table')[0]` grabs the first (and only) table on the page, which holds every chocolate bar entry.
- **Building the DataFrame:** the table's `<th>` header cells become the DataFrame's column names, then every `<tr>` row (skipping the header row) has its `<td>` cells stripped of whitespace and appended as a new row via `df.loc[length] = cleaned_data`.
- **Filtering by country:** `df[df["Country of Bean Origin"] == search_word]` isolates only the rows where the bean origin matches the target country (`"Philippines"` in this run).
- **DataFrame → JSON:** `matching_rows.to_json(orient='records')` converts the filtered rows into a JSON string, which is then parsed back into a list of Python dictionaries with `json.loads()` for easy field access.
- **Pushing to Sheety:** each matching chocolate bar is repackaged into the nested `{"sheet1": {...}}` shape Sheety expects, then `requests.post()` sends it to the configured Sheety endpoint — one row appended to the connected Google Sheet per chocolate bar.

## 🐛 Notes on the current code

- **Unused CSS selector left in:** `soup.select(selector="#choco_database")` is run and printed but never actually used — the real table is grabbed separately via `find_all('table')[0]`, so this line (and its `print`) is leftover debugging code that can be removed.
- **Placeholder Sheety endpoint:** `SHEETY_ENDPOINT_API` is set to `'add_endpoint_here'` — the script will fail with a connection/URL error on the `requests.post()` call until a real Sheety project endpoint is filled in.
- **No response status checking before posting more:** the loop prints `sheet_response.status_code` and `.text` for visibility, but doesn't check for a failed request (e.g. `4xx`/`5xx`) before moving on to the next item, so one bad row wouldn't stop or flag the rest of the batch.
- **Fragile table selection:** `find_all('table')[0]` assumes the target table is always the first one on the page — if the site's HTML structure changes and adds another table above it, this would silently scrape the wrong data.
- **Hardcoded search term:** `search_word = "Philippines"` is fixed in code rather than read from user input or a command-line argument, so reusing the script for a different country currently requires editing the source.

## 🧠 Concepts Practiced

- Making HTTP requests to fetch raw HTML with `requests`
- Parsing and navigating HTML with `BeautifulSoup`
- Extracting table headers and rows into a structured `pandas` DataFrame
- Filtering tabular data based on column values
- Converting between DataFrames, JSON strings, and Python dictionaries
- Integrating with a third-party REST API (Sheety) to write scraped data into a Google Sheet
- Basic end-to-end ETL: **E**xtract (scrape) → **T**ransform (filter/reshape) → **L**oad (POST to API)

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
