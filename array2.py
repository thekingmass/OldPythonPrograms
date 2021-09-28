from array import *
try:
    marks = array('i', [])
    num = int(input("enter the number of students in your class"))
    print("enter the marks of",  num,  "students of your class")
    for i in range(num):
        print("enter the marks of student", i + 1)
        value = int(input())

        marks.append(value)

    for k in marks:
        print(k)

        ''' below  we are performing  the searching operation in the array'''

    search = int(input("enter the value to be searched in the array"))

    # here we will perform searching without using inbuilt function 'index()'

    '''
    pos = 0
    for l in marks:
        if search == l:
            print("the element is found at the position ", pos + 1)
            break
    
        else:
            pos += 1
    
    else:
        print("the element",search ," is not found in the given array")  '''

    # this is the second way of finding the index of the given value in the given array using index function


    found = 0
    found = marks.index(search)
    if found != 0:
        print("the element is found at the position ", found)


except ValueError:
    print("the element", search, " is not found")