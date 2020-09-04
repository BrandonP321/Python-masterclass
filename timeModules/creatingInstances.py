import datetime

"""These are the 3 most useful classes of the datetime module"""

date = datetime.date(year=2020, month=7, day=21)
print(f"datetime.date: {date}")  # 2020-07-21

time = datetime.time(hour=11, minute=33, second=54, microsecond=348983)
print(f"datetime.time: {time}")  # 11:33:54.348983

date_time = datetime.datetime(year=2020, month=7, day=21, hour=11, minute=33, second=54, microsecond=348983)
print(f"datetime.datetime: {date_time}\n")  # 2020-07-21 11:33:54.398204

year, month, day, hour, minute, second, microsecond = (2020, 7, 20, 11, 33, 54, 398204)
print(datetime.datetime(year, month, day, hour, minute, second, microsecond))
print()

"""3 other ways to create instances"""

# creates instance of the current local date
today = datetime.date.today()
print(f"datetime.date.today(): {today}")  # 2020-08-28

# creates instance of the current date and time
timeNow = datetime.datetime.now()
print(f"datetime.datetime.now(): {timeNow}\ttype: ", end='')  # YYYY-MM-DD HH:MM:SS.SSSSSS
print(type(timeNow))

# combines instances of datetime.date & datetime.time into a sings datetime.datetime instance
current_time = datetime.time(timeNow.hour, timeNow.minute, timeNow.second, timeNow.microsecond)
combined = datetime.datetime.combine(today, current_time)
print(f"datetime.datetime.combine(<date>, <time>): {combined}\n")

"""Using a string to create an instance of datetime"""

# converts the string into a datetime.date type
dateIso = datetime.date.fromisoformat("2000-07-21")
print(f"datetime.date.fromisoformat(): {dateIso}\t", end='')
print(f"type: {type(dateIso)}")

# similar to previous
timeIso = datetime.time.fromisoformat("05:42:32.483720")
print(f"datetime.time.fromisoformat: {timeIso}", end='\t')
print(f"type: {type(timeIso)}")

# similar to previous
dateTimeIso = datetime.datetime.fromisoformat("2000-07-21 05:42:32.483720")
print(f"datetime.datetime.fromisoformat: {dateTimeIso}", end='\t')
print(f"type: {type(dateTimeIso)}")
print()

"""Handling dates & time not in the iso 8601 format"""

date_string = "01-31-2020 14:45:37"
formatted_string = "%m-%d-%Y %H:%M:%S"
date_string_final = datetime.datetime.strptime(date_string, formatted_string)
print(f"datetime.datetime.strptime(date_string, formatted_string): {date_string_final}")
