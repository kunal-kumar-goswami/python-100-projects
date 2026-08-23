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
