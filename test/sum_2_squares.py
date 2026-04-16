
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
    for q in range(101):
        pairs = sum_two_squares_fast(q*q)
        if((len(pairs)>1)and(True)):
            print(q,pairs)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
