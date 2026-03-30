#!/usr/bin/env python3
#
#  calc_q_n.py
#  
#  Copyright 2026 Mike <mike@Fedora40>
#  
#  


import sys
import math
import itertools as it
from sympy import ntheory

def triples_legs(n):
	# list divisor pairs for n
	# find expanded prime factorisation
	# list all combinations from 1 to nfactors
	# apply set to remove repeats
	# count pairs with equal parity
	
	return (-1)
	
def triples_hypot(n):
	return (-2)

def Qn(n):
	# Define Q(n) to be the smallest number which occurs in exactly n Pythagorean Triples
	# Examples Q(5) = 15, Q(10) = 48 and Q(10^3) = 8064000
	# Given a number e.g. a = 75
	# find the number of triples when 75 is a 'leg'
	nlegs = triples_legs(n)
	nhyps = triples_hypot(n+5)
	#total = nlegs + nhyps
	total = -1
	print(f"nlegs = {nlegs} nhypn = {nhyps} total = {total}")
	return total

def main(args):
	Qn(75)	# expect 7 + 2 = 9
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
