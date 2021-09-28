def print_even(s=1, e=10):
	for i in range(s,e+2):
	    if(i % 2==0):
             print(str(i)+",",end=" ")

print("The series is:" ,end="")
print_even()
print("\nThe series is:",end="")
print_even(0)
print("\nThe series is:",end="")
print_even(10,100)
print("\nthe series is:",end="")
print_even(e=100)
