#python ascii_encode.py .... ._ _._. _._ . ._. ... . _._. _._. _ .._. 

import sys

string = str(sys.argv[1:])

ascii_encoded = [ ord(x) for x in string ]

string_ints = [str(int) for int in ascii_encoded]

ascii_encoded_string = ",".join(string_ints)

print 'Ascii Encoded:', ascii_encoded_string.replace(",", " ")
