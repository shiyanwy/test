import base64
import binascii

with open(r'doc\stego.txt') as fobj:
    lines = fobj.readlines()

for line in lines:
    print(base64.b64decode(line).decode('iso-8859-1'))