# coding:utf8
"""
日志的使用
1. 创建logger
2. 使用logger写日志
"""
import log_conf  # 导入配置文件
import logging


print(1)
logger1 = logging.getLogger('logger1')
logger1.error('first')
print(2)
logger2 = logging.getLogger('logger1.descendant')
logger2.warning('second')
print(3)
logger3 = logging.getLogger('others_logger')
logger3.error('third')
