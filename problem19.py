#!/usr/bin/env python
## You are given the following information, but you may prefer to do some research for yourself.
## 
## 1 Jan 1900 was a Monday.
## Thirty days has September,
## April, June and November.
## All the rest have thirty-one,
## Saving February alone,
## Which has twenty-eight, rain or shine.
## And on leap years, twenty-nine.
## A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
##
## How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import sys

FEBRUARY = 2

days_in_month_map = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year):
	if year % 100 == 0:
		return year % 400 == 0
	else:
		return year % 4 == 0

def rotate(i, out_of):
	""" Increase day or month modulo but start at one instead of 0. """
	return ((i-1) % out_of) + 1

def days_in_month(date):
	day, month, year = date
	if month == FEBRUARY and leap_year(year):
		return 29
	else:
		return days_in_month_map[month]

def next_sunday(date):
	(day, month, year) = date

	ret_day = rotate(day + 7, days_in_month(date))

	ret_month = month
	if ret_day < day:
		ret_month = month + 1
	ret_month = rotate(ret_month, 12)

	ret_year = year
	if ret_month < month:
		ret_year = year + 1
		
	return (ret_day, ret_month, ret_year)

if __name__ == '__main__':
	results = []

	SUNDAY = (31, 12, 1899)
	year = 1899
	s = SUNDAY
	while year < 2001:
		s = next_sunday(s)
		(day, month, year) = s
		if (day == 1 and year >= 1901):
			results.append(s)
	print len(results)
