""" the quiz brain will perform the following:
    1. check if the quiz still has any more questions for the user (via the 'still_has_questions' method
    2. display the next question for the user
    3. keep track of the question number and the users score
    4. display the correct answer regardless of if the user is right or wrong
"""


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        """starting the numbering of our output from 1. and not 0, which is how python starts its own numbering"""
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
        print(f"The correct_answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")