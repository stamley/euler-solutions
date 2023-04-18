#p19
def counting_sundays():
    year = 1901
    # sunday
    day = 7
    day_in_month = 6

    month = 1
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    count = 0

    while year < 2001:
        if year % 100 == 0:
            if year % 400 == 0:
                months[2] = 29    
        elif year % 4 == 0:
            months[2] = 29
        else:
            months[2] = 28
        while day_in_month < months[month]+1:
            if day == 7:
                day = 1
                if day_in_month == 1:
                    count += 1
            else: day += 1
            day_in_month += 1
        month += 1
        day_in_month = 1
        if month == 13:
            month = 1
            year += 1
    
    return count

print(counting_sundays())

