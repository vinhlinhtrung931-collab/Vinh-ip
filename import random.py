import random
num=random.randint(1,100)



b=0
num1=int(input("Guess a number "))
while num1!=num:
    num1=int(input("Guess a number "))
    b=b+1
    if num1 >num:
        print("High")
    elif num1<num:
        print("Low")
    else: 
        print("Correct")
print(b)
   

