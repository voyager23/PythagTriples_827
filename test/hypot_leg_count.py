#!/usr/bin/env python3
#
#  hypot_leg_count.py
#  
#  Copyright 2026 Mike <mike@Fedora40>

import sys
from sympy.ntheory import factorint
import BaseNcount as bncnt
import math

def nHypot(qq,d1,d3):
	# expects the square under consideration, qq
	# congruence symbol - ctl + shift + 'u' 2261
	# list d1, (prime,exponent) of primes ≡ 1 mod 4
	# list d3, (prime,exponent) of primes ≡ 3 mod 4
	return 0
	
def nlegs(qq,d1,d3):
	# expects the square under consideration, qq
	# congruence symbol - ctl + shift + 'u' 2261, not congruent 2262
	# list d1, (prime,exponent) of primes ≡ 1 mod 4
	# list d3, (prime,exponent) of primes ≡ 3 mod 4
	return 0

def func_d1d3(q):
	pairs = [[key, value] for key, value in factorint(q).items()]
	# If q is prime and ≢ 4k + 1 there is no soln
	if((len(pairs)==1)and(pairs[0][1]==1)and(pairs[0][0]%4 != 1)):		
		print("Invalid prime, no pairs.")
		return 0
	print(f"q:{q} {pairs}")
	for k in pairs:
		k[1] *= 2	# squaring the factorization
	d1 = list()
	d3 = list()
	for [p,e] in pairs:
		if(p % 4 == 1):
			d1.append([p,e])
			continue
		if(p % 4 == 3):
			d3.append([p,e])
			continue
		# powers of 2 are discarded
	print(f"q^2:{q*q}  d1:{d1}  d3:{d3}")
	return 0
	
	
def main(args):
	while(True):
		q = input("Enter query: ")
		if(q == ""):
			return 0
		func_d1d3(int(q))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
