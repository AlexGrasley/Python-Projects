import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii
import sys


# set up data, original cipher text, and IV
data = b"This is a top secret."

# original ciphertext
ciphertext = "8d20e5056a8d24d0462ce74e4904c1b513e10d1df4a2ef2ad4540fae1ca0aaf9"
# set IV to all 0s
iv = bytearray([b'\0'] * 16)
# import dictionary of words into array
word_file = open("words.txt", "r")
words = []
for line in word_file:
    if len(line.rstrip()) <= 16:
        words.append(line.rstrip())

# loop through words in file trying each as a key
# padded to 16 bytes
for word in words:
    # set the key with the current word
    key = bytes(word)
    # key = pad(key, AES.block_size)
    length_diff = 16 - len(key)
    key += '\x20' * length_diff

    # create cipher and encipher text with new key
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    ct = binascii.hexlify(ct_bytes).decode('utf-8')
    del cipher

    if ct.lower() == ciphertext.lower():
        # we found the key, exit.
        print("The key is: " + key)
        sys.exit()

# got through dictionary and did not find the key
print( "the key could not be found")
sys.exit()


