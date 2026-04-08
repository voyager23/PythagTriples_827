#!/usr/bin/env python3
#
#  BaseNcount.py
#  
#  Copyright 2026 mike <mike@fedora.home>
#  

import sys

class BaseN:

	def __init__(self, base):
		self.base = base
		self.n = 0	# current counter state

	def inc(self, m=1): # increment n modulo current base
		self.n = (self.n + m) % self.base
		return self.n
		
	def dec(self, m=1):
		self.n -= m
		while(self.n < 0):
			self.n += self.base
			
	def get(self):
		return self.n
		
	def set(self,m):
		self.n = m % self.base
		while(self.n < 0):
			self.n += self.base
			
def main(args):
	counters = [BaseN(2), BaseN(4), BaseN(6)]
	working = len(counters) - 1
	
	while(True):
		for bn in counters:
			print(bn.get(),end=" ")
		print()
		z = counters[working].inc()
		if(z == 0):	# need to retreat and increment previous counter
			while(True):
				working -= 1
				if(working < 0):
					return 0
				y = counters[working].inc()
				if(y != 0):	# Success
					working = len(counters) - 1
					break
				else:	# Increment failed
					continue
		else:
			continue
			
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
