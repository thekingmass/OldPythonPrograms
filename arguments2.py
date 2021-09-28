'''
types of actual arguments
1. positional argument
2. keyword argument
3. default argument
4. variable length argument(*)
5. keyword variable length argument

'''


# variable length argument
def add(*a):  # here *a means we can pass many arguments in this function and it will recieve it as a tuple
    s = 0
    for i in a:
        s = s + i
    print("final sum=", s)


add(5, 9, 2, 3, 78, 45)  # this type of argument is called varianble length argument
add(5, 9, 56, 465, 78, 35, 26, 526, 65, 46, 5, 5465, 4, 65, 6)


# keyword variable length argument
def person(name, mob, **etc):  # here **etc means it will accept arguments as key value pair form
    print("Name", name)
    print("mobile", mob)
    #print(etc)
    for i, j in etc.items():
        print(i, j)


person(name='pratik', mob=8707347698, address='gkp', branch='CS', year='2nd')# we can give more argument
                                                      # to this function in the form of key value pair
