# coding:utf-8
"""
关于configobj的文档：http://www.voidspace.org.uk/python/configobj.html
configobj是第三方模块：pip install configobj; import configobj
ConfigParser是标准库模块：import ConfigParser
"""
import configobj
import pprint


config = configobj.ConfigObj('mp_login.ini')
print
pprint.pprint(dict(config), indent=4)
print config['SECTION_ALLOWED_USER_CHANNEL']['ITEMS']
print config['SECTION_ALLOWED_USER_CHANNEL_WITH_CODE']['ITEMS'].keys()
