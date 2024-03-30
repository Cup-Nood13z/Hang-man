import random

words = ["banana", "pineapple", "watermelon", "grape", "orange"]
hangman = [
    '  _____',
    '  |/    |',
    '  |     o',
    '  |    /|\\',
    '  |    / \\',
    ' _|_',
]
def print_hangman(remaining_attempts):
    for line in hangman[:6 - remaining_attempts]:
        print(line)

def print_word_to_guess(guessed_letters):
    print(' '.join(guessed_letters)) 
# join() method takes all items in an iterable and joins them into one string
    
def play(word):
    remaining_attempts = 6
    guessed_letters = ['_' for letter in word]
    
    while True:
        print_word_to_guess(guessed_letters)
        
        letter = input('Enter a letter: ')
        
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_letters[i] = letter
        else:
            remaining_attempts -= 1
            print_hangman(remaining_attempts)
        
        if '_' not in guessed_letters:
            print(f"Congratulations, you guessed the word: {word}")
            break
        elif remaining_attempts == 0:
            print(f"You lost! The word was {word}")
            print_hangman(remaining_attempts)
            break

word = random.choice(words)
play(word)
        

