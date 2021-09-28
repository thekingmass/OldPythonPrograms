#tuples are same as the list but they are "immutable" that means the value of tupls can not be changed
# the tuple is initialized by using the round braces
tup = (25,94,75,45,46,21,75,32)
print(tup)
print(tup[5])
count=tup.count(75)
#the count method count the number of occurrance of the element in the tuple list
print("the numbe of occurance of 75 is :: ",count)
count2=tup.count(94)
print("the numbe of occurance of 94 is :: ",count2)
#we can not change the value of the tuple so we cant execute the following statemet
# tup[5]=25
######  Now the time for set
# A set is exactly same as the set in the mathematics . in python a set is just like a list.
# we can chang the value of the set
# but there is one main defference between list and set a set can not contain any duplicate value
# A set is initialized by using the curly braces
set= {65,12,65,36,47,25,96,81,65,96}
# I have repeated the values in the set but at the time of printing it will make it distinct that means
# the duplicate value will be print once
print("\n",set)
length=set.__len__()
print("the length of the set is ",length)

