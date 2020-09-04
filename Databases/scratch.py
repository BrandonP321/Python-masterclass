import time
import datetime
from dateutil import tz

# zone = datetime.datetime.now(tz=tz.tzlocal())
# print(zone)

time1 = datetime.datetime.now(tz=tz.gettz("America/New_York"))
time.sleep(1)
time2 = datetime.datetime.now(tz=tz.tzlocal())
time.sleep(1)
time3 = datetime.datetime.now(tz=tz.gettz("America/Ojinaga"))

times = []
for time in [(time2, 'time2'), (time1, 'time1'), (time3, 'time3')]:
    times.append(time)

print(f"time1: {time1}")
print(f"time2: {time2}")
print(f"time3: {time3}")

print(times)
print(sorted(times))

print()

time1 = time1.strftime("%z")
print(time1)
