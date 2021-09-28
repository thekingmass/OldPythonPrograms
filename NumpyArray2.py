from numpy import *

arr = array([5, 8, 7, 6, 3, 2])
print(arr)

arr2 = array([12, 18, 22, 28, 65, 51])
print(arr2)

print(arr+5) # we can directly add(subtract, multiply etc) something to the elements of array
# this will add 5 in each element of the array arr
arr3 = arr + arr2
print(arr3)
# we can directly add or subtract two different arrays but in this case the size of array should be same

print(sin(arr)) # we can also use mathematical formulas to the array directly cuz the numpy module import math module internaly
# for example print(cos(arr2))   or   tan(arr3)  and so on


'''
we can also find the minimum and maximum  for any array
'''

print("maximum in the array arr2 is", max(arr2))

print("minimum in the array arr2 is", min(arr2))

print(pow(arr, 2))

'''
we can use all of the formula that is present in the math module after importing numpy module because the numpy
module internally import the math module
'''