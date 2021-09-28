'''
there  are  6 ways for creating array with the help of numpy module
1 array()
2 linspace()
3 logspace()
4 arange()
5 zeros()
6 ones()
'''

''' --------------------------------------------------------------------------------------------------------------'''

from numpy import *

''' first one is array function  this is similar to the module array '''
arr = array([12, 58, 49, 46547], int)
'''
 we can specify the data type also in the array() to make it distinct 
 doing so will restrict the data to be entered in the array if the type of the data will not math with the 
 specified data type
 eg. arr = array([12,...,45],int)
 '''
print(arr)
print(arr.dtype)  # dtype means data type

''' --------------------------------------------------------------------------------------------------------------'''

arr2 = linspace(1, 10, 10)
''' the linspace function make the some equal parts from the given range
    It takes three arguments. 1)the lower bound of the range. 2)The upper bound of the range. 3) number of parts that
     we want to make equally
     in the above line arr2 = linspace(0, 40, 10)
     0 is the lower bound from where it will start to make parts and 40 is the upper bound till the range it will make 
     parts and 10 is the number of parts which will be made from range 0 to 40
     '''
print(arr2)
''' --------------------------------------------------------------------------------------------------------------'''

arr3 = logspace(0, 20,  10)
''' the logspace() function is same as the linspace() but the difference is it first make the values to
 the base 10 and then make the equal parts   
'''
print(arr3)
''' --------------------------------------------------------------------------------------------------------------'''
arr4 =  arange(0, 42, 3)
'''
the arange function is similar to the range() function 
'''
print(arr4)

''' --------------------------------------------------------------------------------------------------------------'''

arr5 = zeros(10, int)
'''
the zeros function is used to make the array of some size having the value zero .
it can take two argument first one is specify the size of the array and the second one for the data type of like int or float
'''
print(arr5)

''' --------------------------------------------------------------------------------------------------------------'''

arr6 = ones(5, int)
'''
the ones function is used to make the array of some size having the values one .
it can take two argument first one is specify the size of the array and the second one for the data type of like int or float
'''

print(arr6)