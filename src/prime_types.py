#!/usr/bin/env python3
#
#  prime_types.py
#  
#  Copyright 2026 mike <mike@fedora>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys
from sympy.ntheory import factorint
#from prime_utils import max_distinct_prime_product
import BaseNcount as bncnt
import math

def func_legs(q):
	fint = factorint(q)	# Dictionary of prime:exponent pairs
	print(q, " -> ", fint)
	product = 1
	for p in fint.keys():
		fint[p] *= 2
		if p != 2:
			fint[p] += 1
		else:
			fint[p] -= 1
		product *= fint[p]
	print(q*q, " -> ", fint)
	legs = (product - 1) // 2
	return legs
	
def func_hypots(q):
	fint = factorint(q)	# Dictionary of prime:exponent pairs
	print(q*Q, " -> ", fint)
	# Using BaseNcount and prime/exponent data, cycle thro' all the divisors
	# and count 4K+1 and 4k+3 types to find divisors
	# Divisor pairs are related to a^2 and b^2 such that a divisor pair (squared)
	# may equal q^2
	
	

def main(args):

	pairs = func_legs(75)
	print("Legs: ",pairs,"\n")

	
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
