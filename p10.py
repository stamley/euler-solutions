#p10
import math

def sum_of_primes():
    sum = 0
    for i in range(2, 2_000_000):
        if is_prime(i):
            sum += i
    return sum

def is_prime(n):
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(sum_of_primes())