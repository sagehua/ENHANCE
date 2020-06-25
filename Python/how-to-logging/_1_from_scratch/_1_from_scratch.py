# coding: utf8
import logging
"""
1. 日志的名称
默认的名称是root

2. 日志的级别：
日志的严重程度有五个级别：DEBUG, INFO, WARNING, ERROR, CRITICAL
默认的级别是WARNING

3. 日志的目的地
日志可以输出到控制台、文件、电子邮件等地方
默认的目的地是StreamHandler, 即sys.stderr

4. 日志的输出格式
日志的输出格式的格式化字符串有：%(asctime)s, %(name)s, %(levelname)s, %(message)s, ...
"""

# 日志配置
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# 日志书写
logging.debug('this message will not appear.')
logging.info('i am a info message.')
