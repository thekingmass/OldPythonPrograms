from numpy import *

''' Multiplication of 2D array '''
# for multiplication of two 2D array Number of row of the first array must be equal
# to the number of column of the second array

# declaration of two 2D array

arr = array([
    [2, 3, 5],
    [7, 9, 1]

])
print("the first matrix is :")
print(arr)

arr2 = array([
    [1, 2, 4],
    [6, 8, 10],
    [12, 14, 16]

])
print("the second matrix is :")
print(arr)
# here no of row of the first array is 3 and nu of column of the second array is 3 botha are equal so
# the multiplication can be performed
arr6 = dot(arr, arr2)
print("The multiplication of these two matrices using dot() function is: ")
print(arr6)

arr4 = arr @ arr2
print("the multiplication of matrices using @ is:")
print(arr4)

''' some special features of python for matrix'''
print("the diagonal of matrix arr2 is:", arr2.diagonal())
print("the transpose of the matrix is :")
print(arr2.transpose())
print("the minimum of them is :", arr4.min())
print("the maximum of them is :", arr4.max())
