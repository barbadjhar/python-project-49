#!/usr/bin/env python3

from math import sqrt
from random import randint

import prompt

from brain_games.cli import welcome_user

DESCRITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_simple_number(num):
    if num == 2:
        return "yes"
    if num <= 1 or num % 2 == 0:
        return "no"
    for i in range(3, int(sqrt(num)), 2):
        if num % i == 0:
            return "no"
    return "yes"


def calculate_value(user):    
    print(f'{DESCRITION}')                     

    for _ in range(3):

        number = randint(1, 100)
        correct_answer = check_simple_number(number) 

        print(f"Question: {number}")
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print("Correct!")
        else: 
            print(f"'{user_answer}' is wrong answer ;(. " +
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            return
    
    print(f"Congratulations, {user}!")


def main():
    user = welcome_user()                    # Получаем имя пользователя
    calculate_value(user)                    # Используем имя дальше


if __name__ == "__main__":
    main()