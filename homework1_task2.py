user_time_in_seconds = int(input("Введите время в секундах: "))

hours = user_time_in_seconds // 3600
minutes = user_time_in_seconds % 3600 // 60
seconds = user_time_in_seconds % 60

time_in_hour_minutes_seconds = "%02d:%02d:%02d" % (hours, minutes, seconds)
print(time_in_hour_minutes_seconds)