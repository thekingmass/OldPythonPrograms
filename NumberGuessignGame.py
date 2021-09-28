import random
num = random.randint(20, 50)
count = 0
#print(num)
while count < 5:
    usrnum = int(input("Enter any number between 20 to 50"))
    if num == usrnum:
        print("you guessed correct number")
        print("\t\tHurray !  You won")
        break
    else:
        count = count + 1
        print("Please try Again \t", (5-count), "Attempt left")

if not count < 5:
    print("you loose please try next time")
    print("the correct answer was :", num)
