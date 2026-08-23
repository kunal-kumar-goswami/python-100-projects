<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2053/day53banner.png" alt="Day 53 - Data Entry Automation Banner" width="100%">
</p>

# Day 53 - Data Entry Automation 📋🔁

A two-part automation pipeline: scrape rental property listings (link, address, price) from a Zillow clone site with `BeautifulSoup`, then automatically fill out and submit a Google Form once per listing using `Selenium`.

## 🗂️ Project Structure

```
DAY 53/
└── data_entry_automation.py
```

## ⚙️ How It Works

### Part 1 — Scraping
- Fetches the Zillow-clone listings page with a spoofed `User-Agent` header (to avoid basic bot-blocking).
- Extracts three parallel datasets via CSS selectors and list comprehension:
  - **Links** to each individual listing.
  - **Addresses**, cleaned up by stripping pipe symbols (`|`) and whitespace.
  - **Prices**, cleaned by removing the `/mo` suffix and any `+` symbol, keeping just the `$` amount — filtered to only elements actually containing a `$` sign.

### Part 2 — Auto-filling the Google Form
- Opens a Chrome session with `detach=True` so it stays open for review.
- Loops through every scraped listing and, for each one: navigates to the Google Form URL, locates the address/price/link short-answer fields by XPath, fills them with `send_keys()`, and clicks submit — repeating this for every listing found.

## 🐛 Notes on the current code

- **Placeholder form URL:** `driver.get("YOUR_GOOGLE_FORM_LINK_HERE")` is a literal placeholder string, not a real URL — this needs to be replaced with your actual Google Form link before the script can run.
- **Form XPaths are specific to one form layout:** the absolute XPaths (`//*[@id="mG61Hd"]/div[2]/...`) will only match a Google Form built with the same field order/structure as the one this was designed for — a differently structured form (extra fields, reordered questions) would need updated XPaths.
- **No delay between form submissions:** after `submit_button.click()`, the loop immediately moves to `driver.get(...)` for the next listing with only the initial 2-second `sleep`. Adding a short pause after submission (to let the "response recorded" confirmation load) would make this more reliable.
- **Price/address list lengths aren't verified against link count:** the loop uses `range(len(all_links))` to index into `all_addresses`/`all_prices`, assuming all three lists always end up the same length — if the page's scraping/filtering ever produces mismatched counts, this would throw an `IndexError` partway through.

## 🧠 Concepts Practiced

- Web scraping with `BeautifulSoup` and CSS selectors
- Data cleaning with string methods (`.replace()`, `.split()`, `.strip()`)
- List comprehension for parallel data extraction
- Chaining a scraping stage into a Selenium-driven form-filling stage
- Automating repetitive data-entry work end-to-end

## 🚀 Run It

```bash
pip install beautifulsoup4 requests selenium
python data_entry_automation.py
```

> Note: replace `"YOUR_GOOGLE_FORM_LINK_HERE"` with your actual Google Form URL, and update the field XPaths to match your form's structure before running.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
