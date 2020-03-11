#FUNCTIONS

import os
import pickle
import random
from data import *

def ask_username():
    """Returns username."""
    username = input("Please enter your name:").capitalize()
    return username

def get_scores():
    """Returns scores."""
    if os.path.exists(scores_file_name):
        with open(scores_file_name,"rb") as file:
            scores = pickle.Unpickler(file).load()
    else:
        scores = {}
    return scores
        
def save_scores(scores):
    """Saves scores."""
    with open(scores_file_name,"wb") as file:
        pickle.Pickler(file).dump(scores)
    
def choose_word():
    """Returns a word randomly selected by the computer."""
    return random.choice(words)

def ask_letter():
    """Returns a letter choosen by the user."""
    check = False
    while check == False:
        letter = input("Which letter would you like to try?")
        if not letter.isalpha() or len(letter) > 1:
            print("You did not enter a valid letter.")
        else:
            check == True
            return letter     

def get_hidden_word(word,validated_letters):
    """Returns word with stars on unknown letters."""
    hidden_word = "".join([elt if elt in validated_letters else "*" for elt in word])
    return hidden_word
