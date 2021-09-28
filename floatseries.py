C=0
def generateNext(d,num):

C=float(input("Please input the starting for your series\n"))
s=float(input("Please input the d for your series\n"))
print ("The series produced by this method is")
for i in range(1,11):
        print(generateNext(s,C))
