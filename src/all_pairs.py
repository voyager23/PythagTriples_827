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
	factors = list(factorint(n).items())	# [ (base:exponent),...]
	# prepare the base n counter for each prime
	# double the exponents using a list comprehension
	bnc = bncnt.BaseNcounters( [ 2*x[1] for x in factors] )
	# list the primes
	primes = [x[0] for x in factors]
	equal_parity_pairs = list()
	count = 0
	while(True):
		print("[idx, comp]: ", end="")
		foo = bnc.get_idx_complement()
		print(foo)
		divisor = 1
		dividend = 1
		for i in range(len(primes)):
			divisor  *= primes[i]**foo[i][0]
			dividend *= primes[i]**foo[i][1]
			
		print("Checking ", divisor, dividend)
		#if((divisor%2 == dividend%2)and(divisor != dividend)):
		if((divisor%2 == dividend%2)and(True)):
			print(divisor,"/",dividend)
			count += 1
			equal_parity_pairs.append([divisor,dividend])	
		bnc.inc_counters()
		if (bnc.all_zero() == True):
			break
	return count, equal_parity_pairs
	
def resolve_divisor_pairs(a,l):
	# a is the query (int) and l is [u,v]
	# From:
	# 	c = (u+v)/2, b = (v-u)/2, a = q
	# establish the result a^2 + b^2 = c^2
	for p in l:
		c = math.fsum(p) // 2
		p[1] *= -1
		b = math.fsum(p)
		print(f"a:{a} b:{b} c:{c}")
	
	return 0

	
def main(args):
	# ~ product,primes = max_distinct_prime_product(1000000000)
	# ~ print(product, primes)
	x, y = map(int, input("Enter query range as two space separated integers: ").split())
	for a in range(x,y):
		print("\na:",a)
		c,llist = a_42(a)
		print(c,llist)
		
		resolve_divisor_pairs(a,llist)
		
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
