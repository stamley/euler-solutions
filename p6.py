# p6

import math

def sum_of_squares():
    s = 0
    for i in range(1,101):
        s += math.pow(i,2)
    return s

def square_of_sums():
    s = 0
    for i in range(1,101):
        s += i
    return math.pow(s,2)

print(square_of_sums()-sum_of_squares())