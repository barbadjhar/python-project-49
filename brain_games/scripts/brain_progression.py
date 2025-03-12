#!/usr/bin/env python3

from random import randint

import prompt

from brain_games.cli import welcome_user

LENGHT_MAX = 10             # длина прогресси большая 
LENGHT_MIN = 5             # длина прогресси малая 


def generation_progression(start, step, length=10):          
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression
    

def calculate_value(user):    
    print('What number is missing in the progression?')                     

    for _ in range(3):

        length = randint(LENGHT_MIN, LENGHT_MAX)      # длина прогресии
        start = randint(1, 100)                         # число для старта
        step = randint(1, 20)                           # шаг прогресии
        shadow = randint(0, length)                        # выбор блок за точками
        
        correct_progress = generation_progression(start, step, length)  # список арифмитической прогресси 

        shadow_progress = [*correct_progress]               # создаем новый список из элиментов correct_progress
        shadow_progress[shadow] = '..'                      # заменям выборочно index на двоеточие
        correct_answer = correct_progress[shadow]           # значение скрытого index 

        print(f"Question: {shadow_progress}")
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print("Correct!")
        else: 
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            return
    
    print(f"Congratulations, {user}!")


def main():
    user = welcome_user()                    # Получаем имя пользователя
    calculate_value(user)                    # Используем имя дальше


if __name__ == "__main__":
    main()