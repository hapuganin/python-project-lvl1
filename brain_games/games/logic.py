#!/usr/bin/env python

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def game_step(question, correct_answer):
    print(f'Question: {str(question)}')
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer;(."
              f" Correct answer was '{correct_answer}'.")
        return False
