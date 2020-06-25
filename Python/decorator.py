# -*- coding: utf-8 -*-
import functools


def log(func):
    """普通装饰器"""
    @functools.wraps(func)  # 确保装饰后的函数名和装饰前一样
    def _wrapper(*args, **kwargs):
        print 'call %s():' % func.__name__
        return func(*args, **kwargs)
    return _wrapper


@log
def now():
    print '2017-7-26'


now()



def logger(text=''):
    """带参数的装饰器"""
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            print '%s %s()' % (text, func.__name__)
            return func(*args, **kwargs)
        return _wrapper
    return _decorator


@logger('DEBUG')
def today():
    print '2019-7-22'

today()
