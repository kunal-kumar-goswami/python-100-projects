# Day 03 — 🧙 Wizard's Quest (Treasure Island)

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

A branching, choice-based text adventure game built entirely with `if`/`elif`/`else` logic — the player navigates a forest, a river, and three magical doors to try to recover the Orb of Light.

## 💡 What it does

The program prints ASCII art and a story intro, then presents the player with a series of choices. Each answer branches the story down a different path, leading to one of several possible endings — only one of which is a win.

**Example:**
```
Welcome, apprentice wizard!
Your mission is to recover the lost Orb of Light from the Enchanted Forest.

You enter the forest and come to a forked path. Do you go 'left' toward the mist or 'right' into the darker woods?
> left
You walk into the mist and see a river guarded by a sleeping troll.
Do you 'sneak' past him or 'wake' him up to ask for help?
> sneak
You quietly cross and find a glowing cave with 3 magical doors: one silver, one green, and one black.
Which door do you open? Type 'silver', 'green', or 'black'
> green
You find the Orb of Light shining brightly. You Win!
```

## 🎯 Concepts Practiced

- Multi-line strings for ASCII art
- Nested `if`/`elif`/`else` statements for branching story logic
- `input()` chained with `.lower()` to handle case-insensitive answers
- Designing multiple possible outcomes from a sequence of decisions

## 🔑 Key Takeaways

- Nesting conditionals inside each other is what makes a branching story possible — each choice only matters within the branch it belongs to
- `.lower()` on user input avoids bugs caused by a player typing "Left" instead of "left"
- Planning the decision tree (which choices lead to which outcomes) before writing the code makes the nested logic much easier to follow
- An `else` fallback at each decision point ensures unexpected input still leads somewhere, rather than crashing or being silently ignored

## 🛠️ Tech Stack

`Python 3`

---

