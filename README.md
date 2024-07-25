# str2xor

## About

Tool for finding 2 or more printable strings that XOR to the given string.

## Usage

```txt
  python str2xor.py <string> [-a] [-b] [-n <number>] [-g <groups>] [-s <number>] [-h]
```

## Options

```txt
  -a          : Use all printable characters. The default is alphanumeric characters.
  -b          : Use byte string as output. This will clearly indicate whitespaces.
  -n <number> : Number of combinations to generate. Default is 1.
                  These are not guaranteed to be unique.
  -g <groups> : Split the string every <groups> characters.
                  If the last group is less than <groups> characters, it will be padded with null.
  -s <number> : Amount of strings to be combined. Default is 2.
  -h          : Show this help message
```

## Examples

```txt
$ str2xor.py supercooltext
16DTJ45X82QIG
BC418WZ7TF413
```

```txt
$ str2xor.py supercooltext -a
VZ2K^K0CI,YF<
%/B.,(_,%X<>H
```

```txt
$ str2xor.py supercooltext -n 3
86G6E1XZ8BV42
KC7S7R75T63LF

G363CUX85BT0F
4FFV167WY61H2

6MF2C1Z9Y9SA9
E86W1R5V5M69M
```

```txt
$ str2xor.py supercooltext -n 2 -a -b -g 4 -s 5
b'08V+ \\YM$ UP\\+ ,8_@'
b"-qF' _DZr zDR/ c@>2"
b'Cv8T 17=d b%1Z t2GB'
b']|%u .;/o D;j{ j:K`'
b'p6}H nrj2 e~0] %pmP'

b'L#*. )O7# &@AS G_ZJ'
b"n'gc ;chs )sRM d7&3"
b'y0Kd 3beT Y,9* q8OC'
b"gt2| 5Ju) m#$l i'GK"
b'O5D0 fg B WHk  Owtq'
```
