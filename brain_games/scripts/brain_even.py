#!/usr/bin/env python3

from random import randint
import prompt
from brain_games.cli import welcome_user


def check_parity(number):
    return "yes" if number % 2 == 0 else "no"


def invitation_to_comparison(user):
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    print(f"{user}")

    for _ in range(3):
        number = randint(0, 99)
        print(f"Question: {number}")

        user_answer = prompt.string('Your answer: ')
        correct_answer = check_parity(number)

        if user_answer == correct_answer:
            print("Correct!")
        else: 
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            return
    
    print(f"Congratulations, {user}!")


def main():
    user = welcome_user()                          # Получаем имя пользователя
    invitation_to_comparison(user)                 # Используем имя дальше


if __name__ == "__main__":
    main()