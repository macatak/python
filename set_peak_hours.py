#!/bin/python3

'''
determine if it's off hours or work hours
Sat/Sun are off hours
8AM-4PM are not off hours
time is based on server time, not GMT
'''

from datetime import date
from datetime import datetime

def get_off_hours():
    now = datetime.now()
    hour_of_day = int(now.strftime("%H"))
    # this will be 1-5 for Mon-Fri
    day_of_week = now.isoweekday()
    print('hour: {} - day of week: {}'.format(hour_of_day,day_of_week))
    if day_of_week >= 6:
        # Sat/Sun will be 6/7
        off_hours = 1
    elif hour_of_day <= 6:
        # 6AM or earlier
        off_hours = 1
    elif hour_of_day >= 17:
        # 5PM or later
        off_hours = 1
    else:
        off_hours = 0
    return(off_hours)

if __name__ == '__main__':
    print(get_off_hours())
