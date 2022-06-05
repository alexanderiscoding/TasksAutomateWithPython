#python ascii_decode.py 46 46 46 46 32 46 95 32 95 46 95 46 32 95 46 95 32 46 32 46 95 46 32 46 46 46 32 46 32 95 46 95 46 32 95 46 95 46 32 95 32 46 46 95 46

import sys

ASCII_values = [int(arg) for arg in sys.argv[1:]]
ASCII_string = "".join([chr(value) for value in ASCII_values])

print 'Ascii Decoded:', ASCII_string
