year = int(input("Enter The Year"))
if(year%4==0):
    if(year%400==0):
        if(year%100==0):
            print("Leap Year")
        else:
            print("Not Leap")
    else:
        print("Leap Year")
else:
    print("Not leap")