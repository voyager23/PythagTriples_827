import sys
from sympy.ntheory import factorint
from prime_utils import max_distinct_prime_product

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
	
def count_divisor_pairs(n):
	# factorint returns a dictionary containing 
	# the prime factors of n as keys and their respective multiplicities as values.
	# e.g. {2: 4, 3: 2}
	primes = factorint(n)
	pairs = 1
	for p,e in primes.items():
		if(p == 2):
			pairs *= (e+1) #?
		else:
			pairs *= (e+1)
	return pairs
			
	
def main(args):
	while(True):
		
		query = input("Enter a query or return to quit: ")
		if(query == ""):
			return 0
		else:
			query = int(query)
		if(query < 1):
			return 0
			
		pair_count = 0
		pairs = factor_pairs(query)	# pairs is a list of 2-tuples
		for p in pairs:
			#if(check_pair(p)):
			if(True):
				print(p)
				pair_count += 1
		print(f"Query: {query} -> testing {query*query}")
		print(f"Found {pair_count} pairs.")
		# analyse pairs into 3 groups, odd, even and mixed parity
		even = list()
		odd = list()
		mixed = list()
		for p in pairs:
			if (p[0]%2 != p[1]%2):
				mixed.append(p)
			else:
				if(p[0]%2 == 0):
					even.append(p)
				else:
					odd.append(p)
					
		print("Even Parity")
		for q in even:
			a = factorint(q[0])
			b = factorint(q[1])
			print(f"{q}\t{a}\t{b}")
		print()
		
		print("Odd Parity")
		for q in odd:
			a = factorint(q[0])
			b = factorint(q[1])
			print(f"{q}\t{a}\t{b}")
		print()
		
		print("Mixed Parity")
		for q in mixed:
			a = factorint(q[0])
			b = factorint(q[1])
			print(f"{q}\t{a}\t{b}")
		print()
		print("-----------------------------------")
		print(f"count_divisor_pairs({query}) = {count_divisor_pairs(query)}")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


