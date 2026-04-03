import sys
from sympy.ntheory import factorint

def factor_pairs(n):
    # Prime factorisation for 2304 = 2^8 * 3^2
    n *= n	#square n
    # factors = [(3, 2), (5, 4)]
    factors = list(factorint(n).items())	# [ (base:exponent),...]
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
	#--------------------
    generate()
    divisors.sort()
    # Build pairs
    pairs = [(d, n // d) for d in divisors]
    return pairs
    #---------------------



def main(args):
	pairs = factor_pairs(10)
	for p in pairs:
		print(p)
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


