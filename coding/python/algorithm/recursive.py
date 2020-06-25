#!/usr/bin/python
# -*- coding: utf8 -*-

def factorial(n):
	if n < 1:
		return 1
	else:
		subSolution = factorial(n - 1)
		solution = subSolution * n
		return solution


def reverse(word):
	if word == "":
		return word
	else:
		subProblem = word[1:]
		subSolution = reverse(subProblem)
		solution = subSolution + word[0]
		return solution


def calcQueens(size):
	board = [-1] * size
	return queens(board, 0, size)

def queens(board, current, size):
	pass

def binary_search(list_data, value):
	"""二分查找
	:param list_data:
	:param value:
	"""
	


if __name__ == '__main__':
	print(factorial(5))
	print(reverse('sagehua'))
