<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2033/day33banner.png" alt="Day 33 - ISS Overhead Notifier Banner" width="100%">
</p>

# Day 33  — ISS Overhead Notifier 🛰️

A script that checks whether the International Space Station is currently overhead **and** it's nighttime, and emails a "look up" alert when both conditions are true. Built while learning to work with API endpoints and query parameters.

## 🗂️ Project Structure

```
DAY 33/
├── iss_tracker.py       # main ISS overhead + email notifier
├── kanye_quotes_start.py # exploratory script for the sunrise-sunset API
└── README.md
```

## ⚙️ How It Works

### `iss_tracker.py`
- **`is_iss_overhead()`:** Calls the Open Notify ISS API (`api.open-notify.org/iss-now.json`) to get the ISS's current latitude/longitude, and checks whether it's within ±5° of your set location.
- **`is_night()`:** Calls the Sunrise-Sunset API (`api.sunrise-sunset.org/json`) with your lat/long as query parameters, extracts the sunrise/sunset hour, and compares it against the current hour to determine if it's night.
- **Main loop:** Runs continuously (`while True`), and whenever both checks pass, sends an email via `smtplib` alerting that the ISS is overhead.

### `kanye_quotes_start.py`
An earlier exploratory/scratch script (despite the filename) used to work out the Sunrise-Sunset API call — fetching sunrise/sunset times and printing the current hour before that logic was folded into `is_night()` in the main tracker.

## 🐛 Notes on the current code

- **Longitude check bug:** in `is_iss_overhead()`, the longitude comparison uses `iss_latitude` twice instead of `iss_longitude`:
  ```python
  if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_latitude <= MY_LONG+5:
  ```
  The second condition should compare against `iss_longitude`, otherwise the longitude check is meaningless.
- **Missing port/TLS setup consistency:** `smtplib.SMTP("smtp.gmail.com")` doesn't specify port `587` explicitly (relies on the default), which usually still works with `starttls()`, but being explicit (`smtplib.SMTP("smtp.gmail.com", 587)`) matches your other projects' style.
- **Credentials hardcoded:** as with Day 32, `MY_EMAIL`/`MY_PASSWORD` should move to environment variables before pushing to a public repo, and Gmail requires an App Password when 2FA is enabled.
- **No sleep/delay in the loop:** the `while True` loop calls both APIs back-to-back with no `time.sleep()`, which will hammer both APIs repeatedly — adding something like `time.sleep(60)` per iteration would be more considerate of the free API rate limits.

## 🧠 Concepts Practiced

- Making GET requests with the `requests` library
- Working with query parameters (`params=`)
- Parsing and navigating JSON API responses
- Combining multiple APIs to drive conditional logic
- Sending automated email alerts with `smtplib`
- Continuous polling with a `while True` loop

## 🚀 Run It

```bash
python iss_tracker.py
```

---
⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
