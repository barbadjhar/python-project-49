
from random import randint

DESCRIPTION = 'What number is missing in the progression?'
LENGHT_MAX = 10             # длина прогресси большая 
LENGHT_MIN = 5             # длина прогресси малая 
ROUND_START, ROUND_END = 1, 100
STEP_START, STEP_END = 1, 20


def generation_progression(start, step, length=10):          
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression
    

def get_question_and_answer():
    length = randint(LENGHT_MIN, LENGHT_MAX)      
    start = randint(ROUND_START, ROUND_END)                         
    step = randint(STEP_START, STEP_END)                    
    
    correct_progress = generation_progression(start, step, length)  

    shadow = randint(0, len(correct_progress) - 1)                        

    shadow_progress = [*correct_progress]               
    shadow_progress[shadow] = '..'                     
    shadow_progress = ' '.join(map(str, shadow_progress))

    question = f'{shadow_progress}'
    correct_answer = str(correct_progress[shadow])   
    return question, correct_answer

