# TODO : asking the questions
# TODO : checking if the answer was correct
# TODO : checking if we're at the end of the quiz


class QuizBrain:

    # constructor i.e attributes which will get initialized upon object creation
    def __init__(self,q_list):

        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self): # this will return a boolean value depending on this we keep our while loop running or to stop
        return self.question_number < len(self.question_list)



    def next_question(self):

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ") # for checking if the input answer is correct we have check_answer()
        self.check_answer(user_answer, current_question.answer)

    # this method will check if the users answers matches with the correct answer
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")






