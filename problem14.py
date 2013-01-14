## The following iterative sequence is defined for the set of positive integers:
## 
## n  n/2 (n is even)
## n  3n + 1 (n is odd)
## 
## Using the rule above and starting with 13, we generate the following sequence:
## 
## 13  40  20  10  5  16  8  4  2  1
## It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
## 
## Which starting number, under one million, produces the longest chain?
## 
## NOTE: Once the chain starts the terms are allowed to go above one million.

import sys

cache = {}

def next(n):
	if n % 2 == 0:
		return n / 2
	else:
		return 3 * n + 1

def collatz(n):
	seq = []
	i = n
	while i != 1:
		seq.append(i)
		i = next(i)
	seq.append(1)
	return seq

def search(n):
	record = 0
	record_holder = []
	for i in range(1,n+1):
		seq = collatz(i)
		if len(seq) > record:
			record_holder = seq
			record = len(seq)
	return record_holder

if __name__ == '__main__':
	n = int(sys.argv[1])
	print search(n)
