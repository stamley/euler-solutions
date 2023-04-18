#p20

from math import factorial

def fact_digit_sum():
    string = factorial(100)
    sum = 0
    for c in str(string):
        sum += int(c)
    return sum

print(fact_digit_sum())