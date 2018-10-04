from RSA_generater import rsa_generater

def encrypt(msg, encrypt_key, N):
    C = (msg ** encrypt_key) % N
    return C

def decrypt(C, decrypt_key, N):
    msg = (C ** decrypt_key) % N
    return msg

if (__name__ == "__main__"):
    public_key, private_key = rsa_generater(17, 19)
    print("Public key: {}".format(public_key))
    print("Private key: {}".format(private_key))

    msg = 3
    print("\nOriginal message: {}\n".format(msg))
    encrypted_text = encrypt(msg, public_key[1], public_key[0])
    print("Encrypted text: {}".format(encrypted_text))
    decrypted_text = encrypt(encrypted_text, private_key, public_key[0])
    print("Decrypted text: {}".format(decrypted_text))
