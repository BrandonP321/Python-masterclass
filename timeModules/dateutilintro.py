from dateutil import tz
import datetime

"""Must first import tz from dateutil as dateutil is a package, not a module"""

now = datetime.datetime.now(tz=tz.tzlocal())
print(f"datetime.datetime.now(tz=tz.tzlocal()): {now}", end='\t')  # 2020-08-28 22:50:22.216819-7:00
print(type(now))
print(now.tzname(), end='\t')  # Pacific Daylight Time
print(type(now.tzname()))

"""Can also create time zones that not the same as the time zone reported by your computer"""

London_tz = tz.gettz("Europe/London")
now = datetime.datetime.now(tz=London_tz)
print(f"datetime.datetime.now(tz=London_tz: {now}")
print(now.tzname())

print()

print(tz.tzutc)