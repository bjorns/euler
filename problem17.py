## If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
## then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
##
## If all the numbers from 1 to 1000 (one thousand) inclusive were written out
## in words, how many letters would be used?
##
## NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and 
## fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import sys

cache = {}
cache[1] = "one"
cache[2] = "two"
cache[3] = "three"
cache[4] = "four"
cache[5] = "five"
cache[6] = "six"
cache[7] = "seven"
cache[8] = "eight"
cache[9] = "nine"
cache[10] = "ten"
cache[11] = "eleven"
cache[12] = "twelve"
cache[13] = "thirteen"
cache[14] = "fourteen"
cache[15] = "fifteen"
cache[16] = "sixteen"
cache[17] = "seventeen"
cache[18] = "eighteen"
cache[19] = "nineteen"
cache[20] = "twenty"
cache[30] = "thirty"
cache[40] = "forty"
cache[50] = "fifty"
cache[60] = "sixty"
cache[70] = "seventy"
cache[80] = "eighty"
cache[90] = "ninety"

def translate(n):
	if n == 0:
		return ""

	s = str(n)
	if len(s) > 3:
		thousands = n / 1000
		return cache[thousands] + " thousand " + translate(n - thousands * 1000)
	if len(s) == 3:
		hundreds = n / 100
		ret = cache[hundreds] + " hundred"
		remainder = n - (hundreds * 100)
		if remainder != 0:
			ret = ret + " and " + translate(n - hundreds * 100)
		return ret
	if len(s) == 2:
		if n <= 20:
			return cache[n]
		single = n % 10
		tens = n - single
		return cache[tens] + translate(single)
	if len(s) == 1:
		return cache[n]

def count(n):
	s = ""
	for i in range(1,n+1):
		t = translate(i)
		print t
		s = s + t
	return length(s)

def length(s):
	return len(s.replace(' ', ''))

if __name__ == '__main__':
	n = int(sys.argv[1])
	print count(n)
	## print "%s (%d)" % (translate(n), length(translate(n)))
