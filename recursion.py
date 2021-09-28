import sys

print(sys.getrecursionlimit())# this function get the current limit of recursion
sys.setrecursionlimit(100)
print(sys.getrecursionlimit())
count = 0


def msg():
    global count
    print(count, "hello")
    count += 1
    msg()
    ''' 
    this is recursion cuz here msg() function is calling itself in its body
    in python there is a limit for infinite recursion it is 1000
    we can control the limit of recursion by importing the module sys 
    in sys module there is a method which is sys.getrecursionlimit() this function will give us the current 
    limit of recursion.
    
    there is one more function which can set the limit  of recursion which is sys.setrecursionlimit()
    '''

msg()


