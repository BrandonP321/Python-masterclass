import datetime

"""Below are examples of datetime.timedelta instances for arithmetic"""

now = datetime.datetime.now()
print(f"now: {now}")

tomorrow = datetime.timedelta(days=+1)
print(f"tomorrow: {tomorrow}")  # 1 day, 0:00:00

print(now + tomorrow)
print()

"""Days can also be a negative value to represent days in the past"""

day_less = -1
yesterday = datetime.timedelta(days=day_less)
print(f"yesterday: {yesterday}")  # -1 day, 0:00:00

print(now + yesterday)
print()

"""another example"""

delta = datetime.timedelta(days=+4, weeks=+4, hours=-4)
print(delta)  # 31 days, 20:00:00

print(now + delta)
print()

"""relativedelta is a much more powerful replacement for timedelta; it can manipulate larger intervals"""

from dateutil.relativedelta import relativedelta

delta = relativedelta(years=+5, months=+2, days=+4, hours=+6)
print(delta)
print(now - delta)
print()

"""relativedelta can also be used to find the difference between two dates"""

now = now
tomorrow = tomorrow + now
difference = relativedelta(now, tomorrow)  # now - tomorrow
print(difference)  # relativedelta(days=-1)
