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
import numpy as np

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
	
def ptt_berggren(Z):
	# Z is a column vector [[a],[b],[c]]
	# Define 3 transformation matrix
	#Z = np.array([[a],[b],[c]])
	A = np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
	B = np.array([[1,2,2],[2,1,2],[2,2,3]])
	C = np.array([[1,-2,2],[2,-1,2],[2,-2,3]])
	ptt1 = np.reshape(np.dot(A,Z),3)
	ptt2 = np.reshape(np.dot(B,Z),3)
	ptt3 = np.reshape(np.dot(C,Z),3)
	return [ptt1, ptt2, ptt3]
	
def ptt_price(Z):
	# Z is a column vector [[a],[b],[c]]
	# Define 3 transformation matrix
	#Z = np.array([[a],[b],[c]])
	A = np.array([[2,1,-1],[-2,2,2],[-2,1,3]])
	B = np.array([[2,1,1],[2,-2,2],[2,-1,3]])
	C = np.array([[2,-1,1],[2,2,2],[2,1,3]])
	ptt1 = np.reshape(np.dot(A,Z),3)
	ptt2 = np.reshape(np.dot(B,Z),3)
	ptt3 = np.reshape(np.dot(C,Z),3)
	return [ptt1, ptt2, ptt3]
	
	
def main(args):
	Y = np.asarray([3,4,5])
	ptt = ptt_berggren(Y)
	print("Base triple ",Y)
	
	for pt in ptt:
		print()
		print(f"From Berggren {pt}")
		pt_price = ptt_price(pt)
		print("From Price:", end='')
		for ptp in pt_price:
			print(ptp, end=' ')
		print()
		
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
