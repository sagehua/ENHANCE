# coding: utf-8

# - 哈希算法
#   - md5: message-digest algorithm 5
#   - SHA: secure hash algorithm: sha-1, sha-224, sha-256, sha-384, sha-512

import hashlib

# 创建一个哈希对象
m = hashlib.md5()  # 或者hashlib.sha1(), hashlib.sha224(), ...

# 给这个哈希对象填充字符串 
m.update('sagehua')  # 在python3中为m.update(b'sagehua')

# 获取字符串的摘要
m.hexdigest()