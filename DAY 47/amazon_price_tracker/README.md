<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2047/amazon_price_tracker/day47banner.png" alt="Day 47 - Amazon Price Tracker Banner" width="100%">
</p>

# Day 47 - Amazon Price Tracker 🛒💸

An Amazon price-drop tracker, built up in three progressive stages — from basic price scraping to a full email alert system with environment variables and anti-bot request headers.

## 🗂️ Project Structure

```
DAY 47/
├── main1.py    # Stage 1: basic price scraping (practice site)
├── main2.py    # Stage 2: + email alert + dotenv environment variables
├── main3.py    # Stage 3: + request headers to scrape live Amazon
├── .env        # (not committed) SMTP_ADDRESS, EMAIL_ADDRESS, EMAIL_PASSWORD
└── README.md
```

---

## Stage 1 — `main1.py`: Basic Price Scraping

Scrapes a practice product page (`appbrewery.github.io/instant_pot`), finds the price element by its `a-offscreen` class, strips the `$` sign, and converts it to a float.

**Concepts:** `requests` + `BeautifulSoup` basics, class-based element selection, string splitting and type conversion.

---

## Stage 2 — `main2.py`: Adding Email Alerts

Builds on Stage 1 by also grabbing the product title, setting a `BUY_PRICE` threshold, and sending an email via `smtplib` if the price drops below it. Credentials are loaded securely from a `.env` file using `python-dotenv` and `os.environ`, rather than being hardcoded.

**Concepts:** Conditional alerting logic, `smtplib` email sending, environment variables for secrets (`load_dotenv()`, `os.environ`).

---

## Stage 3 — `main3.py`: Scraping the Live Amazon Page

Switches from the practice URL to the actual live Amazon product page, and adds a `User-Agent`/`Accept-Language` request header to avoid being blocked as a bot — a real obstacle when scraping Amazon directly (a fuller header set is shown commented out as an alternative/fallback). Also lowers `BUY_PRICE` to a more realistic threshold for the real product.

**Concepts:** Spoofing request headers to bypass basic bot detection, adapting a scraper from a practice sandbox to a real-world target site.

## 🐛 Notes on the current code

- **`main3.py` has a leftover debug print:** `print(soup.prettify())` right after the request will dump the entire page HTML to the console — useful while confirming Amazon isn't blocking you, but worth removing (or commenting out) for normal runs.
- **`.env` should be in `.gitignore`:** since it holds real email credentials, make sure it's excluded from the repo (only commit an `.env.example` with placeholder keys if you want to document the expected variables).
- **Scraping Amazon directly can break unpredictably:** even with headers, Amazon may still show CAPTCHAs or a different layout depending on IP/session, so `main3.py` is the most fragile of the three and may need occasional adjustment.

## 🧠 Concepts Practiced (Overall)

- Progressive project development (practice → full feature → real-world hardening)
- Web scraping with `BeautifulSoup`
- Automated email alerts with `smtplib`
- Secrets management with `python-dotenv`
- Bypassing basic bot detection with custom request headers

## 🚀 Run It

```bash
pip install beautifulsoup4 requests python-dotenv
python main3.py   # the most complete, production-style version
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
