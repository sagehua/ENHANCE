# coding: utf8
import logging
"""
常用的Handler: StreamHandler, FileHandler, SMTPHandler
FileHandler又包括: RotatingFileHandler, TimedRotatingFileHandler
"""

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.ERROR)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create handler
ch = logging.StreamHandler()
ch.setLevel(logging.CRITICAL)
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# use of logger
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')