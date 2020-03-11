#GAME

from data import *
from functions import *

game_username = ask_username()
game_scores = get_scores()

if game_username not in game_scores.keys():
    game_scores[game_username] = 0

continue_game = True
    
while continue_game == True:
    
    print("Player {0}: {1} points\n".format(game_username,game_scores[game_username]))

    chances_left = chances
    letters_found = []
    word_to_find = choose_word()
    word_found = get_hidden_word(word_to_find,letters_found)

    while chances_left > 0 and word_found != word_to_find:
        
        print("Word to find: {0} ({1} chances)".format(word_found,chances_left))
        tried_letter = ask_letter().lower()
        if tried_letter in word_to_find:
            letters_found.append(tried_letter)
            word_found = get_hidden_word(word_to_find,letters_found)
            print("Good guess!\n")
        else:
            print("Try again!\n")
        chances_left-=1

    if chances_left == 0 and word_found != word_to_find:
        print("You lost! The word was: ",word_to_find)
    elif word_found == word_to_find:
        print("You won!")
    
    game_scores[game_username] += chances_left
    print("You won {0} points. Your new score is: {1}".format(chances_left,game_scores[game_username]))

    play_choice = input("Would you like to play again? (yes/no)")

    if play_choice == "yes":
        print("Let's guess a new word!")
    elif play_choice == "no":
        save_scores(game_scores)
        print("Hope you had fun. See you very soon!")
        continue_game = False
