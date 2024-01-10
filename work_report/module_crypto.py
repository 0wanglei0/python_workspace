import hashlib
import os

from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

# 多个相同依赖无法识别，当前使用的依赖是pycryptodome
# "https://blog.csdn.net/miffy2017may/article/details/107546033"
# .\pip.exe install pycryptodome


def md5_encrypt(origin_string):
    """ 使用md5加密 不能解"""
    md5 = hashlib.md5()
    md5.update(origin_string.encode('utf-8'))
    return md5.hexdigest()


def base64_encode(origin_string):
    return base64.b64encode(origin_string.encode("utf-8"))


def base64_decode(encode_string):
    return base64.b64decode(encode_string.decode("utf-8"))


def aes_encrypt(text, key="0123456789ABCDEF"):
    """
    AES加密函数
    :param key: 密钥
    :param text: 待加密文本
    :return: base64编码后的密文
    """
    iv = os.urandom(16)  # 生成16位随机向量
    key = bytes(key, encoding='utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pad = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    # 先进行填充
    encrypted_text = cipher.encrypt(pad(text).encode())
    # 将加密后的密文和向量使用base64编码后返回
    return base64.b64encode(encrypted_text + iv).decode()


def aes_decrypt(text, key="0123456789ABCDEF"):
    """
    AES解密函数
    :param key: 密钥
    :param text: 待解密密文
    :return: 解密后的文本
    """
    # 先进行base64解码
    text = base64.b64decode(text.encode())
    iv = text[-16:]  # 先取出向量
    key = bytes(key, encoding='utf-8')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 进行解密并去掉填充的字符
    unpad = lambda s: s[0:-s[-1]]
    return unpad(cipher.decrypt(text[:-16])).decode("utf-8")


def generate_key():
    """
    RSA密钥生成函数，生成1024位密钥对
    :return: 公钥和私钥
    """
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key


def rsa_encrypt(public_key, text):
    """
    RSA加密函数
    :param public_key: 公钥
    :param text: 待加密文本
    :return: base64编码后的密文
    """
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    # 进行加密并返回base64编码的密文
    return base64.b64encode(cipher.encrypt(text.encode())).decode()


def rsa_decrypt(private_key, text):
    """
    RSA解密函数
    :param private_key: 私钥
    :param text: 待解密密文
    :return: 解密后的文本
    """
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    # 先进行base64解码
    text = base64.b64decode(text.encode())
    # 进行解密并返回解密后的文本
    return cipher.decrypt(text, None).decode()


def test_func():
    # encode = aes_encrypt("hello world 6\--\@")
    # decode = aes_decrypt(encode)
    # print(encode)
    # print(decode)

    public_key, private_key = generate_key()
    # print('公钥:', public_key)
    # print('私钥:', private_key)

    text = "hello world --- @"
    # 进行加密
    encrypted_text = rsa_encrypt(public_key, text)
    print('加密后的密文:', encrypted_text)

    # 进行解密
    decrypted_text = rsa_decrypt(private_key, encrypted_text)
    print('解密后的文本:', decrypted_text)


# test_func()
