#!/usr/bin/env python3
#
#  all_pairs.py
#  
#  Copyright 2026 Mike <mike@Fedora40>
#  


import sys
from sympy.ntheory import factorint
from prime_utils import max_distinct_prime_product

def pairs_225():
	# Consider 3^2 * 5^2 = 225
	# 3^4 * 5^4 =
	numerator = 3*3*5*5 
	print(numerator)
	count = 0
	for e3 in range(5):
		for e5 in range(5):
			divisor = 3**(e3) * 5**(e5)
			dividend = 3**(4-e3) * 5**(4-e5)
			print(divisor,dividend)
			count += 1
	print(f"{count} pairs found\n")
	return 0

def pairs_196():
	# Consider 2^2 * 7^2 = 196
	numerator = 2*2*7*7 
	print(numerator)
	count = 0
	for e2 in range(5):
		for e7 in range(5):
			divisor = 2**(e2) * 7**(e7)
			dividend = 2**(4-e2) * 7**(4-e7)
			if(divisor%2 != dividend%2):
				print("\t",end="")
			print(divisor,dividend, end = " ")
			print(factorint(divisor), end = " ")
			print(factorint(dividend))
			count += 1
	print(f"{count} pairs found\n")
	return 0

def pairs_1764():
	# Consider 2*2 * 3*3 * 7*7 = 1764
	numerator = 2*2*3*3*7*7 
	print(numerator)
	count = 0
	for e2 in range(5):
		for e7 in range(5):
			
			divisor = 2**(e2) * 7**(e7)
			dividend = 2**(4-e2) * 7**(4-e7)
			if(divisor%2 != dividend%2):
				print("\t",end="")
			print(divisor,dividend, end = " ")
			print(factorint(divisor), end = " ")
			print(factorint(dividend))
			count += 1
	print(f"{count} pairs found\n")
	return 0
	
def main(args):
	product,primes = max_distinct_prime_product(1000000000)
	print(product, primes)
	exit(0)
	pairs_225()
	pairs_196()
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
