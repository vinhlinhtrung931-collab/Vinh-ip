import random

# List of words
words = [
    "python",
    "computer",
    "keyboard",
    "programming",
    "banana",
    "elephant",
    "football",
    "mountain"
]

# Choose a random word
word = random.choice(words)

guessed_letters = []


b=10
while b>0:
    display=" "
    for char in word:
        #Gắn char với từng chữ cái có trong word
        if char in guessed_letters:#Nếu char trong các chữ mình đoán
            display=display+char# display từ một string trống thêm chữ cái mình cần
        else:
            display=display+"_ "
    print(display)
    b=b-1
    player=input("Guess")
    guessed_letters+=player


   



