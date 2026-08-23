<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2049/day49banner.png" alt="Day 49 - Gym Booking Bot Banner" width="100%">
</p>

# Day 49 - Automating Your Gym Booking 🏋️🤖

A Selenium bot that logs into a gym's class scheduling site, automatically books (or joins the waitlist for) every Tuesday and Thursday 6pm class, then verifies all bookings went through by cross-checking the "My Bookings" page.

## 🗂️ Project Structure

```
DAY 49/
└── gym_routine.py
```

## ⚙️ How It Works

- **Persistent Chrome profile:** Uses a dedicated `chrome_profile` folder (via `--user-data-dir`) so the browser session/login can persist across runs, and `detach=True` keeps the window open after the script finishes.
- **Login:** Uses `WebDriverWait` with `expected_conditions` to reliably wait for the login button, email field, and schedule page to be ready before interacting — far more robust than fixed `sleep()` calls.
- **Finding target classes:** Loops through every class card, walks up to its parent day-group to read the day title (`h2`), and filters for cards on Tuesday **or** Thursday at **6:00 PM**.
- **Booking logic:** For each matching class, checks the button's current text and handles all four states: already `Booked`, already `Waitlisted`, `Book Class` (clicks to book), or `Join Waitlist` (clicks to join) — tracking each outcome in separate counters and a detailed `processed_classes` list.
- **Verification step:** After booking, navigates to the "My Bookings" page and re-counts every Tuesday/Thursday 6pm entry found there, comparing that count against the total processed during booking to confirm everything actually went through — printing a clear ✅ success or ❌ mismatch message.

## 🐛 Notes on the current code

- **No retry/resilience layer:** unlike some earlier iterations of this script, this version doesn't wrap the login or booking actions in a retry loop — if a `TimeoutException` fires due to a slow page load, the script will crash rather than retry. Wrapping the login and booking steps in a small retry helper (catching `TimeoutException` and reattempting a few times) would make it more resilient to flaky loads.
- **Booking summary section is commented out:** the `--- BOOKING SUMMARY ---` block that prints new bookings/waitlists/already-booked counts is currently disabled — only the verification step's totals get printed. Uncommenting it would give a fuller picture per run.
- **Hardcoded credentials:** `ACCOUNT_EMAIL` and `ACCOUNT_PASSWORD` are hardcoded at the top of the script — worth moving to environment variables before this goes on a public repo, especially since a real-looking password pattern is visible here.

## 🧠 Concepts Practiced

- Explicit waits with `WebDriverWait` and `expected_conditions` (far more reliable than `time.sleep()`)
- Persistent browser sessions via Chrome user profiles
- XPath for traversing up the DOM (`./ancestor::div[...]`)
- Conditional multi-state UI handling (booked / waitlisted / bookable / joinable)
- Exception handling (`NoSuchElementException`) for defensive scraping
- End-to-end verification: confirming actions actually took effect, not just assuming success

## 🚀 Run It

```bash
pip install selenium
python main.py
```

> Note: requires a matching ChromeDriver on your system PATH, and a pre-created account on the target gym site.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
