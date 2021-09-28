from datetime import datetime
from datetime import date
'''
datetime function for time and time function for date
'''

time = datetime.now()
print(time)
print(date.today())
print(date.today().weekday()) # this will give the week date for today as it counts monday as 0 and saturday as 6
