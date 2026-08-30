<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2096/day96banner.png" alt="Day 96 - HTTP Requests & APIs Banner" width="100%">
</p>

# Day 96 - Professional Portfolio: HTTP Requests & APIs — Tesla News Email Digest 📰📧

A two-part automation script that pulls the latest Tesla-related articles from NewsAPI and emails a formatted digest straight to an inbox via Gmail's SMTP server — split cleanly into a data-fetching script and a reusable email-sending module.

## 🗂️ Project Structure

```
DAY 96/
├── new.py
└── send_email.py
├── README.md
```

## ⚙️ How It Works

- **`new.py` — fetch & format:** builds the NewsAPI `/v2/everything` endpoint URL with a `q=tesla` query, sorted by `publishedAt` so the newest articles come first, and authenticates using an API key pulled from the `NEWSAPI_KEY` environment variable.
- **Response validation:** `response.raise_for_status()` immediately raises an exception if NewsAPI returns an error status (bad key, rate limit, etc.), preventing the script from silently continuing with an empty or invalid response.
- **Building the digest body:** loops through every article in `content["articles"]`, skipping any without a title, and appends each article's title and description (falling back to an empty string if no description exists) into a single plain-text `body` string separated by blank lines.
- **`send_email.py` — reusable mailer:** a standalone `send_email(message)` function that takes any plain-text string and emails it — completely decoupled from where that string came from, so it could be reused by any other script that just needs to "send this text as an email."
- **Secure SMTP delivery:** connects to Gmail's SMTP server over SSL (`smtplib.SMTP_SSL` on port `465` with an `ssl.create_default_context()`), logs in using a Gmail address and an app-specific password (both from environment variables), and sends the message with a fixed `"Tesla News Update"` subject line.
- **Flexible recipient:** `RECEIVER_EMAIL` is read from the environment with a fallback to the sender's own address, so the digest can be sent to a different inbox without changing any code.

## 🐛 Notes on the current code

- **No handling for an empty article list:** if NewsAPI returns zero matching articles, `body` stays an empty string and `send_email()` still fires off a blank email rather than skipping the send or noting "no news today" in the message.
- **Unbounded digest length:** every article returned by the API is included with no limit (e.g. `content["articles"][:10]`), so a busy news day could produce a very long single email rather than a curated top-N digest.
- **Fixed search term and subject line:** `q=tesla` and the `"Tesla News Update"` subject are hardcoded in their respective files, so reusing this for a different topic currently means editing source code rather than passing a parameter.
- **No retry or rate-limit handling:** `raise_for_status()` will crash the script outright on a `429` (rate limited) or transient `5xx` error, with no backoff/retry logic to handle temporary API hiccups gracefully — useful behavior if this script is ever run on a schedule (e.g. via cron).
- **Plain-text only:** the email is sent as `MIMEText(..., "plain", ...)`, so article titles and descriptions arrive as an undecorated wall of text — no clickable links back to the original articles, since NewsAPI's `url` field isn't included in the body.

## 🧠 Concepts Practiced

- Making authenticated GET requests to a third-party REST API (`requests`)
- Reading secrets and configuration safely from environment variables
- Validating HTTP responses with `raise_for_status()`
- Parsing and iterating over JSON API responses
- Sending email programmatically over SMTP with `smtplib` and SSL/TLS
- Structuring a project into a task script and a reusable, decoupled utility module
- Designing a function (`send_email`) around a single, generic responsibility

## 🚀 Run It

```bash
export NEWSAPI_KEY="your_newsapi_key"
export GMAIL_ADDRESS="your_email@gmail.com"
export GMAIL_APP_PASSWORD="your_app_password"
export RECEIVER_EMAIL="destination@example.com"   # optional

python new.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
