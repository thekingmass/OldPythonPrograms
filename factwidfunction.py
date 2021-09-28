num = int(input("Enter any number to check its factorial"))

# first method using for loop and with function call
'''def factorial(p):
    facto = 1
    for i in range(1, num + 1):
        facto = facto * i
    return facto'''


# third method using while loop and using function call

def factorial1(p):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    return fact


# third method using while loop and using function call

'''def factorial2(p):
    fact = 1
    i = 1
    while i != p + 1:
        fact = fact * i
        i += 1
    return fact'''

fact = factorial1(num)
print("the factorial of ", num, "is ", fact)
