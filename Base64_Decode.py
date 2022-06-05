#python base64_decode.py YWJhY2F4aQ==

import base64
import sys

print 'Base64 Decoded:', base64.b64decode(sys.argv[1])
