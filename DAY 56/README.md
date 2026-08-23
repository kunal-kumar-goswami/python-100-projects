<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2056/day56banner.png" alt="Day 56 - Static Files and Templates Banner" width="100%">
</p>

# Day 56 - Rendering HTML/Static Files & Website Templates 🖼️🎨

A personal portfolio/landing page, built as a static HTML/CSS site — practicing how static assets (CSS, images, fonts, favicon) are structured and linked in a real web project, ready to be served through Flask's static/templates convention.

## 🗂️ Project Structure

```
DAY 56/
├── index.html
├── css/
│   └── styles.css
├── images/
│   ├── cloud.png
│   ├── mountain.png
│   ├── chillies.png
│   └── kunal's.png
└── README.md
```

## ⚙️ How It Works

- **Linking static assets:** the page links a local stylesheet (`css/styles.css`), a Google Fonts stylesheet (Merriweather, Montserrat, Sacramento), and a favicon, all via `<link>` tags in the `<head>`.
- **Top section (`top-container`):** a decorative hero area with cloud and mountain images layered behind a title/subtitle introducing "Kunal Goswami."
- **Middle section (`middle-container`):** three stacked blocks —
  - **Profile:** a profile photo, greeting, and short intro line.
  - **Skills:** two `skill-row` blocks (Design & Development, Hot Wings Challenge), each pairing an image with a heading and descriptive paragraph.
  - **Contact:** a heading, message, and a `mailto:` link styled as a call-to-action button.
- **Bottom section (`bottom-container`):** footer links (LinkedIn, Twitter, Website) and a copyright line.

## 🐛 Notes on the current markup

- **Filename with an apostrophe:** `images/kunal's.png` — apostrophes in filenames can cause issues on some servers/URLs (they sometimes need encoding as `%27`), so renaming it to something like `kunal-profile.png` would be safer and more portable.
- **Placeholder skill content:** the "Hot Wings Challenge" skill block currently describes eating hot wings rather than a real skill — likely leftover boilerplate text from the original template that's worth swapping out for a real second skill (e.g. a specific language, framework, or tool).
- **Small typo:** "curiosity to build my own video games ans applications" — "ans" should be "and."
- **Personal email exposed:** `mailto:ilove@hotwings.com` looks like placeholder/template text too — worth replacing with your real contact email if this page is meant to be live.

## 🧠 Concepts Practiced

- Structuring a multi-section static HTML page
- Linking external stylesheets, custom fonts, and a favicon
- Organizing project assets into `css/` and `images/` folders
- Building a portfolio-style layout with hero, profile, skills, and contact sections
- Preparing static content in a structure that maps cleanly onto Flask's `static/`/`templates/` folders

## 🚀 Run It

Open `index.html` directly in a browser — no server needed for this static page.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
