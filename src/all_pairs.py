#!/usr/bin/env python3
#
#  all_pairs.py
#  
#  Copyright 2026 Mike <mike@Fedora40>
#  


import sys
from sympy.ntheory import factorint
from prime_utils import max_distinct_prime_product
import BaseNcount as bncnt

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
	
def a_42():
	"""
	let a = 42 then a^2 = 1764
	a = 2*3*7  then 1764 = 2^2 * 3*2 * 7^2
	exponent range is 0 <= e < 3
	"""
	# Test output only
	bnc = bncnt.BaseNcounters([2,2,2])
	for c in bnc.get_base_list():
		print(f"n:{c.get_n()}/base{c.get_base()}",end=" ")
	print()
	# End test output
	
	count = 0
	pivot = False
	for e2 in range(3):
		if(pivot==True):
			break
		for e3 in range(3):
			if(pivot==True):
				break
			for e7 in range(3):
				divisor = 2**(e2) * 3**(e3) * 7**(e7)
				dividend = 2**(2-e2) * 3**(2-e3) * 7**(2-e7)
				if(divisor%2 != dividend%2):
					print("\t",end="")
				else:
					count += 1
				print(divisor,dividend, end = " ")
				print(factorint(divisor), end = " ")
				print(factorint(dividend))
				# Breakout logic here
				if(divisor==dividend):
					pivot = True
					count -= 1
					break
	return count

	
def main(args):
	# ~ product,primes = max_distinct_prime_product(1000000000)
	# ~ print(product, primes)
	print(a_42(),"useable equal-parity pairs")
	#pairs_225()
	#pairs_196()
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
