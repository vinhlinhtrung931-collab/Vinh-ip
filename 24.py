#The game is played between two players who take turns one after another.
#On each turn, a player can call 1 to 3 numbers.
#The numbers must be consecutive (for example, 5 6 7) skipping numbers leads to disqualification.
#The counting always starts from 1 and continues upward.
#The one who calls 21, loses the game.

#Dùng hàm while.
import random
numbers=[]
computer_guess=" "
list1=[]
def count2():
        last=None
        for a in range(list1[-1]+1,list1[-1]+3):
            print(a,end=' ')
            last=a
        return last
def count3():
        last=None
        for b in range(list1[-1]+1,list1[-1]+4):
            print(b,end=' ')
            
            last=b
        return last
while True:
    d=input("Player guess: ")
    e = [int(x) for x in d.split()]
    numbers.extend(e)
    list1.extend(e)
    if list1[-1]>=21:
          print("Fail")
          break
    c=[count2,count3]
    count= random.choice(c)()
    numbers.append(count)
    list1.append(count)
    if list1[-1] == 21:                  # <-- THÊM đoạn này
        print(f"\nMáy đã đếm tới {list1[-1]} — máy thua, bạn thắng!")
        break

#Ta buộc phải dùng int để máy tính có thể nhận diện
        
    