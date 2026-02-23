# dates.py

import datetime

# Current datetime
now = datetime.datetime.now()
print("Current datetime:", now)

# Custom datetime
custom_date = datetime.datetime(2026, 2, 23, 10, 30, 0)
print("Custom datetime:", custom_date)

# Formatting
print("Formatted date:", now.strftime("%Y-%m-%d"))
print("Formatted time:", now.strftime("%H:%M:%S"))

# Time difference
d1 = datetime.datetime(2026, 1, 1)
d2 = datetime.datetime(2026, 2, 23)

diff = d2 - d1
print("Days difference:", diff.days)