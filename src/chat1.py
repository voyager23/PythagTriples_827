def factor_pairs(n):
    # Prime factorisation for 2304 = 2^8 * 3^2
    factors = [(2, 8), (3, 2)]
    
    limit = int(n**0.5)
    divisors = []

    # Generate all divisors
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

    # Build pairs
    pairs = [(d, n // d) for d in divisors]
    return pairs


pairs = factor_pairs(2304)

for p in pairs:
    print(p)
