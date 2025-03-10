#!/usr/bin/env python3

import prompt
from brain_games.cli import welcome_user
from random import randint, choice
from operator import add, sub, mul


def generating_value(min=1, max=100):
    operand_1 = randint(min, max)
    operand_2 = randint(min, max)
    return operand_1, operand_2


def generating_symbol():
    operation, operator = choice([
        (add, '+'),
        (sub, '-'),
        (mul, '*'),
    ])
    return operation, operator


def calculate_exact(a, b, operator):
    return operator(a, b)


def calculate_value(user):    
    print('What is the result of the expression?')

    for _ in range(3):
        operand_1, operand_2 = generating_value()
        operation, operator = generating_symbol()
        print(f"Question: {operand_1} {operator} {operand_2}")
        
        user_answer = prompt.string('Your answer: ')

        correct_answer = calculate_exact(operand_1, operand_2, operation)

        if user_answer == str(correct_answer):
            print("Correct!")
        else: 
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user}!")
            return
    
    print(f"Congratulations, {user}!")


def main():
    user = welcome_user()                          # Получаем имя пользователя
    calculate_value(user)                 # Используем имя дальше


if __name__ == "__main__":
    main()