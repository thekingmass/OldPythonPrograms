

games = {}
num = int(input("enter the number of participants "))

for i in range(num):
    name = input("enter the name")
    win = int(input("enter number of wins"))
    games[name] = win

print(type(games))
print(games)