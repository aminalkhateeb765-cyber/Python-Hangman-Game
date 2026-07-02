# Hangman Game (Python)

A classic Hangman game built using Python. The program randomly selects a secret word, and the player tries to guess it letter by letter before running out of lives and getting "hanged".

## Features
* Random Word Selection: Uses the random module to select a word from a predefined list.
* ASCII Art Visuals: Displays the stages of the hangman dynamically after each wrong guess.
* Input Validation: Prevents players from losing lives if they guess the same letter more than once.

## How It Works
1. The game displays empty underscores _ representing the letters of the hidden word.
2. The player inputs a letter.
3. If the guess is correct, the letter appears in its right position.
4. If the guess is wrong, the player loses a life, and a new part of the hangman is drawn.
5. The game ends when the player guesses the entire word (WIN) or runs out of lives (LOSE).

## Core Concepts Covered
* Loops (while and for)
* Conditional Statements (if, elif, else)
* Lists and String manipulation
* Random module integration
