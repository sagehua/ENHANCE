from multiprocessing import Pool  # 进程池
from multiprocessing.pool import ThreadPool  # 线程池
from time import sleep
import threading
import time


def apply(*args, **kwargs):
    print(args, kwargs)
    sleep(kwargs['a'])
    t = threading.currentThread()
    print('Thread name : %s' % t.getName(), t.ident)
    return str(kwargs)


if __name__ == '__main__':
    time_start = time.time()
    pool = ThreadPool(4)  # 这里的TheadPool换成Pool就是进程池，其它代码不用动
    result1 = pool.apply_async(apply, args=(1, 2), kwds={'a': 1})
    result2 = pool.apply_async(apply, args=(1, 2), kwds={'a': 2})
    result3 = pool.apply_async(apply, args=(1, 2), kwds={'a': 3})
    result4 = pool.apply_async(apply, args=(1, 2), kwds={'a': 4})
    pool.close()  # 停止往线程池添加任务
    pool.join()  # 主线程等待子线程结束
    print(result1.get())
    print(result2.get())
    print(result3.get())
    print(result4.get())
    print(time.time() - time_start)
