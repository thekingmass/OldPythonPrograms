'''name,age = input("enter your name and age").split(",") # The split function help to split between multiple user input
print(name,type(name))
print(age, type(age))'''

''' 
but using this method we can only take input as a string for any other type cast we have to use following way
'''

# Example I want to take input of some subjects from user and in one line
'''
a, b, c, d = [int(i) for i in input("enter marks of four subjects separated with space").split(" ")]
print("a=", a, type(a))
print("b=", b, type(b))
print("c=", c, type(c))
print("d=", a, type(d))
'''
# Taking list and tuple as runtime user input
'''
one important thing at the time of input we need to use the brackets for example if we want to input a list so we have
to use this [] and in this bracket we will put the values separated with commas and for tuple  this {} 
'''

l1 = eval(input("enter the list elements"))
print(l1, type(l1))
t = eval(input("enter the elements of tuple"))
print(t, type(t))