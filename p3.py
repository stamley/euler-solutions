import math

def prime_factors(prime):
    m = 1
    for i in range(2, round(math.sqrt(prime))):
        if prime % i == 0 and is_prime(i):
            if i > m:
                m = i
    return m

def is_prime(n):
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(prime_factors(600851475143))