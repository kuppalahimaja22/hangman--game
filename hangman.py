import random

# 1. Predefined list of 5 words
word_bank = ["python", "coding", "program", "matrix", "galaxy"]

# Pick a random word from the list
secret_word = random.choice(word_bank)

# Create a list of underscores to represent the hidden letters
guessed_word = ["_"] * len(secret_word)

# Track game state
incorrect_guesses_left = 6
guessed_letters = []  # To keep track of letters the player already tried

print("--- Welcome to Text-Based Hangman! ---")

# 2. Main game loop (While loop)
while incorrect_guesses_left > 0 and "_" in guessed_word:
    print(f"\nWord to guess: {' '.join(guessed_word)}")
    print(f"Guesses remaining: {incorrect_guesses_left}")
    print(f"Letters guessed so far: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    
    # Take basic console input
    guess = input("Guess a letter: ").lower().strip()
    
    # Input validation: Ensure it's a single alphabetical character
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue
        
    # Check if the letter was already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue
        
    # Add the guess to our tracker
    guessed_letters.append(guess)
    
    # 3. Decision making (If-Else)
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
        # Reveal the correctly guessed letter in our list
        for index, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        incorrect_guesses_left -= 1

# 4. Game Over evaluation
print("\n--- Game Over ---")
if "_" not in guessed_word:
    print(f"Congratulations! You won! The word was: {secret_word}")
else:
    print(f"You ran out of guesses! The secret word was: {secret_word}")