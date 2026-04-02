#!/usr/bin/env python3
#
#  basicdata.py
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
import math
import itertools as it

ptt_list = [(3, 4, 5),(5, 12, 13),(8, 15, 17),(7, 24, 25),
	(20, 21, 29),(12, 35, 37),(9, 40, 41),(28, 45, 53),
	(11, 60, 61),(16, 63, 65),(33, 56, 65),(48, 55, 73),
	(13, 84, 85),(36, 77, 85),(39, 80, 89),(65, 72, 97),
	(20, 99, 101),(60, 91, 109),(15, 112, 113),(44, 117, 125),
	(88, 105, 137),(17, 144, 145),(24, 143, 145),(51, 140, 149), 
	(85, 132, 157),(119, 120, 169),(52, 165, 173),(19, 180, 181),
	(57, 176, 185),(104, 153, 185),(95, 168, 193),(28, 195, 197),
	(84, 187, 205),(133, 156, 205),(21, 220, 221),(140, 171, 221),
	(60, 221, 229),(105, 208, 233),(120, 209, 241),(32, 255, 257),
	(23, 264, 265),(96, 247, 265),(69, 260, 269),(115, 252, 277),
	(160, 231, 281),(161, 240, 289),(68, 285, 293)]

def main(args):
	triples = set()
	limit = 10000	# 10000 => 9 seconds

	for m in range(2, limit):
		for n in range(1, m):
			a = m*m - n*n
			b = 2*m*n
			c = m*m + n*n
			if c >= limit:
				continue
			# scale primitive triple to get all multiples
			k = 1
			while k*c < limit:
				triples.add(tuple(sorted((k*a, k*b, k*c))))
				k += 1

	# Print sorted triples
	triples = sorted(triples)
	# ~ for t in triples:
		# ~ print(t)
	print("Total triples:", len(triples))
	
	# Construct a dictionary which counts the occurrences of an integer
	# Key: integer	Value: count
	database = dict()
	for k in triples:
		for v in k:
			if database.get(v) == None:
				database[v] = 1
			else:
				database[v] += 1

			if v == 75:
				print(k)
				
	print("Database Dictionary Complete")

	# DEBUG EXIT
	exit(0)
	
	"""
		# Database content
		Total triples: 878
		Database Dictionary Complete
		Int: 3  Count: 1
		Int: 4  Count: 1
		Int: 6  Count: 1
		Int: 7  Count: 1
		Int: 11 Count: 1
		Int: 61 Count: 1
		Int: 14 Count: 1
		Int: 113        Count: 1
		
		Sort the database by count,integer
		
	"""
	mnl = [[v,k] for k,v in database.items()]
	mnl = sorted(mnl)
	current = 0
	for kv in mnl:
		if kv[0] == current:
			continue
		else:
			print(f"{kv} -> Q({kv[0]}) = {kv[1]}")
			current = kv[0]
	
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
