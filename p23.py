#p23
 
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

def sum_of_divisors(n):
    # Initialize sum to 1, as 1 is a divisor of all numbers
    divisor_sum = 1

    # Step 2: Find all prime factors and their exponents of n
    global primes
    for p in primes:
        if p**2 > n:
            break
        exp = 0
        while n % p == 0:
            n //= p
            exp += 1
        divisor_sum *= (p**(exp+1) - 1) // (p - 1)

    # If n is still greater than 1, it is a prime factor of n
    if n > 1:
        divisor_sum += (n + 1)

    return divisor_sum