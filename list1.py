#lists are the collection of data , the data in the list can be of same type or can be of different type
#we can change the value of the list whenever we want that means they are "mutable"
# the list can be initialized by using angular brackets
nums=[23,24,36,56,59,95,56,89,65,99,5,66,996,66,6,6,6,9,6,32,98,96,5,7,9,5,1,87,96,23,1,8]
print("\noriginal list:\n",nums)
popped=nums.pop()
print("\nthe popped item is:",popped,"and this was the last item in the list ")
print("\nafter poping without any argument:\n",nums)
nums.pop(5)
print("\npoping with argument 5:\n",nums)
del nums[1:6]

print("After deleting from index  number 1 to 6 in the list using del keyword \n",nums)
del nums [5]
print("After deleting from index  number 5 in the list using del keyword only one argument \n",nums)
#nums.extend()
