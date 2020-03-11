## Hangman Game

*This game is the very first code that I made, as part of OpenClassrooms "Learn How to Code in Python" course.*

This short program offers you to play the well-known **Hangman Game** against your computer. It is **more suitable for French speakers**, as the list of words to guess is exclusively in French (my apologies!).

At the beginning of each game, you will be asked to **enter your username**, so that the program can retrieve your previous score (if any) and store the new one under a `scores` binary file, as a dictionary object `{"username":score}`.

A word will be **randomly selected from the list,** and you will have **a maximum of 15 attempts** to guess it. Your new score will be calculated from your previous score, to which will be added **the number of attempts remaining when you guessed the word**.

*Besides the overall game logic, the most interesting part of this project for me was certainly to learn how to use the Pickle module to save Python objects (here, the scores dictionary).*

The project is composed of **three Python files**, the last one being executable:

 - `data.py`: contains the list of words, the number of max. attempts, and the name of the scores file
 - `functions.py`: contains the functions used in the `game.py` file
 - `game.py`: core program of the game, to be executed