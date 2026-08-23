<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2050/day50banner.png" alt="Day 50 - Auto Swipe Bot Banner" width="100%">
</p>

# Day 50 - Auto Swipe Bot 💘🤖

A Selenium bot that logs into Tinder via Facebook authentication and automatically clicks "Like" on profiles up to the free-tier daily limit, handling popups, multi-window auth flows, and match notifications along the way.

## 🗂️ Project Structure

```
DAY 50/
└── tinder_bot.py
```

## ⚙️ How It Works

- **Login flow:** Opens Tinder, clicks "Log in", then clicks the Facebook login option — which opens a **second browser window** for Facebook's own login form.
- **Multi-window handling:** Captures both window handles, switches to the Facebook popup window to enter email/password and submit with `Keys.ENTER`, then switches back to the main Tinder window to continue.
- **Onboarding popups:** Dismisses the location-permission prompt, notifications prompt, and cookie-consent banner, all located via absolute XPath.
- **Swiping loop:** Runs up to 100 iterations (Tinder's free daily like limit), clicking the "Like" button once per second.
- **Match handling:** If a "Like" click is intercepted by a "It's a Match!" popup (`ElementClickInterceptedException`), it locates and dismisses the popup instead, then continues. If the Like button hasn't rendered yet (`NoSuchElementException`), it waits 2 seconds before the next attempt.

## ⚠️ Important Notes

- **Automating Facebook/Tinder logins likely violates both platforms' Terms of Service.** Both explicitly prohibit automated access, bots, and scripted interactions with their login and swipe systems, and doing so can result in account suspension or a permanent ban. This is best treated as a Selenium *learning exercise* (multi-window handling, popup/exception handling, rate-limited loops) rather than something to run against a real account regularly.
- **Real credentials were shared in this conversation.** Since a real email and what looks like a real password were pasted directly into the code here, it's strongly worth changing that Facebook password now and moving credentials to environment variables (`os.environ`) or a `.env` file (excluded via `.gitignore`) going forward — never commit real login credentials to a public GitHub repo.
- **Absolute XPaths are fragile:** selectors like `//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button` are tightly coupled to Tinder's exact current DOM structure — any UI update on Tinder's end would likely break this script immediately.

## 🧠 Concepts Practiced

- Multi-window/tab handling in Selenium (`window_handles`, `switch_to.window()`)
- Locating elements via XPath and CSS selectors
- Simulating keyboard input (`Keys.ENTER`)
- Exception-driven control flow (`ElementClickInterceptedException`, `NoSuchElementException`)
- Rate-limited automation loops respecting a platform's usage limits
- Handling unpredictable UI states (popups appearing mid-loop)

## 🚀 Run It

```bash
pip install selenium
python tinder_bot.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
