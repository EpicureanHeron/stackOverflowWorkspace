from datetime import datetime,timedelta

time_str = "09:00"
time_object = datetime.strptime(time_str, '%H:%M')
new_time =  time_object + timedelta(hours=1)
print(new_time.time())