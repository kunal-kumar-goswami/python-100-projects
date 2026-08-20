<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2035/day35banner.png" alt="Day 35 - Weather App Banner" width="100%">
</p>

# Day 35 / 100 — Weather App 🌦️

A feature-rich `tkinter` desktop weather app that looks up current conditions for a searched city via the OpenWeatherMap API, showing temperature, humidity, pressure, visibility, sunrise/sunset, and a matching weather icon — with local time computed from the city's actual timezone.

## 🗂️ Project Structure

```
DAY 35/
├── rain_tracker/
│   ├── main.py
│   ├── data.json
│   ├── api_key                    # config file (INI-style, holds the OpenWeather key)
│   ├── Image/                     # UI assets (borders, buttons, icons, backgrounds)
│   └── Icons/                     # weather-condition icons (clear, clouds, rain, haze, etc.)
└── README.md
```

## ⚙️ How It Works

- Built as a `Weather` class extending `Tk`, with the entire GUI built inside `__gui()` — search box, current-weather label, temperature display, sunrise/sunset info, and a bottom bar showing humidity, pressure, description, and visibility.
- **Threading:** the GUI is built on a background thread at startup, and each weather lookup also runs on its own thread (`self.threading()`) so the UI doesn't freeze while waiting on the network request.
- **Fetching weather:** `__get_weather()` reads the API key from a config file (`configparser`) and calls the OpenWeatherMap `/data/2.5/weather` endpoint.
- **Timezone-aware local time:** uses `timezonefinder.TimezoneFinder` to resolve the city's timezone from its lat/lon, then `pytz` + `datetime` to display the correct local time for that city (not the user's own local time).
- **Dynamic icon:** `place_image()` picks a weather icon (clear/clouds/rain/haze/default) based on the API's `weather[0]['main']` field.
- **Error handling:** catches `requests.exceptions.ConnectionError` for no internet, and shows friendly `messagebox` errors for city-not-found or empty input.
- **Reset/Exit:** `clear()` blanks all labels back to their default state; `exit()` asks for confirmation before closing.

## 🐛 Notes on the current code

- **Search box isn't actually used for the lookup:** the API request is hardcoded to `q=India` instead of using the value from the search box (`self.search.get()`), so every search currently returns the same result regardless of what's typed.
- **API key exposure:** the request URL has the OpenWeather API key hardcoded directly in the string, even though a `configparser`/`api_key` file is already being read just above it — the `api` variable is fetched but never actually used in the request. Worth wiring `api` into the URL and adding `api_key` to `.gitignore` so the real key isn't pushed to GitHub.
- **Broken image path in `set_image()`:** the path uses a comma instead of a `/` before the filename — `f"...Icons,{img}"` — which will raise a file-not-found error and looks like a typo of `/`.
- **Temperature conversion:** `weather['main']['temp'] - 273` is an approximate Kelvin→Celsius conversion; the precise offset is `273.15`, so results can be off by a fraction of a degree.

## 🧠 Concepts Practiced

- Consuming a REST API with `requests` and parsing JSON
- GUI programming with `tkinter`, absolute positioning via `.place()`
- Image handling with `Pillow` (`Image`, `ImageTk`)
- Multithreading to keep the UI responsive during network calls
- Timezone resolution and conversion (`timezonefinder`, `pytz`, `datetime`)
- Config file management with `configparser`
- Error handling with `try`/`except` and user-facing `messagebox` alerts

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
