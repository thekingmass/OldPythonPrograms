import calendar as cal


session = 0

while session == 0:
    #print("press 1 to print calendar and press 2 to exit")
    x = int(input("press 1 to print calendar and press 2 to exit"))
    if x == 1:

        year = int(input("enter the year to find its calendar"))
        print(cal.calendar(year))
    else:
        session = 1
        exit(0)
