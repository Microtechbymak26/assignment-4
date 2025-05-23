import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    word = get_valid_word(words).upper()  # Convert word to uppercase
    print(f"(For testing) The word is: {word}")

    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'\nYou have {lives} lives left. You have used these letters: ', ' '.join(used_letters))

        # Current word display
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        # User input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print('Letter is not in the word. Try again.')
        elif user_letter in used_letters:
            print('You have already used that letter. Try again.')
        else:
            print('Invalid character. Please enter a valid letter.')

    # Game result
    if lives == 0:
        print(f'\nYou died, sorry. The word was: {word}')
    else:
        print(f'\nYou guessed the word: {word}!!')

hangman()
