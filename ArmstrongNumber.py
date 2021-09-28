num = int(input("Enter The number to check weather it is armstrong or not"))
arm = num
sum = 0
result = 0
while arm > 0:
    result = arm % 10
    sum += result ** 3
    arm  = arm // 10

if num == sum:
    print("This is an armstrong number ")

else:
    print("This is not an armstrong number")
