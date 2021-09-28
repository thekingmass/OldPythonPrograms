from numpy import *
'''
there are three ways for copying an array to another using numpy
1. using assignment operator 
2. shallow copy method 
3. deep copy method
'''

''' using normal assignment '''

arr = array([2, 3, 5, 9, 8, 4])
arr2 = arr
print(arr)
print(arr2)
# in this case both the array having the same value will point the same address
print("address of arr ", id(arr))
print("address of arr2 ", id(arr2))

arr2[2] = 255
print(arr)
print(arr2)
print("address of arr ", id(arr))
print("address of arr2 ", id(arr2))
# in this case if we change the value of one array the value of second array will automatically be
# changed but the address will remain same

''' shallow copy method'''

arr3 = array([1, 2, 3, 4, 5, 6])
arr4 = arr3.view()
# we use view function to apply the shallow method
# in this case two arrays having the same value will have two different addresses
# changing in one array's value will also change the value of the second array

print(arr3)
print(arr4)
print("address of arr3 ", id(arr3))
print("address of arr4 ", id(arr4))


'''  Deep copy method   '''

arr5 = array([9, 8, 7, 6, 5, 4])
arr6 = arr5.copy()
# we use copy function to apply deep copy method
# both array will have two different addresses

# changing in one array's value will not affect the other one

arr5[0] = 777
print(arr5)
print(arr6)
print("address of arr5 ", id(arr5))
print("address of arr6 ", id(arr6))
