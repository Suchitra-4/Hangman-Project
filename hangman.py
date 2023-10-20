import random

def choose_word():
    words = ["python", "hangman", "computer", "programming", "game"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()
def hangman_game():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()

    print("Welcome to Hangman!")
    print("",display_word(word_to_guess, guessed_letters))

    while max_attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Guess is correct,Keep going on!!")

        if guess not in word_to_guess:
            max_attempts -= 1
            print("Your Assumption is wrong, try it again!!")

        print("word:",display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word!")
            break

        print(f"Attempts left: {max_attempts}")

    if max_attempts == 0:
        print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")

hangman_game()