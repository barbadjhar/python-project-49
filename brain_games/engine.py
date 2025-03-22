#!/usr/bin/env python3

import prompt

from brain_games.cli import welcome_user

ROUNDS = 3


def run_game(games):
    name = welcome_user()

    print(f'{games.DESCRIPTION}')

    for _ in range(ROUNDS):
        question, correct_answer = games.get_question_and_answer()

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. " +
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
