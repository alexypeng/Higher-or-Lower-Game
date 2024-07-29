# This program is a simple Higher or Lower game that pulls data from a pre-existing list
# of people/things. It makes use of user input, dictionaries, and functions. 
# Programmed by Alexander Peng on 2024/07/28

import random

from replit import clear

from art import logo, vs
from game_data import data


def get_item_B(item_A):
    """Chooses an item for B"""
    item = random.choice(data)
    while item_A == item: # Ensures that items A and B are not the same
        item = random.choice(data)
    return item

def format(item):
    """Formats the data of the dictionary object taken and returns it as a string."""
    name = item['name']
    description = item['description']
    country = item['country']
    return f"{name}, a {description}, from {country}."

def check(guess, first, second):
    """Checks if the user's guess is correct."""
    guess = guess.lower()
    if first['follower_count'] > second['follower_count']:
        return guess == 'a'
    return guess == 'b'

def game():
    """Function that runs the Higher or Lower game"""
    lose = False
    first_turn = True
    item_B = ""
    score = 0
    
    while not lose:
        
        item_A = random.choice(data) if first_turn else item_B
        item_B = get_item_B(item_A)

        print(logo)
        
        print(f"Compare A: {format(item_A)}")
        print(vs)
        print(f"Compare B: {format(item_B)}")

        guess = input("Who has more followers? Type 'A' or 'B': ")

        clear()
        print(logo)
        
        if check(guess, item_A, item_B):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            lose = True

game()