# prime_utils.py

def max_distinct_prime_product(limit):
    primes = []
    
    def is_prime(n):
        if n < 2:
            return False
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

    n = 2
    product = 1

    while True:
        if is_prime(n):
            if product * n > limit:
                break
            primes.append(n)
            product *= n
        n += 1

    return product, primes
