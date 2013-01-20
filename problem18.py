#!/usr/bin/env python
## By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
## 
## 3
## 7 4
## 2 4 6
## 8 5 9 3
## 
## That is, 3 + 7 + 4 + 9 = 23.
## 
## Find the maximum total from top to bottom of the triangle below:
## 
## 75
## 95 64
## 17 47 82
## 18 35 87 10
## 20 04 82 47 65
## 19 01 23 75 03 34
## 88 02 77 73 07 63 67
## 99 65 04 28 06 16 70 92
## 41 41 26 56 83 40 80 70 33
## 41 48 72 33 47 32 37 16 94 29
## 53 71 44 65 25 43 91 52 97 51 14
## 70 11 33 28 77 73 17 78 39 68 17 57
## 91 71 52 38 17 14 91 43 58 50 27 29 48
## 63 66 04 68 89 53 67 30 73 16 69 87 40 31
## 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
## 
## NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, 
## Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by 
## brute force, and requires a clever method! ;o)
import sys

class Node:
	def __init__(self, v):
		self.value = v
		self.tree_sum = -1
		self.next_in_path = None

def read_triangle_file(f):
	""" Output will be:
		[ [1, 2, 3],
			[4, 5],
			[6] ]
	"""
	reversed_triangle = []
	for line in f:
		array = [int(x) for x in line.split(' ')]
		reversed_triangle.insert(0, array)
	return reversed_triangle;

def translate_row(line, last_row):
	ret = []
	for i in range(len(line)):
		node = Node(line[i])
		if last_row != None:
			sub_node = None
			if last_row[i].tree_sum >= last_row[i+1].tree_sum:
				sub_node = last_row[i]
			else:
				sub_node = last_row[i+1]
			node.tree_sum = sub_node.tree_sum + node.value
			node.next_in_path = sub_node
		else:
			node.tree_sum = node.value
			node.next_in_path = None
		ret.append(node)
	return ret

def translate_triangle(reversed_triangle):
	ret = []

	last_out = None
	for line in reversed_triangle:
		out_row = translate_row(line, last_out)
		ret.insert(0, out_row)
		last_out = out_row
	return ret

def print_sums(tri):
	for row in tri:
		print [x.tree_sum for x in row]

def max_path(triangle):
	ret = []

	node = triangle[0][0]

	while node != None:
		ret.append(node.value)
		node = node.next_in_path
	return ret

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage: %s <input_file>" % sys.argv[0]
		sys.exit(0)
	input_filename = sys.argv[1]
	triangle = read_triangle_file(open(input_filename))
	triangle = translate_triangle(triangle)

	path = max_path(triangle)
	print_sums(triangle)
	## print path
	## print "Sum: %d" % sum(path)
