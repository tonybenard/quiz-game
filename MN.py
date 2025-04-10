from data import question_data
from M import Question
from q_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("Weldone! you've completed the quiz")
print(f"Final score: {quiz.score}/{quiz.question_number}")