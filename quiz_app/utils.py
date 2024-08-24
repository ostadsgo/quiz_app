import json


def read_questions(filename: str):
    with open(filename) as json_file:
        questions = json.load(json_file)
        return questions
