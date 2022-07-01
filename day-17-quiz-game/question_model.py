"""this is the question class which will have the attributes 'question text' and the 'question answer' """
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
