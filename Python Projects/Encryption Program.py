#Encryption Program
import random
import string

def generate_key():
    """
    Generates a shuffled key for encryption based on the set of characters.
    Returns the character set and shuffled key as lists.
    """
    # Define the characters to be used and create a shuffled key
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def encrypt_message(plain_text, chars, key):
    """
    Encrypts a message using a substitution cipher with a shuffled key.
    """
    cipher_text = ""
    for letter in plain_text:
        # Find the index of the letter in the original characters list and substitute it
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

def decrypt_message(cipher_text, chars, key):
    """
    Decrypts a message encrypted with a substitution cipher using the provided key.
    """
    plain_text = ""
    for letter in cipher_text:
        # Find the index of the letter in the key and map it back to the original characters
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

# Generate character set and key
chars, key = generate_key()

# Display character set and shuffled key (for demonstration)
print(f"chars: {chars}")
print(f"key  : {key}")

# Encrypt message
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt_message(plain_text, chars, key)
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt message
cipher_text = input("Enter a message to decrypt: ")
plain_text = decrypt_message(cipher_text, chars, key)
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")