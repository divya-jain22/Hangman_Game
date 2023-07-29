import random

def choose_word():
    words = ['apple', 'banana', 'cherry', 'orange', 
    'grape', 'melon', 'kiwi', 'pear', 'pineapple',
    'cat', 'dog', 'elephant', 'giraffe', 'lion', 'tiger', 'zebra', 'penguin', 'kangaroo', 'dolphin'
'chair', 'table', 'sofa', 'bed', 'lamp', 'mirror', 'clock', 'rug', 'couch', 'bookshelf', 'dining table', 'cabinet', 'dresser', 'nightstand', 'coffee table', 'TV stand', 'wardrobe', 'fan', 'kitchen sink', 'refrigerator',
 'oven', 'microwave', 'toaster', 'blender', 'kettle',
  'iron', 'vacuum cleaner', 'washing machine', 'dishwasher', 'air conditioner', 
  'broom', 'mop', 'trash can', 'bucket', 'hanger', 'cooking utensils', 'cutlery', 
  'glassware', 'plates', 'pots and pans', 'dish rack'
 'strawberry']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0:
        display = display_word(word, guessed_letters)
        print(display)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)

    if attempts == 0:
        print("Game Over. The word was:", word)

if __name__ == "__main__":
    hangman()
