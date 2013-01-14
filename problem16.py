## Starting in the top left corner of a 22 grid, there are 6 routes (without backtracking) to the bottom right corner.
##
## How many routes are there through a 2020 grid?

import sys

def sum(n):
	string = str(n)
	sum = 0
	for c in string:
		sum = sum + int(c)
	return sum

def run(n):
	x = 1
	for i in range(n):
		print "The number sum of 2^%d(%d) is %d" % (i, x, sum(x))
		x = x << 1

if __name__ == '__main__':
	n = int(sys.argv[1])
	run(n)
