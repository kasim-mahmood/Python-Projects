from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key Function
def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Message Encryption Function
def encrypt(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message




if __name__ == "__main__":
    private_key, public_key = generate_keys()

    print(f"Private Key: {private_key}")
    print(f"Public Key: {public_key}")