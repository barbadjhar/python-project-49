#!/usr/bin/env python3

import prompt


def round(run_game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")      
    
    print(f'{run_game.DESCRIPTION}')

    for _ in range(3):
        question, correct_answer = run_game.assembling_game()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. " +
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
