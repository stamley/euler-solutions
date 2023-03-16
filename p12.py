#p12
def triangle():
    triangle = 1
    i = 2
    while count_divisors(triangle) < 500:
        triangle += i
        i += 1
    return triangle

def divisors_less_than_500(triangle):
    count = 2
    for i in range(2,triangle):
        if triangle % i == 0:
            count += 1
    #print(count)
    return count < 500

primes = []

def sieves():
      # Step 1: generate the sieve of primes up to the square root of n
    global primes    
    is_prime = [True] * (int(1000000**0.5) + 1)
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
            for j in range(i**2, len(is_prime), i):
                is_prime[j] = False

def count_divisors(n):
    # Step 2: divide n by each prime factor and count the number of times
    #         it is divisible
    global primes
    count = 1
    for p in primes:
        if p**2 > n:
            break
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        count *= (exp + 1)

    # If n is still greater than 1, it is a prime factor of n
    if n > 1:
        count *= 2

    return count

sieves()

print(triangle())