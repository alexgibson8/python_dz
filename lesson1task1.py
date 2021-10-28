one_minute = 60
one_hour = 3600
one_day = 86400
duration = int(input())
if duration < one_minute:
    print (duration, "сек")
elif duration < one_hour:
    real_minutes = duration // one_minute
    real_seconds = duration % one_minute
    print(real_minutes, "мин", real_seconds, "сек")
elif duration < one_day:
    real_hours = duration // one_hour
    duration = duration % one_hour
    real_minutes = duration // one_minute
    real_seconds = duration % one_minute
    print(real_hours, "час", real_minutes, "мин", real_seconds, "сек")
else:
    real_days = duration // one_day
    duration = duration % one_day
    real_hours = duration // one_hour
    duration = duration % one_hour
    real_minutes = duration // one_minute
    real_seconds = duration % one_minute
    print(real_days, "дн", real_hours, "час", real_minutes, "мин", real_seconds, "сек")