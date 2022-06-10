#!/usr/bin/env python


from brain_games.games import logic
from random import randint, choice

MIN_NUMBER = 1
MAX_NUMBER = 50

PROGRESSION_LEN = 10
BEGIN_STRING = 'What number is missing in the progression?'


def start():
    user_name = logic.welcome_user()
    print(BEGIN_STRING)
    for i in range(3):
        number1 = randint(MIN_NUMBER, MAX_NUMBER)
        step = randint(1, 10)
        progression_len = randint(5, 10)
        max_num = number1 + (step * progression_len)
        progression = range(number1, max_num, step)
        correct_answer = choice(progression)

        text_question = ' '.join([
            '..' if num == correct_answer else str(num) for num in progression
        ])

        if not logic.game_step(text_question, str(correct_answer)):
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!!!')
