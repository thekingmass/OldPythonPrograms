a=5
b=9
#first method
temp=a
a=b
b=temp
#second method
a=a+b   #here a will have 5+9=14
b=a-b   # b=14-9=5
a=a-b    # a=14-5=9
# third method
a,b=b,a  # this method will work only in python
print(a)
print(b)
