<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2091/day91banner.png" alt="Day 91 - HTTP Requests & APIs Banner" width="100%">
</p>

# Day 91 - Professional Portfolio: HTTP Requests & APIs — PDF to Speech Web App 📄🔊

A Flask web app that takes an uploaded PDF, extracts its text, and converts that text into a downloadable/playable MP3 using Google's Text-to-Speech (`gTTS`) — turning any document into an audiobook-style narration in just a couple of clicks.

## 🗂️ Project Structure

```
DAY 91/
├── main.py
├── static/
│   └── style.css
├── templates/
│   └── index.html

```

## ⚙️ How It Works

- **File upload route (`/`):** accepts `GET` and `POST` requests. On `POST`, the uploaded PDF is saved into the `uploads/` folder, and its text is immediately extracted and stored in the session so it persists across requests.
- **`extract_text_from_pdf()`:** uses `PyPDF2.PdfReader` to loop through every page of the uploaded PDF and concatenate the extracted text into a single string, skipping pages that return no text.
- **Session-based state:** `session['file_path']` and `session['text_to_convert']` keep track of the uploaded file and its extracted text between the upload step and the conversion step, so the user doesn't need to re-upload to generate audio.
- **`/convert_audio` route:** pulls the extracted text back out of the session, cleans up whitespace with `" ".join(text.split())`, and passes it to `gTTS` to synthesize speech, saving the result as `output.mp3` inside `uploads/`.
- **`/audio/<filename>` route:** serves the generated MP3 back to the browser via `send_file()` with the correct `audio/mpeg` mimetype, so it can be streamed directly in an HTML `<audio>` player instead of forcing a download.
- **User feedback:** `flash()` messages confirm successful upload, successful audio conversion, or warn the user when no text is available to convert.

## 🐛 Notes on the current code

- **Hardcoded secret key:** `app.config['SECRET_KEY']` is set to a placeholder string — fine for local development, but should be pulled from an environment variable before any real deployment since Flask uses this key to sign session cookies.
- **No file-type or size validation:** the upload route trusts that `request.files['filename']` is a valid PDF; a non-PDF upload would cause `PdfReader` to throw an unhandled exception rather than failing gracefully with a user-facing error message.
- **Single shared `output.mp3`:** every conversion overwrites the same `output.mp3` file for every user, since the filename isn't tied to a session ID or upload — fine for a single-user demo, but would cause collisions with multiple concurrent users.
- **Duplicate imports:** `redirect` and `url_for` are each imported twice in the same `from flask import ...` line — harmless, but a small cleanup opportunity.

## 🧠 Concepts Practiced

- Building a Flask web app with combined `GET`/`POST` routes
- Handling file uploads and saving them to a server-side folder
- Extracting text content from PDFs with `PyPDF2`
- Using Flask `session` to persist state across multiple requests
- Converting text to speech with `gTTS` and saving audio output
- Serving generated files back to the browser with `send_file()`
- Giving user feedback with Flask's `flash()` messaging system

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
