<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2051/day51banner.png" alt="Day 51 - Internet Speed Bot Banner" width="100%">
</p>

# Day 51 - Internet Speed X (Twitter) Complaint Bot 📶🐦

A Selenium bot that runs a real Speedtest.net test, then automatically logs into X (Twitter) and tweets at your internet provider comparing your actual speed against what you're paying for.

## 🗂️ Project Structure

```
DAY 51/
└── twitter_bot.py
```

## ⚙️ How It Works

- **`InternetSpeedTwitterBot` class:** wraps the whole workflow in an OOP structure with `up`/`down` state and two main methods.
- **`get_internet_speed()`:** opens Speedtest.net, clicks the "Go" button to start a real speed test, waits 60 seconds for it to complete, then scrapes the download and upload results via absolute XPath.
- **`tweet_at_provider()`:** logs into X/Twitter (handling the email step and an optional extra username-confirmation step some accounts require), enters the password, composes a tweet comparing the measured speed (`self.down`/`self.up`) against the promised speed (`PROMISED_DOWN`/`PROMISED_UP`), and posts it.
- **Execution:** creates the bot instance, runs the speed test, then fires off the tweet — a simple two-step pipeline.

## ⚠️ Important Notes

- **Real credentials were shared in this conversation.** A real-looking email and password were pasted directly into the code. It's strongly worth changing that password now and switching to environment variables (`os.environ`) or a `.env` file (excluded via `.gitignore`) before this script is used again or the repo goes public.
- **Automating login and posting on X likely violates its Terms of Service**, which generally prohibit automated/scripted account access outside their official API. This is best treated as a learning exercise in browser automation rather than a bot to run regularly against a real account — repeated automated logins can also trigger suspicious-activity flags or a temporary lock.
- **Bare `except: pass`** in the optional username-confirmation step silently swallows *any* exception, not just the expected "element not found" case — if something else goes wrong there (e.g. a network hiccup), it would fail silently rather than surfacing the real error. Catching the specific exception (e.g. `NoSuchElementException`) would be safer.
- **Absolute XPaths for the speed results** are tightly coupled to Speedtest.net's current page layout — any UI change there would break the scraping step.

## 🧠 Concepts Practiced

- Object-Oriented design for a multi-step automation workflow
- Driving a third-party speed test tool via Selenium and scraping its results
- Multi-step login flows (handling optional/conditional confirmation screens)
- Composing and submitting dynamic text content via a web UI
- Chaining two automated workflows (test → tweet) into one script

## 🚀 Run It

```bash
pip install selenium
python twitter_bot.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
