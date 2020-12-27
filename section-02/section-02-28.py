# Section 2
# 28. Date & Time

import time
import calendar

# Ticks
var1 = time.time()
print(var1)

# Local Time
local = time.localtime(time.time())
print(local)

# Formatted Time
timeLocal = time.asctime(time.localtime(time.time()))
print(timeLocal)

# Calendars
calendarVar = calendar.month(2008, 1)
print(calendarVar)

# Basic date and time types —  https://docs.python.org/3/library/datetime.html

# Output
# 1608988994.315279
# time.struct_time(tm_year=2020, tm_mon=12, tm_mday=26, tm_hour=13, tm_min=23, tm_sec=14, tm_wday=5, tm_yday=361, tm_isdst=0)
# Sat Dec 26 13:23:14 2020
#     January 2008
# Mo Tu We Th Fr Sa Su
#     1  2  3  4  5  6
#  7  8  9 10 11 12 13
# 14 15 16 17 18 19 20
# 21 22 23 24 25 26 27
# 28 29 30 31
