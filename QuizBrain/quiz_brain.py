class QuizBrain:
    score = 0
    question_number = 0
    
    def __init__(self,question_list):
        self.question_list = question_list
             
        
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("Questions Complete!")
            return False
        
    def ask_next_question(self):
        """Ask next question and check user's answer of it and score user"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"{current_question.text}(True/False): ").title()
        self.check_answer(user_answer=user_input,correct_answer=current_question.answer)
        
        
    
    
    def check_answer(self,user_answer,correct_answer):
        """Checks user's response and scores user"""
        if user_answer == correct_answer:
            self.score += 1
            print(f"You're right\nScore:{self.score}/{self.question_number}")
        else:
            print(f"You're wrong\nScore: {self.score}/{self.question_number}")