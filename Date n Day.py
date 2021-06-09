import calendar as cal

def day_name(v1, v2, v3):
    c=cal.weekday(v1,v2,v3)
    return cal.day_name[c]

print(day_name(2001,12,12))