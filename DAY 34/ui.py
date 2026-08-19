from tkinter import *
from quiz_brain import QuizBrain  # Import the QuizBrain class

THEME_COLOR = "#375362"

class QuizeInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 14))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 16, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="/python/100 Days of Code/DAY 34/images/true.png")  
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_image = PhotoImage(file="/python/100 Days of Code/DAY 34/images/false.png")  
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        """Load the next question."""
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question() 
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Handle the event when the true button is pressed."""
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        """Handle the event when the false button is pressed."""
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        """Give feedback after answering."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        
        self.window.after(1000, self.get_next_question)


# Create a QuizBrain object (make sure the class is implemented correctly)
# quiz_brain = QuizBrain(question_list)  # Assuming question_list is provided somewhere
# quiz = QuizeInterface(quiz_brain)  # Initialize the quiz interface

