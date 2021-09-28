import calendar as cal
print(cal.calendar(2020)) # this will give us the calendar of the given year : calendar(year)
print(cal.month(2000, 12)) # this will give the calender of given month : month(year, month)

print(cal.weekday(2020,7,15)) # this will give the week day for the given date : weekday(year, month, date)

print(cal.isleap(2020)) # this will give true or false if the given year is leap it will give true otherwise false
# isleap(year)


'''
to find the number of leap year in the given range  we will use leapdays
 syntax----    leapdays(year1,year2)

'''
print(cal.leapdays(1970, 2020))