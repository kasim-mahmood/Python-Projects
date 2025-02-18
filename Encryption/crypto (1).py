import hashlib
import base64

# this function will create a hash from the Message
def encrypt_md5(text):
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()

def encrypt_sha1(text):
    sha1_hash = hashlib.sha1(text.encode())
    return sha1_hash.hexdigest()


#This is the secret message
secret_text = "We will atack 10 AM on 29th May"

#We need to covert this to a secret
encrypted_text = encrypt_md5(secret_text)
encrypted_text_sha = encrypt_sha1(secret_text)

#let's print
print(f"Secret Code md5: {encrypted_text}")
print(f"Secret Code sh1: {encrypted_text_sha}")

def encrypt_md5(text):
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()

def encrypt_sha1(text):
    sha1_hash = hashlib.sha1(text.encode())
    return sha1_hash.hexdigest()

encrypted_text = encrypt_md5(secret_text)
encrypted_text_sha = encrypt_sha1(secret_text)

#let's print
print(f"Secret Code md5: {encrypted_text}")
print(f"Secret Code sh1: {encrypted_text_sha}")





