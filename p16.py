#p16

import math

def power_digit_sum():
    string = 2**1000
    sum = 0
    for c in str(string):
        sum += int(c)
    return sum

print(power_digit_sum())