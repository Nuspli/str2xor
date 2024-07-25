#!/usr/bin/python3

import random
import sys

if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 2:
    print("Usage:")
    print(f"  python {sys.argv[0]} <string> [-a] [-b] [-n <number>] [-g <groups>] [-s <number>] [-h]\n")
    print("About:")
    print("  Tool for finding 2 or more printable strings that XOR to the given string.\n")
    print("Options:")
    print("  -a          : Use all printable characters. The default is alphanumeric characters.")
    print("  -b          : Use byte string as output. This will clearly indicate whitespaces.")
    print("  -n <number> : Number of combinations to generate. Default is 1.")
    print("                  These are not guaranteed to be unique.")
    print("  -g <groups> : Split the string every <groups> characters.")
    print("                  If the last group is less than <groups> characters, it will be padded with null.")
    print("  -s <number> : Amount of strings to be combined. Default is 2.")
    print("  -h          : Show this help message.")
    exit()

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
if '-a' in sys.argv:
    alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

num_runs = 1
if '-n' in sys.argv:
    num_runs = int(sys.argv[sys.argv.index('-n')+1])

input = bytearray(sys.argv[1], 'utf-8')

groups = len(input)
if '-g' in sys.argv:
    groups = int(sys.argv[sys.argv.index('-g')+1])
    if len(input) % groups != 0:
        input += b'\x00' * (groups - len(input) % groups)

num_strings = 2
if '-s' in sys.argv:
    num_strings = int(sys.argv[sys.argv.index('-s')+1])

while num_runs > 0:

    strings = [""] * num_strings

    for i in range(len(input)):
 
        target = input[i]

        j = 0
        while j < num_strings-1:
            for b in ''.join(random.sample(alphabet, len(alphabet))):
                if chr(target ^ ord(b)) in alphabet:
                    target = target ^ ord(b)
                    strings[j] += b
                    j += 1
                    break
            else:
                print("nothing")
                exit()

        strings[j] += chr(target)

    if groups != len(input):
        for i in range(num_strings):
            strings[i] = " ".join([strings[i][j:j+groups] for j in range(0, len(strings[i]), groups)])

    if '-b' in sys.argv:
        for s in strings:
            print(bytes(s, 'utf-8'))
    else:
        for s in strings:
            print(s)

    num_runs -= 1
    if num_runs > 0:
        print()
