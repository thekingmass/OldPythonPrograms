from math import sqrt
try:
    num = int(input("Enter the number to check weather the number is prime or not"))

    if num == 2:
        print("2 is the only even prime number")
        exit(0)
    rng = int(sqrt(num))
    for i in range(2, rng + 1):
        if num % i ==0:
            print("Not a prime number")
            break
    else:
        print("prime number")

except ValueError:
    print("only enter the number to check prime")