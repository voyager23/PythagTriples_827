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
	# Define 3 transformation matrix
	A = np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
	B = np.array([[1,2,2],[2,1,2],[2,2,3]])
	C = np.array([[1,-2,2],[2,-1,2],[2,-2,3]])
	ptt1 = (np.dot(A,Z))
	ptt2 = (np.dot(B,Z))
	ptt3 = (np.dot(C,Z))
	return [ptt1, ptt2, ptt3]
	
def ptt_linear_berggren(Z):
	# Z is a 3-list of integers
	a = Z[0]
	b = Z[1]
	c = Z[2]	# convenience variables
	return [[-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c],
			[a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c],
			[a - 2*b + 2*c, 2*a -b + 2*c, 2*a -2*b + 3*c ]]

	
def ptt_price(Z):
	# Define 3 transformation matrix
	A = np.array([[2,1,-1],[-2,2,2],[-2,1,3]])
	B = np.array([[2,1,1],[2,-2,2],[2,-1,3]])
	C = np.array([[2,-1,1],[2,2,2],[2,1,3]])
	ptt1 = (np.dot(A,Z))
	ptt2 = (np.dot(B,Z))
	ptt3 = (np.dot(C,Z))
	return [ptt1, ptt2, ptt3]
	
def ptt_linear_price(Z):
	# Z is a 3-list of integers
	a = Z[0]
	b = Z[1]
	c = Z[2]	# convenience variables
	return [[2*a + b - c , -2*a + 2*b + 2*c, -2*a + b + 3*c],
			[2*a + b + c , +2*a - 2*b + 2*c, +2*a - b + 3*c],
			[2*a - b + c , +2*a + 2*b + 2*c, +2*a + b + 3*c]]
	
def build_nlevel_tree(levels, transform = 'P'):
	tree = [[[3,4,5]]]	# Initial tree with base triple
	level = 0
	while(level < levels):
		src = tree[-1]
		dst = []
		for pt in src:
			if transform == 'P':
				# extend adds an 'object'
				dst.extend(ptt_linear_price(pt)) 	# add 3 lists to the tree using Price transform
			else:
				dst.extend(ptt_linear_berggren(pt))	# Berggren transform
		tree.append(dst)	# adds individual lists to tree
		level += 1			
	return tree
	
def main(args):
	tree = build_nlevel_tree(3,'P')
	
	for z in tree:
		print()	# z is list of arrays
		for a in z:
			print(a)	# a is an array of 3 int
		print()
		
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
