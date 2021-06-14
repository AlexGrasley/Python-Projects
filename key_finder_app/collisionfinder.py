import json
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii
import sys


def check_coll(data1, data2):
    bool = False
    for h in range(0,3):
        if data1[h] == data2[h]:
            bool = True
        else:
            bool = False

    return bool


# set up weak collision check
def weak_collision():

    # original message
    orig_mess = b"messagetext"
    # hash original message
    mes_hash = SHA256.new(data=orig_mess)

    # set up first random hash to check
    rand_bytes = get_random_bytes(16)
    rand_hash = SHA256.new(data=rand_bytes)

    # set up counter
    it_count = 0

    while check_coll(mes_hash.digest(), rand_hash.digest()) == False:
        del rand_hash
        rand_bytes = get_random_bytes(16)
        rand_hash = SHA256.new(data=rand_bytes)
        it_count += 1

    return it_count


# set up string collision
def strong_collision():

    # set up first random hash to check
    rand_bytes1 = get_random_bytes(16)
    rand_hash1 = SHA256.new(data=rand_bytes1)

    # set up 2nd random hash to check
    rand_bytes2 = get_random_bytes(16)
    rand_hash2 = SHA256.new(data=rand_bytes2)

    # set up counter
    it_count = 0

    while check_coll(rand_hash1.digest(), rand_hash2.digest()) == False:
        del rand_hash1
        del rand_hash2
        rand_bytes1 = get_random_bytes(16)
        rand_hash1 = SHA256.new(data=rand_bytes1)
        rand_bytes2 = get_random_bytes(16)
        rand_hash2 = SHA256.new(data=rand_bytes2)
        it_count += 1

    return it_count



if __name__ == '__main__':

    avg_weak_count = 0
    avg_strong_count = 0

    for i in range(0, 1000):
        avg_weak_count += weak_collision()
        avg_strong_count += strong_collision()

    print("Avg Weak Collision Iteration: " + str(avg_weak_count / 1000))
    print("Avg Strong Collision Iteration: " + str(avg_strong_count / 1000))
