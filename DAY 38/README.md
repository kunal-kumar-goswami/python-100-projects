<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2038/day38banner.png" alt="Day 38 - Workout Tracker Banner" width="100%">
</p>

# Day 38 - Workout Tracker 🏋️📋

A script that takes a natural-language description of a workout, uses the Nutritionix API to parse it into structured exercise data (duration, calories burned), and logs each exercise as a new row in a Google Sheet via the Sheety API.

## 🗂️ Project Structure

```
DAY 38/
└── main.py
```

## ⚙️ How It Works

- **Natural language input:** Prompts the user to describe their workout in plain English (e.g. "ran 5km, then did 20 pushups").
- **Parsing with Nutritionix:** Sends the text, along with personal stats (gender, weight, height, age), to the Nutritionix `natural/exercise` endpoint, which returns a structured breakdown of each recognized exercise — name, duration, and calories burned.
- **Logging to Google Sheets:** For each parsed exercise, builds a row with today's date, current time, exercise name (title-cased), duration, and calories, then `POST`s it to a Sheety-backed Google Sheet using **Basic Authentication** (`auth=("kunal", "...")`).
- Each exercise from the response is logged as its own separate row.

## 🧠 Concepts Practiced

- Parsing natural language into structured data via a third-party NLP-powered API
- Chaining two APIs together (Nutritionix → Sheety) in one workflow
- HTTP Basic Authentication with `requests`
- Working with dates/times (`datetime.now().strftime()`)
- String formatting (`.title()` for consistent capitalization)
- Looping over API response data to create multiple records

## 🔐 Security Note

`APP_ID`, `API_KEY`, and the Sheety Basic Auth credentials are currently hardcoded in `main.py`. Since real values were shared in this conversation, it's worth rotating the Nutritionix API key and changing the Sheety account password, then moving all of these to environment variables (e.g. via `python-dotenv`) before pushing to a public repo.

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
