# first method

'''import array
arr = array.array('i',[12,15])
print(arr)'''
# second method
from array import *
print("print using for ")


arr = array('i', [22, 78])
for i in range(len(arr)):
    print(arr[i])

#  third method
print("print using while")
j = 0
while j < len(arr):
    print(arr[j])
    j = j + 1
arr.extend([25]) # in extend function we have to pass the value in the form of list
arr.insert(0, 58) # in insert function we have to pass only the value without using the angular bracket
print(arr)
arr.reverse() # the reverse function reverse the array or list and does not returns any value
print(arr)
c = arr.count(58) # the count function count the given value (as the argument).
                   # As how many times the given value is present in the list.it returns an integer value
print(c)
item = arr.itemsize # the 'itemsize' count the number of item available in the list and returns an integer value
print(item)
buffer = arr.buffer_info()
print(buffer) #it returns two arguments as one is the address of the list and another one is the size of the list or array