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

def func_a(q):
	fi = list(factorint(q).items())
	# test 
	# case A  odd primes only
	# case B even prime only
	# case C all primes
	print(fi, end="  ")	
	if(fi[0][0] != 2):
		print("Odd prime(s) only.")
	else:
		if(len(fi) == 1):
			print("Prime 2 only.")
		else:
			print("Even and odd primes.")
		



def main(args):
	for q in range(2,20):
		func_a(q)
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
