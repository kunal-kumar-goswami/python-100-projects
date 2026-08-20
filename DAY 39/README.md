<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2039/day39banner.png" alt="Day 39 - Flight Deal Finder Banner" width="100%">
</p>

# Day 39 - Flight Deal Finder ✈️💰

The start of a flight-deal-finder project: pulls a list of destination cities from a Google Sheet, resolves missing IATA airport codes via a flight search API, then checks flight prices for each destination over a 6-month window to find the cheapest option.

## 🗂️ Project Structure

```
DAY 39/
├── main.py
├── data_manager.py    # DataManager class — reads/writes the Google Sheet
├── flight_search.py   # FlightSearch class — talks to the flight search API
├── flight_data.py     # find_cheapest_flight() helper + flight data structure
└── README.md
```

## ⚙️ How It Works

- **Loading destinations:** `DataManager` fetches the destination sheet data (city names, and possibly-empty IATA codes) from a connected Google Sheet.
- **Filling in missing airport codes:** For every row without an `iataCode`, `FlightSearch.get_destination_code()` looks it up via the city name, with a 2-second delay between calls to stay under the API's rate limit. The updated codes are then written back to the sheet with `update_destination_codes()`.
- **Searching flights:** For each destination, `FlightSearch.check_flights()` queries flights from the origin (`LON`) to the destination's IATA code, searching a window from tomorrow to roughly 6 months out.
- **Finding the cheapest option:** `find_cheapest_flight()` (from `flight_data.py`) picks the lowest-priced flight from the results, and the price is printed per destination.
- This is a foundational version — it currently just finds and prints the cheapest flights, without yet emailing/texting alerts for good deals (a likely next step in later days).

## 🧠 Concepts Practiced

- Multi-module OOP project structure (data, search, and logic separated into their own classes/files)
- Reading and writing data via a Google Sheets-backed API
- Rate-limiting API calls with `time.sleep()`
- Working with date ranges using `datetime` and `timedelta`
- Looping through structured data to drive repeated API calls
- Finding a minimum value from a collection of results

## 🚀 Run It

```bash
python main.py
```

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
