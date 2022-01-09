class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_remains(self, score):
        print(f'Your score is {score}')
        if self.question_number >= len(self.question_list):
            print('You ran out of questions!')
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]

        self.question_number += 1

        current_answer = input(f'Q.{self.question_number}{current_question.text} (True/False)')

        print(f'The correct answer was {current_question.answer}')

        if current_answer == current_question.answer:
            return True
        else:
            return False
