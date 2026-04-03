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
    
def check_pair(t):
	# t is 2-tuple of integer
	# return True if both elements are of equal odd/even parity
	return t[0]%2 == t[1]%2 and t[0] != t[1]
	
def main(args):
	query = 48
	
	pair_count = 0
	pairs = factor_pairs(query)
	for p in pairs:
		if(check_pair(p)):
			print(p)
			pair_count += 1
	print(f"Query: {query} -> testing {query*query}")
	print(f"Found {pair_count} pairs.")
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


