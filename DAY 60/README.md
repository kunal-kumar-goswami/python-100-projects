<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2060/day60banner.png" alt="Day 60 - POST Requests and HTML Forms Banner" width="100%">
</p>

# Day 60 - POST Requests with Flask & HTML Forms 📬📝

Builds on the blog capstone by adding a fully working contact form — handling both `GET` and `POST` on the same route, reading submitted form data, and emailing it via `smtplib`.

## 🗂️ Project Structure

```
DAY 60/
├── main.py
├── static/
│   ├── assets
│   ├── css
│   ├── js
├── templates/
│   ├── index.html
│   ├── footer.html
│   ├── header.html
│   ├── post.html
│   ├── about.html
│   └── contact.html
└── README.md
```

## ⚙️ How It Works

- **Dual-method route:** `/contact` accepts both `GET` and `POST` — on `GET` it just shows the empty contact form (`msg_sent=False`); on `POST` it processes the submitted form.
- **Reading form data:** `request.form` gives access to the submitted fields (`name`, `email`, `phone`, `message`) from the HTML form's `POST` body.
- **Sending the email:** `send_email()` builds a plain-text email summarizing the submission and sends it via Gmail's SMTP server using `smtplib`, logging in with the site owner's own email/password.
- **Confirmation state:** after a successful `POST`, the same `contact.html` template is re-rendered with `msg_sent=True`, letting the template conditionally show a "message sent" confirmation instead of the form again.
- The rest of the app (`/`, `/about`, `/post/<int:index>`) carries over unchanged from Day 59.

## 🐛 Notes on the current code

- **Placeholder credentials:** `OWN_EMAIL = "YOUR OWN EMAIL ADDRESS"` and `OWN_PASSWORD = "YOUR EMAIL ADDRESS PASSWORD"` are literal placeholder strings — these need to be filled in with real values before the contact form can actually send anything. For a public repo, it's worth pulling these from environment variables (`os.environ`) rather than hardcoding real credentials directly.
- **Gmail requires an App Password** when 2-Step Verification is enabled — your regular account password won't work with `smtplib` in that case.
- **No form validation:** the code assumes `name`, `email`, `phone`, and `message` are always present in `request.form` — if a field were ever missing (e.g. a malformed request), this would raise a `KeyError`. Using `request.form.get("name", "")` style access would be more defensive.

## 🧠 Concepts Practiced

- Handling multiple HTTP methods (`GET`/`POST`) on a single Flask route
- Reading submitted form data via `request.form`
- Sending email programmatically from a web app (`smtplib`)
- Conditional template rendering based on request outcome
- Building a real, functional contact form end-to-end

## 🚀 Run It

```bash
pip install flask requests
python main.py
```

> Note: fill in `OWN_EMAIL` and `OWN_PASSWORD` (ideally via environment variables) before testing the contact form.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
