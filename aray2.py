from array import *
arr = array('i',[])
n = int(input("Enter the size of the array"))
for i in range(n):
    val = int( input("Enter the next value"))
    arr.append(val)

for i in arr:
    print(i)

# Searching for an element in array
k=0
x = int(input("Enter the value to be searched "))
for e in arr:
    if e==x:
        print("the value is found" , e , "At position" , k)
        break
    k+=1

# we can also do so by using some in build function

print(arr.index(x))
