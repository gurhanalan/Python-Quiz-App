from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question = "Question Comes Here"
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            fill=THEME_COLOR,
            text=f"{self.question}",
            font=("Ariel", 20, "italic")
        )

        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.false_answer, bd=0)
        self.false_button.grid(row=2, column=0)

        check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_image, highlightthickness=0, command=self.true_answer, bd=0)
        self.true_button.grid(row=2, column=1)

        self.score_label = Label(fg="white", bg=THEME_COLOR, text=f"Score: {self.quiz.score}")
        self.score_label.grid(row=0, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)



    def false_answer(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
