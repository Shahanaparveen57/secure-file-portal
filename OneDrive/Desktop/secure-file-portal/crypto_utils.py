from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
from dotenv import load_dotenv

load_dotenv()
key_env = os.getenv("AES_KEY")
if not key_env:
    raise ValueError("AES_KEY not found in .env file!")
KEY = key_env.encode()

def pad(data):
    padding_len = 16 - len(data) % 16
    return data + bytes([padding_len]) * padding_len

def unpad(data):
    padding_len = data[-1]
    return data[:-padding_len]

def encrypt_file(file_path, dest_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    data = pad(data)
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(data)
    with open(dest_path, 'wb') as f:
        f.write(iv + encrypted)  # prepend IV

def decrypt_file(file_path, dest_path):
    with open(file_path, 'rb') as f:
        raw = f.read()
    iv = raw[:16]
    encrypted = raw[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted))
    with open(dest_path, 'wb') as f:
        f.write(decrypted)
