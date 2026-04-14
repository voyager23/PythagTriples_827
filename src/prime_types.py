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
	print(q, " -> ", fint)
	legs = (product - 1) / 2
	return legs

	

def main(args):
	for leg in range(3,101):
		pairs = func_legs(leg)
		print("Legs: ",pairs,"\n")

	
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
