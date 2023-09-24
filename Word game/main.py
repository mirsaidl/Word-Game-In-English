import nltk
nltk.download('words')
from nltk.corpus import words


import random as r


# Get a list of English words
english_words = words.words()


random_word = r.choice(english_words).lower()
length = len(random_word)
print(f"I thought {length} letter word. Can you find it?")



space = '-' * length
print(space)
space = list(space)


random_list = list(random_word)
letter_entered = []

while True:
    guess = input("Enter letter: ").lower()
    found = False  # To keep track of whether the guessed letter was found
    if guess in letter_entered:
        print("You entered this. Please enter another letter!")
        continue
    
    for index, item in enumerate(random_word):
        if item == guess:
            found = True
            space[index] = item
    
    if not found:
        print(f"The letter '{guess}' is not in the word.")

    joined = ''.join(space)
    print(joined)
    
    letter_entered.append(guess)
    letter = ''.join(letter_entered)
    print(f"Letters you entered: {letter}")

    if joined == random_word:
        print(f'Congratulations! You found the word: {random_word} with {len(letter)} tries ')
        break
    


