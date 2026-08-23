<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2048/day48banner.png" alt="Day 48 - Selenium WebDriver Banner" width="100%">
</p>

# Day 48 - Selenium WebDriver 🤖🌐

An introduction to browser automation with Selenium — launching and controlling a real Chrome browser, filling out forms, scraping page content, and building a bot that plays Cookie Clicker.

## 🗂️ Project Structure

```
DAY 48/
├── main.py         # Minimal browser launch demo
├── challenge.py     # Automated form-filling
├── intraction.py    # Locating and reading page elements (Wikipedia)
├── cookie.py         # Cookie Clicker automation bot
└── README.md
```

---

## 1️⃣ `main.py` — Launching a Browser

The simplest possible Selenium script: configures Chrome with the `detach` option (so the browser window stays open after the script finishes), opens Amazon, then explicitly closes and quits the driver.

**Concepts:** `webdriver.Chrome()`, `ChromeOptions`, `driver.get()`, `driver.close()` vs `driver.quit()`.

---

## 2️⃣ `challenge.py` — Automated Form Filling

Opens a sign-up form page, locates the first name, last name, and email input fields by their `value` (element `id`/`name`), fills them in with `send_keys()`, and clicks the submit button.

**Concepts:** Locating elements, simulating keyboard input, clicking buttons.

---

## 3️⃣ `intraction.py` — Reading Page Content

Opens the Wikipedia main page and locates the "Today's featured article" link/text to read it back.

**Concepts:** Element location with CSS-style selectors, extracting `.text` from a found element.

---

## 4️⃣ `cookie.py` — Cookie Clicker Bot 🍪

The most advanced script here: a bot that plays [Cookie Clicker](https://ozh.github.io/cookieclicker/) autonomously for 5 minutes.

- Selects the English language on load, then repeatedly clicks the big cookie.
- Every 5 seconds, checks the current cookie count and looks through all store items (`product0`–`product17`) in reverse order (most expensive first), buying the priciest one currently affordable (identified by the `"enabled"` CSS class).
- After 5 minutes, prints the final cookie count and stops.
- Uses proper exception handling (`NoSuchElementException`, `ValueError`) so a missing element or bad text-to-number conversion doesn't crash the bot.

**Concepts:** Timed automation loops, dynamic element re-querying, CSS attribute-based filtering, robust error handling in a long-running bot.

## 🧠 Concepts Practiced (Overall)

- Setting up and configuring the Selenium Chrome WebDriver
- Locating elements by ID, CSS selector, and value
- Simulating user interaction: typing, clicking
- Reading dynamic page content and numeric text parsing
- Building a timed, self-correcting automation loop
- Exception handling for resilient browser automation

## 🚀 Run It

```bash
pip install selenium
python cookie.py    # or any of the other scripts
```

> Note: requires a matching ChromeDriver installed and available on your system PATH.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
