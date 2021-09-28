try:
    num = int(input("enter the number to check its factorial"))
    fact = 1
    for i in range(num, 0, -1):
        # print(fact, "*", i, end=" =")
        print(i, '*', end=' ')
        fact = i * fact
    print("=", fact)
except ValueError:
    print("Enter only number to check the factorial")

