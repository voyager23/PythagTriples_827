
import sys
import math

def sum_two_squares_fast(n):
    pairs = []
    x = 0
    y = int(math.isqrt(n))

    while x <= y:
        s = x*x + y*y
        if s == n:
            pairs.append((x, y))
            x += 1
            y -= 1
        elif s < n:
            x += 1
        else:
            y -= 1
    return pairs

def main(args):
	while(True):
		q = input("Input query integer: ")
		if(q == ""):
			break
		q = int(q)
		pairs = sum_two_squares_fast(q)
		#print any useful pairs
		print(q,end=" ")
		for p in pairs:
			if(p[0] == 0):
				print(p,end=" ")
			else:
				print(p,end=" ")
		print()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
