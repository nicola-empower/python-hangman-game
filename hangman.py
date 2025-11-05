import random

# List of words for the game
WORD_LIST = ['python', 'github', 'coding', 'terminal', 'developer', 'algorithm']
MAX_ATTEMPTS = 6

def select_word(word_list):
    """Randomly selects a word from the list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Returns the word with unguessed letters replaced by underscores."""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def hangman():
    word = select_word(WORD_LIST)
    guessed_letters = set()
    attempts_left = MAX_ATTEMPTS
    
    print("\n--- Welcome to Hangman! ---")
    print(f"You have {MAX_ATTEMPTS} attempts to guess the word.")

    while attempts_left > 0:
        # Display current game state
        current_display = display_word(word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Guessed letters: {sorted(list(guessed_letters))}")
        print(f"Attempts left: {attempts_left}")

        # Check for win condition
        if "_" not in current_display:
            print(f"\n--- Congratulations! You guessed the word: {word} ---")
            break

        # Get and validate user input
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add guess to the set
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct!")
        else:
            attempts_left -= 1
            print(f"Incorrect. That letter is not in the word.")
            
    # Check for loss condition
    else:
        print("\n--- Game Over! You ran out of attempts. ---")
        print(f"The word was: {word}")

if __name__ == "__main__":
    hangman()
