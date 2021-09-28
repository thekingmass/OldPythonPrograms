num = int(input())
# reversed_num = 0
token = 0
def rev(temp):
    revs = 0
    while temp:
        digit = temp % 10
        revs = (revs * 10) + digit
        temp //= 10
    return revs
reversed_num = rev(num)
# print(reversed_num)
while (reversed_num):
    digit = reversed_num % 10
    if digit == 0:
        token = (token * 10) + 1
        continue
    elif digit == 1:
        token = (token * 10)
        continue
    if (digit % 2 == 0):
        token = (token * 10) + digit + 1
    else:
        token = (token * 10) + digit - 1
    reversed_num = reversed_num // 10
print(token)
