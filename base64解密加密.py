import  base64
import binascii

a = 'testzhifuchuan'
b = 'dGVzdHppZnVjaHVhbg=='
print(base64.b64encode(a.encode('utf-8')).decode('utf-8'))
print(base64.b64decode(b.encode('utf-8')).decode('utf-8'))


