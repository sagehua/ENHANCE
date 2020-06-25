# coding:utf8
"""
日志的配置
1. logger的命名存在继承关系，比如 'foo.bar'是'foo'的子代
2. 父子代logger间可以propagate。如果propagate为True，那么子代logger会传播到父代——不论父代的level，直接调用父代的handler
3. 关于level：每个logger和每个handler都有level
"""
import os
import logging.config


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(module)s %(lineno)d %(name)s %(message)s',
        },
        'standard': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'simple': {
            'format': '%(message)s'
        },
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'console_simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': BASE_DIR + '/logs/application.log',
            'maxBytes': 1024 * 1024 * 5,  # 一个日志文件最多 5 MB
            'backupCount': 3,  # 最多有3个备份文件（即最多有4个日志文件）
            'encoding': 'utf-8'
        },
    },
    'loggers': {
        'logger1': {
            'level': 'ERROR',
            'handlers': ['console_simple'],
            'propagate': False
        },
        'logger1.descendant': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': True
        },
        # 默认的配置（名字不在loggers字典里的logger，默认名字为空字符串；名字在loggers字典里且propagate为True的logger也会扩散到这里）
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False
        }
    }
}
logging.config.dictConfig(LOGGING)
