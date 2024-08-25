import tkinter as tk
from tkinter import ttk

from quiz import Quiz
from utils import read_questions


class MainFrame(ttk.Frame):
    question_index = 0

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.questions = read_questions("questions.json")
        self.question_var = tk.StringVar()
        self.answer_var = tk.IntVar()
        self.options_var = []

        q0 = self.questions[MainFrame.question_index]
        self.question_var.set(q0["question"])
        ttk.Label(self, textvariable=self.question_var).pack(anchor="w")
        options = q0.get("options")
        for option in options:
            opt_var = tk.BooleanVar()
            self.options_var.append(opt_var)
            ttk.Checkbutton(self, text=option, variable=opt_var).pack(anchor="w")
        

        next_button = ttk.Button(self, text="Next")
        next_button.pack()
        next_button.config(command=self.next_question)


    def make_question(self, question):
        question = self.questions[MainFrame.question_index]
        question_text = question.get("question")
        options = question.get("options")
        answer_index = question.get("answer")
        q_obj = Quiz(question_text, options, answer_index)
        return q_obj

    def next_question(self):
        question = self.questions[MainFrame.question_index]
        q = self.make_question(question)
        ttk.Label(self,  text=q.question).pack()

        MainFrame.question_index += 1


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("400x400")
        mainframe = MainFrame(self, padding=(20, 20))
        mainframe.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = App()
    app.mainloop()
