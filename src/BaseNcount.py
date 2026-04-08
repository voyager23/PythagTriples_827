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
			
	def get_n(self):
		return self.n
		
	def get_base(self):
		return self.base
		
	def set(self,m):
		self.n = m % self.base
		while(self.n < 0):
			self.n += self.base
# ----- End Class BaseN -----

class BaseNcounters:
	
	def __init__(self, base_list):
		self.base_list = list()
		for b in base_list:
			self.base_list.append(BaseN(b))
		self.working = len(self.base_list) - 1
		
	def inc_counters(self, m=1):
		z = self.base_list[self.working].inc()
		if(z == 0):	# need to retreat and increment previous counter
			while(True):
				self.working -= 1
				if(self.working < 0):
					return 0
				y = self.base_list[self.working].inc()
				if(y != 0):	# Success
					self.working = len(self.base_list) - 1
					break
				else:	# Increment failed
					continue
		return self.base_list
	
	def get_base_list(self):
		return self.base_list
		
	def get_indices(self):
		# return a list of current index value for each counter
		idx = list()
		for c in self.base_list:
			idx.append(c.get_n())
		return idx
		
	def all_zero(self):
		for c in self.base_list:
			if(c.get_n() != 0):
				return False
		return True
		
# -----End Class BaseNcounters-----
		
def main(args):
	bnc = BaseNcounters([2,3,5])
	for c in bnc.get_base_list():
		print(f"{c.get_n()}/{c.get_base()}",end=" ")
	print()
	
	while(True):
		bnc.inc_counters()
		print(bnc.get_indices())
		if (bnc.all_zero() == True):
			break
						
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv[1:]))
