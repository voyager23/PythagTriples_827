def prime_factorisation(n):
    i = 2
    factors = []
    while i * i <= n:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        if count > 0:
            factors.append((i, count))
        i += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def factor_pairs(n):
    factors = prime_factorisation(n)
    limit = int(n**0.5)
    divisors = []

    def generate(idx=0, current=1):
        if idx == len(factors):
            if current <= limit:
                divisors.append(current)
            return
        
        p, max_exp = factors[idx]
        for e in range(max_exp + 1):
            generate(idx + 1, current * (p ** e))

    generate()
    divisors.sort()
    
    return [(d, n // d) for d in divisors]


print(factor_pairs(2304))
