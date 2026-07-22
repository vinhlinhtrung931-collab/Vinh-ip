import random

b=["rock","paper","scissor"]
c=random.choice(b)
print(c)
while True:
    a=input("What is your choice ").lower()
    
    if a=="rock" and c=="paper":
        print("you lose")   
        break
    if a=="rock" and c=="scissor":
        print("You win")
        break
    if a=="paper" and c=="rock":
        print("You win")
        break
    if  a=="paper" and c=="scissor":
        print("You lose")
        break
    if  a=="scissor" and c=="rock":
        print("You lose")
        break
    if  a=="scissor" and c=="paper":
        print("You win")
        break
    if  a==c:
        print("Again")
        continue
