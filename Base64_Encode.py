#python base64_encode.py hacker

import base64
import sys

print 'Base64 Encoded:', base64.b64encode(sys.argv[1])
