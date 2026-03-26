#!/usr/bin/env python3
#
#  src1.py
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
def pythagorean_triples_with_side(a):
    """
    Return all Pythagorean triples (a, b, c) containing the given side 'a'.
    Results are returned as sorted tuples (smallest first).
    """
    triples = []
    a2 = a * a

    # Loop through all divisors of a^2
    for u in range(1, int(a2**0.5) + 1):
        if a2 % u == 0:
            v = a2 // u

            # u and v must have same parity for b,c to be integers
            if (u + v) % 2 == 0:
                b = (v - u) // 2
                c = (v + u) // 2

                if b > 0:
                    triple = tuple(sorted((a, b, c)))
                    triples.append(triple)

    # Remove duplicates and sort
    return sorted(set(triples))


def main(args):
	print(pythagorean_triples_with_side(15))
	return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
