import hashlib
import base64

# this function will create a hash from the Message
def encrypt_md5(text):
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()


#This is the secret message
secret_text = "We will atack 10 AM on 29th May"

#We need to covert this to a secret
encrypted_text = encrypt_md5(secret_text)
