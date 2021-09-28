from numpy import *

'''
we can make multidimension arrays using numpy
for this we have to create an array which will contain two arrays
'''
arr = array([
    [1, 2, 3],
    [4, 5, 6]
])
# this is a 2D-Array
print("this is the first 2D Array")
print(arr)

arr2 = array([
    [7, 8, 9],
    [10, 11, 12]
])
print("this is the second 2D Array")
print(arr2)

arr3 = arr + arr2
print("this is the addition of two arrays")
print(arr3)
# we can do subtraction also

''' there are some functions in python which we can use in our program'''
print("The data type of the array arr is:", arr.dtype)  # This will print the data type of the array
print("the dimension of the array arr is :", arr.ndim)  # This will print the dimension of the array
print("The shape of the array arr is :", arr.shape)  # This will print the shape of the array ((2 * 3), or (4 * 5) etc)
print("The size of the array is:", arr.size)  # This will give the total number of element in the N-D array


''' converting 2D array into 1D array '''
print("The 2D array is :")
print(arr2)
arr4 = arr2.flatten() #this converts the 2D array into 1D
print("the converted 1D array is :")
print(arr4)
print("the dimension of the array arr4 is :", arr4.ndim)

''' converting from 1D array to N-D array'''
print("the 1D array is :")
print(arr4)

arr5 = arr4.reshape(3, 2)# it converts 1D array into 2D. It takes two arguments number of columns and number of row
#                       but remember one thing the multiplication of row and columns must be equal to size of 1D array
print("the new 2D array is:")
print(arr5)
print("The shape of the array arr5 is :", arr5.shape)



