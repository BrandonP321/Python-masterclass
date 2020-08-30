import datetime

PYCON_DATE = datetime.datetime(year=2021, month=5, day=12, hour=8)
countdown = PYCON_DATE - datetime.datetime.now()
print(f"Countdown to Pycon US 2021: {countdown}")
print(type(countdown))  # datetime.timedelta
print()

"""below is and updated version using the tz and parser modules from the dateutil package"""

from dateutil import tz, parser

PYCON_DATE = parser.parse("May 12, 2021 8:00 AM")
print(PYCON_DATE)  # 2021-05-21 08:00:00
print(type(PYCON_DATE))  # datetime.datetime

# PYCON_DATE is currently a naive instance of datetime.datetime; .replace() is used to add a timezone to it
PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))
print(PYCON_DATE)  # 2021-05-12 08:00:00-04:00
print(type(PYCON_DATE))  # still a datetime.datetime instance

now = datetime.datetime.now(tz=tz.tzlocal())
countdown = PYCON_DATE - now
print(f"countdown to Pycon US 2021: {countdown}")
