from pip._vendor.pyparsing import countedArray

import array as arr
number = arr.array('I', [25,54,84,24,74,2,7,56,85,52])
# print(number)
for i in range(len(number)) :
    print(number[i])
# we can use while loop also to do so
# lets copy the element of array into another array
cpArray = arr.array( number.typecode , (a+1 for a in number))
print("the element of second array:")
var = 0
while var < len(cpArray) :
    print(cpArray[var])
    var+=1
