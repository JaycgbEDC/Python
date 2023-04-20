""" 对称密钥密码算法-AES """
import string
import random
from Crypto.Cipher import AES


def generate_key(length):
    """ 生成指定长度的AES密钥 """
    if length not in (16, 24, 32):  # 生成的密钥长度为128/192/256b中的任意一个
        return None
    x = string.ascii_letters + string.digits
    return ''.join([random.choice(x) for _ in range(length)])


def aes_encrypt(key, mode, text):
    """ 使用指定密钥和模式对给定信息加密 """
    encryptor = AES.new(key, mode, b'0000000000000000')  # 最后一个参数是偏移量iv
    return encryptor.encrypt(text)


def aes_decrypt(key, mode, text):
    """ 使用指定密钥和模式对给定信息解密 """
    decryptor = AES.new(key, mode, b'0000000000000000')
    return decryptor.decrypt(text)


def text_process(text):
    """ text明文必须是字节串形式，且长度为16的倍数 """
    text_encoded = text.encode()
    text_length = len(text_encoded)
    padding_length = 16 - text_length % 16
    text_encoded += b'0' * padding_length
    return text_encoded


if __name__ == '__main__':
    text = 'i love you 周杰伦'
    text_encoded = text_process(text)
    key = generate_key(16)
    mode = random.choice((AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB))  # 随机选择AES的模式
    if not key:
        print('Something is wrong.')
    else:
        print(f'key: {key}')
        print(f'mode: {mode}')
        print(f'Before encryption: {text}')
        text_encrypted = aes_encrypt(key.encode(), mode, text_encoded)
        print(f'After encryption: {text_encrypted}')
        text_decrypted = aes_decrypt(key.encode(), mode, text_encrypted)
        print(f'After decrypted: {text_decrypted.decode()}')