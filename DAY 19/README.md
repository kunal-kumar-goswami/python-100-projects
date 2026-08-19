<p align="center"> <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2019/day19-banner.png" alt="Day 19 — Turtle Race banner" width="100%" /> </p>

# Day 19 — 🏁 Turtle Race

> Part of my [100 Days of Python](https://github.com/kunal-kumar-goswami/python-100-projects) journey — Angela Yu's Python Pro Bootcamp

A betting-style race game where six colored turtles race to the finish line at random speeds, and the player wins or loses based on which color they bet on beforehand.

## 💡 What it does

The program asks the player to type the color of the turtle they think will win, lines up six turtles (one per color) at the starting line, then moves each one forward by a random distance every frame until one crosses the finish line. It then announces whether the player's bet was correct.

**Example:**
```
Make your bet
Which turtle will win the race? Enter a color: blue

You've won! The blue turtle is the winner!
```

## 🎯 Concepts Practiced

- `screen.textinput()` for a popup text input dialog
- Creating multiple `Turtle` objects in a loop and storing them in a list
- `random.randint()` to give each turtle an independently randomized speed each frame
- `turtle.xcor()` to detect when a turtle crosses the finish line
- A `while` loop driven by a boolean flag (`race_on`) to control the race duration

## 🔑 Key Takeaways

- Storing each turtle in a list (`all_turtles`) makes it possible to move and check every racer with a single loop, instead of writing separate code per turtle
- Giving each turtle a random forward distance every frame (rather than a fixed speed) is what makes the race outcome genuinely unpredictable
- Checking `turtle.xcor() > 230` inside the race loop is a simple, effective way to detect a finish line without needing collision detection
- Only starting the race if `your_bet` is not empty prevents the race from running (and looking broken) if the player closes the input dialog without typing anything

## 🛠️ Tech Stack

`Python 3` · `turtle` module · `random` module

## 🏃 How to Run

```bash
git clone https://github.com/kunal-kumar-goswami/python-100-projects.git
cd 100-days-of-python/day19/project
python main.py
```

No external libraries required.
## 🎥 Project Demo

(https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2019/Video%20Project.mp4)

---

⬅️ · [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
