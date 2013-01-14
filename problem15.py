## Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
##
## How many routes are there through a 2020 grid?

import sys

def fac(n):
	sum = 1
	while n > 1:
		sum = sum * n
		n = n - 1
	return sum

if __name__ == '__main__':
	n = int(sys.argv[1])
	print fac(2*n)/(fac(n)**2)
