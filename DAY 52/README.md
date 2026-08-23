<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2051/day51banner.png" alt="Day 52 - Insta Follower Bot Banner" width="100%">
</p>

# Day 52 - Instagram Follower Bot 📸🤖

A Selenium bot that logs into Instagram, opens the follower list of a chosen account, scrolls through it via JavaScript, and automatically follows everyone found — useful for growing a following around a similar niche account.

## 🗂️ Project Structure

```
DAY 52/
└── main.py
```

## ⚙️ How It Works

- **`InstaFollower` class:** wraps the whole workflow with a `detach=True` Chrome session so the browser stays open for manual review/logout afterward.
- **`login()`:** navigates to the Instagram login page, dismisses the cookie-consent dialog if present, enters username/password, submits, then dismisses the "Save login info" and notifications prompts that Instagram shows after a successful login.
- **`find_followers()`:** navigates to `SIMILAR_ACCOUNT`'s followers list, then scrolls the followers modal 5 times using `execute_script()` to run raw JavaScript (`scrollTop = scrollHeight`) — loading more followers into the DOM each time, since Instagram lazy-loads the list.
- **`follow()`:** finds every "Follow" button currently rendered in the modal and clicks each one. If a click is intercepted (because that person is already followed, which pops up an Unfollow/Cancel dialog instead), it catches the exception and clicks "Cancel" to skip that person safely.

## ⚠️ Important Notes

- **Automating follows on Instagram likely violates its Terms of Service**, which prohibit scripted/bot interactions outside the official API. Doing this at scale (or repeatedly) is a common trigger for temporary action blocks or permanent bans — this is best treated as a Selenium learning exercise (JS execution, dynamic modal scrolling, exception-driven UI handling) rather than a bot to run regularly against a real account.
- **Credentials are placeholders here** (`"YOUR_USERNAME"` / `"YOUR_PASSWORD"`) — good practice already, but when you fill these in for real, use environment variables (`os.environ`) rather than hardcoding the actual values directly in the file, especially since this repo is public.
- **Fragile absolute XPaths:** the cookie-dismissal XPath (`/html/body/div[6]/div[1]/...`) is tightly coupled to Instagram's current DOM structure and is likely to break whenever Instagram updates their layout — the code's own comment acknowledges this ("xpath of the modal will change over time").
- **No rate-limiting between follows beyond ~1 second:** Instagram is known to flag accounts for suspicious activity when following many accounts in quick succession — a longer, slightly randomized delay between follows (and following far fewer than the full list in one run) would be safer, if this were ever used for real.

## 🧠 Concepts Practiced

- Object-Oriented automation workflow design
- Executing raw JavaScript from Python via `execute_script()`
- Handling lazy-loaded / infinite-scroll content
- Exception-driven conditional UI handling (`ElementClickInterceptedException`)
- Multi-step login flows with conditional popups

## 🚀 Run It

```bash
pip install selenium
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
