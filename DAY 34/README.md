<p align="center">
  <img src="https://github.com/kunal-kumar-goswami/python-100-projects/blob/main/DAY%2034/day34banner.png" alt="Day 34 - GUI Quiz App Banner" width="100%">
</p>

# Day 34  — GUI Quiz App 🧠

A trivia quiz app with a `tkinter` GUI, built with a clean OOP structure separating the question data model, quiz logic, and interface into their own modules.

## 🗂️ Project Structure

```
DAY 34/
├── main.py            # Wires everything together and starts the app
├── data.py            # Raw question_data (list of question/answer dicts)
├── question_model.py  # Question class — wraps a single question + answer
├── quiz_brain.py       # QuizBrain class — quiz logic (scoring, next question, etc.)
├── ui.py               # QuizeInterface class — tkinter GUI for the quiz
└── README.md
```

## ⚙️ How It Works

- `data.py` holds the raw trivia question data (question text + correct answer).
- `main.py` loops through `question_data`, wraps each entry in a `Question` object (from `question_model.py`), and builds a `question_bank` list.
- A `QuizBrain` instance is created from the `question_bank`, holding the quiz state — current question number, score, and logic for whether more questions remain.
- A `QuizeInterface` instance takes the `QuizBrain` and builds the `tkinter` GUI — presumably showing each question, True/False (or similar) buttons, and updating the score as the user answers.
- The GUI drives the quiz loop internally (via button clicks calling into `QuizBrain`), which is why the old `while quiz.still_has_questions(): quiz.next_question()` console-loop is commented out — that was the earlier console-only version before the GUI took over.

## 🧠 Concepts Practiced

- Working with structured question data (API-style data, kept locally in `data.py`)
- Object-Oriented Programming across multiple collaborating classes (`Question`, `QuizBrain`, `QuizeInterface`)
- Separating data, logic, and UI into distinct modules
- GUI programming with `tkinter`
- Tracking quiz state (current question index, score)

## 🚀 Run It

```bash
python main.py
```

---

⬅️ [Back to full project index](https://github.com/kunal-kumar-goswami/python-100-projects)
