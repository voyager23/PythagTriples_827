#!/usr/bin/env python3
#
#  hypot_leg_count.py
#  
#  Copyright 2026 Mike <mike@Fedora40>

import sys
from sympy.ntheory import factorint
import BaseNcount as bncnt
import math

def func_q(q):
	pairs = factorint(q)
	for k in pairs.keys():
		pairs[k] *= 2	# squaring the factorization
	d1 = list()
	d3 = list()
	for p,e in pairs.items():
		if(p % 4 == 1):
			d1.append([p,e])
		else:
			d3.append([p,e])
	print(f"q:{q}  d1:{d1}  d3:{d3}")
	return 0
	
	
def main(args):
	func_q(120)
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
