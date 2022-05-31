# Write a Python program to display the current date and time.

import datetime
now = datetime.datetime.now()
print("Currrent Date Time:", now.strftime("%Y-%m-%d %H:%M:%S"))