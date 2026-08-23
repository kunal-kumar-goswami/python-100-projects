<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2045/bs4-start/day45banner.png" alt="Day 45 - Web Scraping with BeautifulSoup Banner" width="100%">
</p>

# Day 45 - Web Scraping with Beautiful Soup 🍲🕸️

## 🗂️ Project Structure

```
DAY 45/
└── main.py
└── website.html
```

## ⚙️ How It Works

- **Fetching the page:** `requests.get()` pulls the raw HTML from `news.ycombinator.com`, and `BeautifulSoup` parses it with the `html.parser` engine.
- **Extracting titles & links:** Finds all `<span class="storylink">` tags, pulling out each article's text and its `href` link into two parallel lists.
- **Extracting upvotes:** Finds all `<span class="score">` tags and parses out the numeric vote count from each (e.g. `"142 points"` → `142`).
- **Finding the top article:** Uses `max()` to find the highest upvote count, then `.index()` to find its position, and uses that same index to look up the matching title and link from the earlier lists.
- Prints just the title and link of the most-upvoted article.

## 🧠 Concepts Practiced

- HTTP requests with `requests`
- HTML parsing with `BeautifulSoup` (`find_all`, `getText()`, `.get()`)
- Extracting and cleaning numeric data from text
- Finding a maximum value and its corresponding index across parallel lists

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
