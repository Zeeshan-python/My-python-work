import datetime
current_time = datetime.datetime.now()
current_hour = current_time.hour
if current_hour < 12:
    print("Good Morning, Zeeshan!")
elif current_hour < 17:
    print("Good Afternoon, Zeeshan!")
else:
    print("Good Evening, Zeeshan!")
