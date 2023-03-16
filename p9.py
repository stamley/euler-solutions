#p9

# a < b < c
# where a^2 + b^2 = c^2
# and a + b + c = 1000

# 1 < 2 < 3
# increase c by one
# 1. check sum
# 2. check squares
# increase c until it reaches 1000
# increase b
# repeat
# 1 < 2 < 3
# 1 < 3 < 4

import math


def pythagorean():
    a, b, c  = 1, 2, 3
    
    while a < 999:
        while b < 1000:
            while c < 1001:
                #if a % 100 == 0 and b % 100 == 0 and c % 100 == 0:
                 #   print((a,b,c))
                if a + b + c != 1000:
                    c += 1
                    continue
                else:
                    if (math.pow(a, 2) + math.pow(b, 2)) == math.pow(c, 2):
                        return a*b*c
                c += 1
            c = 3 + b - 1
            b += 1
        b = 2 + a
        a += 1


print(pythagorean())