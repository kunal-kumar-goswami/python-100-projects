<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2032/day32banner.png" alt="Day 32 - Birthday Wisher Banner" width="100%">
</p>

# Day 32 — Automated Birthday Wisher 🎂✉️

A script that checks a birthdays CSV against today's date and automatically sends a personalized birthday email using `smtplib`, picking a random letter template each time.

## 🗂️ Project Structure

```
DAY 32/
├── birthdays.csv              # name, email, year, month, day
│   └── birthday.csv
│   └── main.py
└── README.md
```

## ⚙️ How It Works

- **Loading birthdays:** `birthdays.csv` is read into a `DataFrame`, then converted into a dictionary keyed by `(month, day)` for quick lookup.
- **Checking today's date:** `datetime.now()` gets today's date, and its `(month, day)` is checked against the birthdays dictionary.
- **Picking a letter:** If there's a match, a random line is chosen from `letter_templates/letter_1.txt`, and the `[NAME]` placeholder is replaced with the birthday person's name.
- **Sending the email:** Connects to Gmail's SMTP server (`smtp.gmail.com`, port `587`), starts TLS, logs in, and sends the personalized message via `sendmail()`.
- If no birthday matches today, the script prints a message and exits without sending anything.

## 🔐 Security Note

The current script has the email and password hardcoded directly in `main.py` (`my_email`, `password`). For real use, these should be pulled from environment variables (e.g. `os.environ.get("EMAIL_PASSWORD")`) or a `.env` file that's excluded from version control — never commit real credentials to a public repo. Gmail also requires an **App Password** (not your regular password) when using SMTP with 2FA enabled.

## 🧠 Concepts Practiced

- Sending automated emails with `smtplib` and TLS
- Reading and indexing tabular data with `pandas`
- Working with dates via `datetime`
- Random selection from a list (`random.choice`)
- Basic templating with string `.replace()`
- Environment-based secrets management (as a best practice, not yet implemented)

## 🚀 Run It

```bash
python main.py
```

> Tip: schedule this script to run daily (e.g. via cron or Task Scheduler) so it checks for birthdays automatically every day.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
