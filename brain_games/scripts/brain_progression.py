#!/usr/bin/env python3

from random import randint

import prompt

from brain_games.cli import welcome_user

DESCRIPTION = 'What number is missing in the progression?'
LENGHT_MAX = 10             # длина прогресси большая 
LENGHT_MIN = 5             # длина прогресси малая 


def generation_progression(start, step, length=10):          
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression
    

def calculate_value(user):    
    print(f'{DESCRIPTION}')                     

    for _ in range(3):

        length = randint(LENGHT_MIN, LENGHT_MAX)      
        start = randint(1, 100)                         
        step = randint(1, 20)                    
        
        correct_progress = generation_progression(start, step, length)  

        shadow = randint(0, len(correct_progress) - 1)                        

        shadow_progress = [*correct_progress]               
        shadow_progress[shadow] = '..'                     
        shadow_progress = ' '.join(map(str, shadow_progress))
        correct_answer = correct_progress[shadow]           

        print(f"Question: {shadow_progress}")
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print("Correct!")
        else: 
            print(f"'{user_answer}' is wrong answer ;(." +
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            return
    
    print(f"Congratulations, {user}!")


def main():
    user = welcome_user()                    # Получаем имя пользователя
    calculate_value(user)                    # Используем имя дальше


if __name__ == "__main__":
    main()