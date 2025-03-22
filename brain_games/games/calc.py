
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def generate_value(min=1, max=100):
    operand_1 = randint(min, max)
    operand_2 = randint(min, max)
    return operand_1, operand_2


def generate_symbol():
    return choice(['+', '-', '*'])


def calculate_exact(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b 
    elif operator == '*':
        return a * b
    return None


def get_question_and_answer():
    a, b = generate_value()
    operator = generate_symbol()
    question = f'{a} {operator} {b}'

    correct_answer = str(calculate_exact(a, b, operator))

    return question, correct_answer

