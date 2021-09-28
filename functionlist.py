number = [2, 8, 36, 45, 78, 13, 19, 74, 48, 17, 43, 69, 94, 91, ]

def findevenodd(list):# we can pass a list in the function as an argument
    evensum=0
    oddsum=0
    for i in list:
        if i%2==0:
            evensum=evensum+i
        else:
            oddsum=oddsum+i
    print("total of even=", evensum)
    print("total of odd=", oddsum)

findevenodd(number)