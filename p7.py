# p7

import time
import math

def which_prime():
    c = 0
    i = 0
    can = 2
    while c < 10002:
        i += 1
        if is_prime(i):
            can = i
            c += 1
    return can

def is_prime(n):
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

st = time.process_time()
which_prime()
et = time.process_time() - st
print(et)