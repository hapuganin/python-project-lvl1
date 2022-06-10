#!/usr/bin/env python


from brain_games.games import logic
from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 100
BEGIN_STRING = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_start():
    user_name = logic.welcome_user()
    print(BEGIN_STRING)
    for i in range(3):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        correct_answer = "yes" if number % 2 == 0 else "no"
        if not logic.game_step(number, correct_answer):
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!!!')
