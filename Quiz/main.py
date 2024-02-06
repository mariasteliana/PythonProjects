from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for entry in question_data:
    question_text = entry["question"]
    question_answer = entry["correct_answer"]
    Question_n = Question(question_text,question_answer)
    question_bank.append(Question_n)


quiz = QuizzBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completes the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")