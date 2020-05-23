import time
import datetime
import pytz
#
# print(time.tzname[1])
# print(time.strftime("%m-%d-%Y\n%H:%M:%S %p\n", time.localtime()))
# print(time.strftime("%m-%d-%Y\n%H:%M:%S", time.gmtime()))
#
# print()
# print(time.time())
#
# print()
# print(time.daylight)

country = 'US/Pacific'
# for x in pytz.all_timezones:
#     print(x)
tz_to_display = pytz.timezone(country)
print(datetime.datetime.now(tz=tz_to_display))

print()
print(f"The time in {country} is {datetime.datetime.now(tz=tz_to_display)}")
print(f"The UTC is {datetime.datetime.utcnow()}")

print()
for x in sorted(pytz.country_names):
    print(f"{x}: {pytz.country_names[x]}")