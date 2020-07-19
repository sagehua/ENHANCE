#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
闭包：
外部函数返回了内部函数，内部函数引用了外部函数的变量，
把内部函数和其引用的变量合起来称作闭包
"""

# 内部函数f引用了外部函数的变量i
def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()

# 由于调用时i的值为3，因此下面三个打印值均为9，而非1, 4, 9
print(f1())
print(f2())
print(f3())


# 利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
    cnt = [0]
    def counter():
        cnt[0] += 1
        return cnt[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

# 以下的函数就会报错，因为闭包里只有外部函数变量的引用，不会取到外部变量的值
def createCounter():
    cnt = 0
    def counter():
        cnt += 1
        return cnt
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
