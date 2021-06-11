import random
import numpy as np
from functools import reduce
from rich import print

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



def generate_msg(size):
    return np.random.randint(2, size=size) 


msg = generate_msg(16)
print("message is", msg, "with random parity", calc_parity_bits(msg))

block = prepare_block(msg)
print("p block is", block, "with actual parity", calc_parity_bits(block))


