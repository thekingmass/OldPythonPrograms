'''
 in this program we will learn about arguments
 there are two types of arguments in python
 1) formal argument
 2) actual argument
'''

def add(x, y):  # x and y are called formal argument
    sum = x + y
    print("sum=", sum)

add(5, 8)# 5 and 8 are  called actual argumet

'''
 when we define a function and in the definition of the function we pass arguments, this arguments is called formal arguments
 
 when we call the function and pass the argument at the time of calling  then this arguments is called actual argument.
 
'''

''' 
types of actual arguments 
1. positional argument
2. keyword argument
3. default argument
4. variable length argument
5. keyword variable length argument

'''

# positional argument

'''
when we pass the actual argument in the same order as it is in the formal argument then it is called positional argument 
'''
def person(name, age):
    print("name=", name)
    print("age=", age)

person('pratik', 23)# this is positional argument as we are passing name first and then age as it is in the formal argument


# keyword argument
'''
when we use keyword for passing actual argument then it is called keyword argument
in this argument there is no need to follow the order of the formal argument
'''
def person2(name, age):
    print("name=", name)
    print("age= ", age)

person2(age=23, name='mass')# as we are using keywords so it is keyword argument

# default arguments
'''
we can use default values in formal arguments 
if we do so then it is called default arguments
'''
def person3(name, age=18):
    print("name=", name)
    print("age=", age)

person3(name="mass")# if we will not pass the it will print the default argument

person3(name='mass', age=25)
