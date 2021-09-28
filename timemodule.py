from time import *
'''
The epoch is the point where the time stars. 
the time function gives us the result in second from the epoch which is 1 jan 1970.
'''
print(time()) # this will give output in seconds since 1 jan 1970 to current time

print(localtime())
# the localtime() function will give us the current time and date in the form of tuple
# sequence is:  year,month, date, hour , min, sec, weekday, YearDay, isdst
'''
lets make a tuple and give it the values of some date in the above sequence
and then we will use mktime() functin this will give us the values in seconds from the epoch to the given time
lets do this.
'''
tu = (2000, 5, 28, 13, 25, 42, 3, 167, 0)
print(mktime(tu))
# this will gives output in the seconds from epoch time to the given time

print(asctime()) # to print the current date and time