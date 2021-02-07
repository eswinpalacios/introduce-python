from datetime import datetime

date_and_hour = datetime.now()
print(date_and_hour)

year = date_and_hour.year
month = date_and_hour.month
day = date_and_hour.day

# hour
hour = date_and_hour.hour
minutes = date_and_hour.minute
seconds = date_and_hour.second

print("hour: {}:{}:{}".format(hour, minutes, seconds))
