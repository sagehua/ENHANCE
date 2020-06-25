# coding: utf-8
"""
关于函数的进一步理解: namibox中函数的另类操作
jct/utility.amrefresh_cache 中 amrefresh_cache.cache_cmb.get（）
1. cache_cmb属性由namibox/ott/gpub.py 中 jct.utility.amrefresh_cache.cache_cmb = funcc 定义
2. 可以用 function_name.variable = value 的方式将variable设置到函数的作用域里
"""
def test():
    print test.name
    print 'name' in dir(test)


test.name = 'closer'


if __name__ == '__main__':
    test()
