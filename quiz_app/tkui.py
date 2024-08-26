import tkinter as tk
from tkinter import ttk

from quiz import Quiz
from utils import read_questions


class MainFrame(ttk.Frame):
    question_index = 0

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # an option(checkbutton) selected (checked)
        self.option_checked = False
        self.option_checked_index = -1
        # get questions from json file
        self.questions = read_questions("questions.json")

        # Variables
        self.question_var = tk.StringVar()
        self.option_0_var = tk.BooleanVar()
        self.option_1_var = tk.BooleanVar()
        self.option_2_var = tk.BooleanVar()
        self.option_3_var = tk.BooleanVar()
        self.options_var = [
            self.option_0_var,
            self.option_1_var,
            self.option_2_var,
            self.option_3_var,
        ]
        self.ans_index = 0

        self.question_label = ttk.Label(self, textvariable=self.question_var)
        self.option_0 = ttk.Checkbutton(self, variable=self.option_0_var)
        self.option_1 = ttk.Checkbutton(self, variable=self.option_1_var)
        self.option_2 = ttk.Checkbutton(self, variable=self.option_2_var)
        self.option_3 = ttk.Checkbutton(self, variable=self.option_3_var)
        self.option_0.config(command=self.uncheck_other)
        self.option_1.config(command=self.uncheck_other)
        self.option_2.config(command=self.uncheck_other)
        self.option_3.config(command=self.uncheck_other)

        self.message = ttk.Label(self)

        next_button = ttk.Button(self, text="Next")
        next_button.pack(anchor="w", pady=10)
        next_button.config(command=self.next_question)

        check_ans_button = ttk.Button(self, text="Check", command=self.check_ans)
        check_ans_button.pack(anchor="w")

    def make_question(self, question):
        question = self.questions[MainFrame.question_index]
        question_text = question.get("question")
        options = question.get("options")
        answer_index = question.get("answer")
        q_obj = Quiz(question_text, options, answer_index)
        return q_obj

    def uncheck_all(self):
        for var in self.options_var:
            var.set(value=False)

    def next_question(self, index=0):
        q = self.questions[MainFrame.question_index]
        q_text = q.get("question")
        options = q.get("options")
        self.ans_index = int(q.get("answer"))

        self.question_var.set(q_text)
        self.question_label.pack(anchor="w")

        self.option_0.config(text=options[0])
        self.option_1.config(text=options[1])
        self.option_2.config(text=options[2])
        self.option_3.config(text=options[3])
        self.option_0.pack(anchor="w")
        self.option_1.pack(anchor="w")
        self.option_2.pack(anchor="w")
        self.option_3.pack(anchor="w")

        self.uncheck_all()
        self.message.config(text="")
        MainFrame.question_index += 1

    def get_selected_index(self, options):
        if True in options:
            return options.index(True)
        return -1

    def check_ans(self):
        user_ans_index = self.get_selected_index(self.options_var)
        if self.ans_index == user_ans_index:
            self.message.config(text="Correct")
        else:
            self.message.config(text="Incorrect")
        self.message.pack(anchor="w")

    def uncheck_other(self):
        options = [var.get() for var in self.options_var]


        if self.option_checked and self.option_checked_index != -1:
            alredy_checked_option = self.options_var[self.option_checked_index]
            alredy_checked_option.set(value=False)
            options[self.option_checked_index] = False
            self.option_checked_index = self.get_selected_index(options)
        else:
            # store first time checked checkbutton index
            self.option_checked_index = self.get_selected_index(options)
            self.option_checked = True



class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("400x400")
        mainframe = MainFrame(self, padding=(20, 20))
        mainframe.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = App()
    app.mainloop()
