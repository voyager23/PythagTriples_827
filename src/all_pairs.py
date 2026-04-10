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
import math

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
	
def a_42(n):
	"""
	let a = 42 then a^2 = 1764
	a = 2*3*7  then 1764 = 2^2 * 3*2 * 7^2
	exponent range is 0 <= e < 3

	# Assume idx is list of current exponents. (dynamic)
	# Assume blist is list of current bases. (static)
	# for working_index in range(len(idx)):
	#	calc divisor
	#	calc dividend
	"""
	factors = list(factorint(n).items())	# [ (base:exponent),...]
	# square the exponents using a list comprehension
	# use a list comprehension to get a list of doubled exponents
	# prepare the base n counter for each prime
	bnc = bncnt.BaseNcounters([x[1]*2 for x in factors])
	# list the primes
	plst = [x[0] for x in factors] #[p0,p1,p2...]
	bases = bnc.get_base_list()
	count = 0
	pivot = False
	while(True):
		idx = bnc.get_indices()	# current exponents
		# plist has the corresponding primes
		divisor = [x**y for x in plst for y in idx]
		divisor = math.prod(divisor)
		#dividend = 2**(2-e2) * 3**(2-e3) * 7**(2-e7)
		idxcomp = bnc.get_idx_complement()
		dividend = [x**(y[1]) for x in plst for y in idxcomp]
		dividend = math.prod(dividend)
					# ~ if(divisor%2 != dividend%2):
						# ~ print("\t",end="")
					# ~ else:
						# ~ count += 1
		print(divisor,dividend)
					# ~ print(factorint(divisor), end = " ")
					# ~ print(factorint(dividend))
		# Breakout logic here
		count += 1
		if(divisor==dividend):
			pivot = True
			count -= 1
			break
		bnc.inc_counters()
	return count

	
def main(args):
	# ~ product,primes = max_distinct_prime_product(1000000000)
	# ~ print(product, primes)
	print(a_42(42),"useable equal-parity pairs")
	#pairs_225()
	#pairs_196()
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
