import os

from quiz import Quiz
from utils import read_questions


def clear_screen():
    os.system("clear") if os.name == "posix" else os.system("cls")


def make_quiz(question):
    q = question.get("question")
    options = question.get("options")
    ans_index = question.get("answer")
    return Quiz(q, options, ans_index)


def display_quiz(quiz):
    print(quiz.question)
    for index, option in enumerate(quiz.options, 1):
        print(f"{index} - {option}")


def get_user_ans(quiz):
    user_ans = int(input("> "))
    if quiz.check_answer(user_ans):
        print("correct")
        return True
    else:
        print("Incorrect ->", quiz.answer)
        return False

def test_cli():
    score = 0
    questions = read_questions("questions.json")
    total_question = len(questions)
    # make quiz object
    for question in questions:
        clear_screen()
        print("-" * 30)
        print(f"SCORE: {score}/{total_question}".center(30))
        print("-" * 30)
        q = make_quiz(question)
        display_quiz(q)
        # check ans
        score += get_user_ans(q)
        input("Enter to continue ..")
