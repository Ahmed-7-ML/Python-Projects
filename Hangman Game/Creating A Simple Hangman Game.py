# The user enter a letter each time to predict the whole letters og the word
# The computer has a password, and you are trying to guess its letters letter by letter before you run out of attempts.

import random

try:
    # Open the Text File (which includes many words)
    # with..clause : automatically closes the file after end.
    with open("wordlist.txt", 'r') as file:
        # Read the content of file into List
        words = file.readlines()

    # The Word to Guess (Randomly Selected from the File)
    # Select all word letters except the final letter, as each word in the list 'words' ended with '\n'
    # Ex: Selected Letter = "Linux\n" -> [:-1] would become 'Linux'
    word = random.choice(words).strip() # or slicing [:-1]
except FileNotFoundError:
    print("Error: File not found!")
    words = []
    word = "Learning" # Default word

# print(words)
# print(word)

# Allowed number of attempts
allowed_errors = 7

# List of Letters the user enters
# The current code treats the space between `Machine` and `Learning` as a character to be guessed,
# so it will appear as an underscore (_) at the beginning. 
# You can manually add the space to the list of guesses at the beginning to avoid this
guesses = [" "] 

# Status Flag -> We use it to find out if the game is over or not.
done = False

while not done:
    # Iterate through the letters in a word
    for letter in word:
        # Check if the letter Like what the user enters ?
        # Initially -> It is all underscores(_) to show the user the length of the word.
        if letter.lower() in guesses:
            print(letter, end = " ")
        else:
            print("_", end=" ")

    print("") # New Line

    guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ").lower()
    # Check if the user enters only 1 Letter and it is Alphabetic character.
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Invalid input! Please enter a single letter (a-z).")
        continue
    
    # Check if the Guessed Letter was entered before (Repeated).
    if guess in guesses:
        print(f"⚠️ You already guessed '{guess}'. Try a different letter!")
        continue
    # Add only the Guessed Letter which is 1 not-repeated Alphabetic Letter 
    guesses.append(guess)

    # In Wrong Guessing
    if guess not in word.lower():
        # Decrease the Number of attempts
        allowed_errors -= 1
        # If it reaches Zero -> Get out from the Loop
        if allowed_errors == 0:
            break

    # Determine the Flag Status
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"🎉You made it! It was '{word}'")
else:
    print(f"💀Game over! It was '{word}'")

# print(guesses)


# To convert it into .exe file (Executable)
# 1. Install Library -> pip install pyinstaller
# 2. Go to Code Folder and Write -> pyinstaller --onefile your_script_name.py
# 3. 'dist' folder will be created -> you will found your .exe file inside it 
