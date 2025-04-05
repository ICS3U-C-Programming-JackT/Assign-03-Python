#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: April 3, 2025

# Hangman Program in python V2

import random

import constants
import icons
import words

# Core variables
word = "hangman"
current_lives = constants.STARTING_LIVES
available_words = words.word_list
game_ongoing = True

# Function to display current hangman icon
def display_hangman(lives):
    current_icon_hm = icons.hangman[lives]

    # Print out each line of the hangman icons
    for line in current_icon_hm:
        print(line)


# Function to chose a word and to set up guessed and current word arrays
def choose_word():
    random_choice = random.randrange(1, len(available_words))
    return available_words[random_choice]


def setup_arrays(word):
    current_word = []
    guessed_word = []
    for i in range(len(word)):
        current_word.append(word[i])
        guessed_word.append("_")
    return current_word, guessed_word


# Check if the word has been guessed
def check_valid(guessed_word, current_word):
    if guessed_word == current_word:
        return True
    else:
        return False


# Main function, commanding the rest of the functions
def main():
    guessed_word = []  # Starts out with only underscores
    guessed_characters = []  # Array so no repeated guessed occur
    current_word = []  # Starts out solved

    # Print out starting message, initiate program
    print(constants.STARTING_MESSAGE)

    # Set random word
    word = choose_word()
    current_lives = constants.STARTING_LIVES

    # For testing purposes
    if constants.OVERRIDE_WORD == True:
        word = "hangman"

    new_cw, new_gw = setup_arrays(word)  # Create arrays for word data
    current_word = new_cw
    guessed_word = new_gw

    while game_ongoing:

        # Displays guessed letters
        print("Guessed letters: ")
        print(guessed_characters)

        # Displays guessed word
        print("Word: ")
        print(guessed_word)

        # Displays hangman
        print("Hangman: ")
        display_hangman(current_lives)
        user_guess = input("Guess a single letter a-z: ")
        isalpha = user_guess.isalpha()  # Is alpha checks if string is a letter

        # If user entered proper character
        if isalpha == True and len(user_guess) == 1:

            # Make new letter lowercase
            new_letter = user_guess.lower()

            # Check if letter has already been guessed
            letter_been_guessed = False
            for char in guessed_characters:
                if char == new_letter:
                    letter_been_guessed = True

            if letter_been_guessed:
                print("You already guessed this letter!")

            guessed_characters.append(new_letter)
            guess_valid = False

            for i in range(len(current_word)):
                if current_word[i] == new_letter:
                    guess_valid = True
                    guessed_word[i] = new_letter

            if guess_valid:
                print("Nice! this word contains the character", new_letter)
            elif letter_been_guessed == False:
                print("Aw, that letter isn't in that word!")
                current_lives -= 1
        else:
            print("You didn't enter a proper character! You entered '", user_guess, "'")

        # If the user has guessed the word
        valid = check_valid(guessed_word, current_word)
        if valid:
            print("You guessed the word! The word was ", guessed_word)
            break

        # If the user has run out of lives
        if current_lives == 0:
            display_hangman(current_lives)
            print("You lost all of your lives!")
            print("The word was ", current_word)
            break

    # Ask user if they want to restart
    restart = input("Restart? (yes/no):")
    if restart == "yes":
        main()


# Fire main, initiate program
if __name__ == "__main__":
    main()
