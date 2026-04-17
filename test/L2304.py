#!/usr/bin/env python3
#
#  L2304.py
#  
#  Copyright 2026 mike <mike@fedora.home>
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
import BaseNcount as bncnt
import math




def main(args):
	# List of 27 divisors of 2304 = 48^2
	L2304 = [1,2,3,4,6,8,9,12,16,18,24,32,36,48,64,72,96,128,144,192,256,288,384,576,768,1152,2304]
	d1 = L2304[:13]
	d2 = L2304[14:]
	d2.reverse()
	for x in range(len(d1)):
		if(d1[x]%2 != d2[x]%2):
			print(f"{d1[x]} * {d2[x]} = {factorint(d1[x])} * {factorint(d2[x])} ")
	print()
	for x in range(len(d1)):
		if(d1[x]%2 == d2[x]%2):
			print(f"{d1[x]} * {d2[x]} = {factorint(d1[x])} * {factorint(d2[x])} ")
			v = d2[x]	# hi
			u = d1[x]	# lo
			c = (v+u) // 2
			b = (v-u) // 2
			check = (c*c - b*b - 2304)
			if(check == 0):
				print("Soln")
			else:
				print("No solution?")
			
			
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
