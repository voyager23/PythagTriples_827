#!/usr/bin/env python3
#
#  triples.py
#  
#  Copyright 2026 mike <mike@fedora.home>

import sys
import math
import itertools as it

triples = set()
limit = 1000

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
for t in triples:
    print(t)

print("Total triples:", len(triples))
