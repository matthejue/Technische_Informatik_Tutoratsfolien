#!/usr/bin/env python

LENGTH = 4
NUM_DEICMAL_BITS = 2
NUM_BITS = 4


def value_1s_complement(bits):
    acc = 0
    i = -1
    for i, ai in enumerate(map(lambda bit: int(bit), reversed(bits[1:]))):
        acc += ai * 2 ** (i - NUM_DEICMAL_BITS)
    return acc - int(bits[0]) * (2 ** (i + 1 - NUM_DEICMAL_BITS) - 2**-2)


def value_2s_complement(bits):
    acc = 0
    i = -1
    for i, ai in enumerate(map(lambda bit: int(bit), reversed(bits[1:]))):
        acc += ai * 2 ** (i - NUM_DEICMAL_BITS)
    return acc - int(bits[0]) * 2 ** (i + 1 - NUM_DEICMAL_BITS)


if __name__ == "__main__":
    print("{", end="")
    i = 0
    while i < 2**NUM_BITS:
        bits = str(bin(i))[2:]
        bits = "0" * (LENGTH - len(bits)) + bits
        print(bits, end="|->(")
        print(value_1s_complement(bits), end=", ")
        print(value_2s_complement(bits), end=")")
        i += 1
        if i != 2**NUM_BITS:
            print(", ", end="")
    print("}", end="")