import random
import numpy as np
from functools import reduce
from rich import print
from random import randint

"""
if there's an error, does its position look like ..___1?
if there's an error, does its position look like ..__1_?
...
"""

def calc_parity_bits(msg):
    return reduce( lambda x, y: x ^ y, [ i for i, bit in enumerate(msg) if bit ] )

def prepare_block(msg):
    block = msg
    parity_bits = bin(calc_parity_bits(msg))[2:].zfill(int(len(msg)**.5))[::-1]
    for i, bit in enumerate(parity_bits):
        block[2**i] ^= int(bit)

    return block


def transmit_msg(msg, errors=1):
    msg = msg.copy()
    for _ in range(errors):
        r = randint(0, len(msg)-1)
        msg[r] = not msg[r]

    return msg


def generate_msg(size):
    return np.random.randint(2, size=size) 


msg = generate_msg(16)
print("message is", msg, "with random parity", calc_parity_bits(msg))

block = prepare_block(msg)
print("p block is", block, "with actual parity", calc_parity_bits(block))

print("transmitting msg...")
tblock = transmit_msg(block)
print(tblock)
print(np.array_equal(tblock, block))

parity_bits = calc_parity_bits(tblock)
print("correcting message at position", parity_bits)
tblock[parity_bits] = not tblock[parity_bits]
print(tblock)
print(np.array_equal(tblock, block))

# TODO implement extended hamming code

