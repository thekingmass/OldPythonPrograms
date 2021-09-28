l1=[x for x in range(1,11)]
l2=[x for x in range(2,21) if x%2==0]
l3=[(x,y) for x in l1 for y in l2 if x*x==y]
print("List of numbers is:",l1)
print("2's table is:",l2)
print ("The original to square pair found in 2's table upto 20 is as:",l3)
