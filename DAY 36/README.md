<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2036/day36banner.png" alt="Day 36 - Stock News Alert Banner" width="100%">
</p>

# Day 36 - Stock News Alert 📈📰

A script that monitors a stock's daily price movement and, when it swings enough, pulls related news headlines and texts them straight to your phone via Twilio.

## 🗂️ Project Structure

```
DAY 36/
├── main.py
└── README.md
```

## ⚙️ How It Works

- **Fetching stock data:** Calls the Alpha Vantage `TIME_SERIES_DAILY` endpoint for `STOCK_NAME` (`TSLA`) and pulls the closing prices for yesterday and the day before.
- **Calculating movement:** Finds the absolute price difference and the percentage change between the two days, and picks a 🔺 or 🔻 emoji depending on whether the price went up or down.
- **Trigger condition:** If the percentage difference exceeds the threshold, the script fetches news.
- **Fetching news:** Queries the News API for articles mentioning `COMPANY_NAME` (`Tesla Inc`), and slices out the first 3 articles.
- **Formatting & sending:** Builds a message per article combining the stock symbol, direction emoji, percentage change, headline, and description, then sends each as a separate SMS using the Twilio Python client.

## 🐛 Notes on the current code

- **Percentage calculation bug:** `diff_percent = round(difference / float(yesterday_closing_price)) * 100` rounds *before* multiplying by 100, which collapses any value under 50% down to `0` or `100`. It should be `round(difference / float(yesterday_closing_price) * 100)` (multiply first, then round) to get an accurate percentage.
- **News query parameter typo:** `"qinTitle": COMPANY_NAME` isn't a valid News API parameter — the correct one is `"qInTitle"` (capital `I`), so as written this search term is likely being ignored by the API.
- **Threshold looks low for a "5% move" script:** the code checks `abs(diff_percent) > 1`, but the original goal (per the comments) was 5% — worth double-checking whether `1` was intentional or a placeholder.
- **Hardcoded secrets:** `STOCK_API_KEY`, `NEWS_API_KEY`, `TWILIO_SID`, `TWILIO_AUTH_TOKEN`, and both phone numbers are hardcoded directly in `main.py`. Since this is going to a public GitHub repo, these should move to environment variables (e.g. via `python-dotenv` and a `.gitignore`'d `.env` file) — and it'd be worth rotating/regenerating these specific keys since they've now been shared in this conversation.

## 🧠 Concepts Practiced

- Consuming multiple REST APIs (Alpha Vantage, News API) with `requests`
- List comprehension over dictionary data
- Percentage/difference calculations
- Conditional logic driving multi-step workflows
- Sending SMS programmatically with the Twilio API
- String formatting for readable notification messages

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
