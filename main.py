from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

score = 0
questions = []

for element in question_data:
    questions.append(Question(element['question'], element['correct_answer']))

quiz = QuizBrain(questions)

while quiz.still_remains(score):
    if quiz.next_question():
        score += 1
    else:
        print('Sorry, you got it wrong')



