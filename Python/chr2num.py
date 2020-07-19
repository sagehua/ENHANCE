#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))

def str2float(s):
	integer = s.split('.')[0]
	decimal = s.split('.')[1]
	return reduce(lambda x, y: x * 10 + y, map(str2int, integer)) \
	     + reduce(lambda x, y: x * 10 + y, map(str2int, decimal)) * 0.1 ** len(decimal)

if __name__ == '__main__':
	print(type(str2int('23')), str2int('23'))
	print(type(str2float('23.23')), str2float('23.23'))
