class Quiz:
    def __init__(self, question: str, options: list[str], answer_index: int):
        self.question = question
        self.options = options
        self.answer_index= answer_index
        self.answer = self.options[self.answer_index]

    def check_answer(self, user_ans_index: int) -> bool:
        return (user_ans_index - 1) == self.answer_index


