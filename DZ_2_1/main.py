import time


def count_leap_years(num):
    start = 1972
    cnt = 0
    while num > start:
        start += 4
        cnt += 1
    return cnt


def add_zero(num):
    if num < 10:
        return str('0' + str(num))
    else:
        return str(num)


time_stamp = time.time()
print(time_stamp)

months = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}

sec = int(time_stamp)
end_sec = sec % 60

minute = sec / 60
end_min = int(minute % 60)

hour = minute / 60
end_hour = int(hour % 24)

day = hour / 24
end_day = int(day % 365)

year = int(day / 365) + 1970

temp = 0
month = 0
for index, i in enumerate(months):
    if temp + i > end_day:
        end_day -= temp + count_leap_years(year)
        month = index + 1
        break
    temp += i

month = add_zero(month)
end_day = add_zero(end_day)
end_hour = add_zero(end_hour)
end_min = add_zero(end_min)
end_sec = add_zero(end_sec)
year = str(year)

print(year + "." + month + "." + end_day + " " + end_hour + ":" + end_min + ":" + end_sec)
print(time.gmtime(time_stamp))
