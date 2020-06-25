# -*- coding: utf-8 -*-
"""
RSA加密算法可以用来加解密以及验签：公钥加密/验签，私钥解密/签名
"""


import os
from base64 import b64encode, b64decode

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256


# 导入公钥和私钥
public_key_path = os.path.join(os.path.dirname(__file__), "keys", "huawei_public_key.pem")
private_key_path = os.path.join(os.path.dirname(__file__), "keys", "pkcs8_rsa_private_key.pem")
with open(private_key_path, 'rb') as f: private_key = RSA.importKey(f.read())
with open(public_key_path, 'rb') as f: public_key = RSA.importKey(f.read())

# RSA签名
signer = PKCS1_v1_5.new(private_key)
signature = signer.sign(SHA256.new('this_is_the_data_to_be_send'))
final_sign = b64encode(signature).decode("utf8").replace("\n", "")

# RSA验签
signer = PKCS1_v1_5.new(public_key)
is_valid = signer.verify(SHA256.new('this_is_the_data_to_be_send'), b64decode(final_sign.encode("utf8")))
print is_valid
