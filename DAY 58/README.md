<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2058/day58banner%20(1).png" alt="Day 58 - Bootstrap Banner" width="100%">
</p>

# Day 58 - Web Foundations: Bootstrap 🅱️🎨

First steps with the Bootstrap 5 framework — linking the CDN, dropping in a prebuilt component, and using Bootstrap's flexbox utilities to center it — then applying it in two full landing pages: a moving company site and a "Tinder for dogs" concept page.

## 🗂️ Project Structure

```
DAY 58/
├── 1-bootstrap-intro/
│   ├── index.html
│   └── flower.jpg
├── 2-moveit-landing-page/
│   ├── index.html
│   └── (images: box-seam.svg, moving-van.jpg, briefcase.svg, bus-front.svg,
│         chat-square-heart.svg, chevron-right.svg, couple.jpg, dog.jpg, family.jpg)
├── 3-tindog/
│   ├── index.html
│   ├── css/
│   │   └── solution.css
│   └── images/
│       (iphone.png, dog-img.jpg, techcrunch.png, mashable.png, bizinsider.png, tnw.png)
└── README.md
```

---

## 1️⃣ Bootstrap Intro

A minimal exercise introducing the framework:
- Links the Bootstrap 5.3 CSS via CDN.
- Drops in Bootstrap's **prebuilt Card component** (image, title, text, button) unchanged from the docs.
- Uses a small custom flexbox rule (`display: flex; justify-content: center; align-items: center; height: 100vh;`) to center the card both vertically and horizontally on the page — showing how custom CSS layers on top of Bootstrap's own classes.

**Concepts:** Linking Bootstrap via CDN, using prebuilt components as-is, combining Bootstrap with custom flexbox CSS.

---

## 2️⃣ "Move It" Landing Page

A complete, realistic landing page for a fictional moving company, built entirely from Bootstrap components:
- **Responsive navbar** with a brand logo, collapsible menu, a dropdown ("Services"), and a search form.
- **Hero section** with a heading, lead paragraph, two call-to-action buttons, and a hero image.
- **Feature cards ("Why Move With Us?")** — a 3-column responsive grid, each with an icon, heading, description, and "Get a quote" link.
- **Image carousel** cycling through three photos with indicator dots and prev/next controls.
- **Multi-column footer** with brand, copyright, and repeated link sections.

**Concepts:** Bootstrap grid system (`row`/`col`), responsive navbar with `navbar-toggler`, dropdown menus, carousels, utility classes.

---

## 3️⃣ TinDog 🐶💕

A polished, multi-section landing page for a fictional dating app for dogs, layered on top of Bootstrap with a custom `solution.css` stylesheet:
- **Title/hero section** with a gradient background, app screenshot, headline, and Apple/Google Play download buttons (with inline SVG icons).
- **Features section** — a 3-column icon + heading + description grid ("Easy to use", "Elite Clientele", "Guaranteed to work"), using inline Bootstrap Icons SVGs.
- **Testimonial section** with a large pull-quote, a profile photo, and a row of "as featured in" press logos (TechCrunch, Mashable, Business Insider, TNW).
- **Pricing section** — three Bootstrap pricing cards (Chihuahua/Labrador/Mastiff tiers) with feature lists and CTA buttons, the middle/top tier styled with `border-dark`/`text-bg-dark` to stand out.
- **Footer** with brand, copyright, and repeated link sections, wrapped in the same gradient background as the hero.

**Concepts:** Bootstrap pricing card patterns, inline SVG icons, gradient section backgrounds via custom CSS, combining custom and Bootstrap-native styling, structuring a landing page into clear semantic `<section>` blocks.

## 🧠 Concepts Practiced (Overall)

- Including Bootstrap via CDN (CSS + JS bundle)
- Using and customizing prebuilt Bootstrap components
- Bootstrap's responsive grid, cards, and utility classes
- Building complete, multi-section landing pages without writing all CSS from scratch
- Combining Bootstrap with custom CSS (flexbox centering, gradient backgrounds)
- Structuring a page into clear content sections (hero, features, testimonial, pricing, footer)

## 🚀 Run It

Open any `index.html` file directly in a browser — no server needed for these static pages.

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
