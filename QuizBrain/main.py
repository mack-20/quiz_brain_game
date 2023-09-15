from question import Question
from data import film_data, general_data, animals_data
from quiz_brain import QuizBrain
import random


#A list to hold the questions available from the data module
question_bank = []

#Question data to use must be selected by user based on his/her prefernces
category = {'f':film_data, 'g':general_data, 'a':animals_data, 'r':random.choice([film_data,general_data,animals_data])}
user_choice = input("""
Pick a category(Press corresponding letter to choose):
* G - General Knowledge(20 questions)
* F - Entertainment: Film(10 questions)
* A - Science: Animals(10 questions)
* R - Random
""").lower()

question_data = category[user_choice]




#Forms question_objects out of the question_data 
for question_datum in question_data:
    new_question = Question(question_datum['question'],question_datum['correct_answer'])
    question_bank.append(new_question)
#Starts the Game    
Game = QuizBrain(question_list=question_bank)

while Game.still_has_questions():
    Game.ask_next_question()