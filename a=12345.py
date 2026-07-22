import random
someWords =["apple","oranges","grapes"]

stages = [
'''
  -----
  |   |
      |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
      |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
  |   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|   |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
      |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
---------
''',
'''
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
---------
'''
]

word = random.choice(someWords)
user_greeting=input("What is your name")
print(f"Welcome to hangman game, {user_greeting}")
list_guess=[]
time=len(word)+2
fail=0
while time>0:
    a=input("Guess a letter")
    list_guess+=a
    display=" "
    for char in word:
        if char in list_guess:
            display=display+char+" "
        else: 
            display+="_ "
    print(display)
   
    if len(a)!=1 or not a.isalpha():
        print("Guess again")
        continue
    if a not in word:
      
        time-=1
        print(f"Try again. You have{time}chance left")
        print(stages[6 - time])
        continue
if time==0:
        print("You lose")
        
  

    




