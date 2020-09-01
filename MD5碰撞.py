import hashlib
import binascii
import _thread

captcha = 'b2ee32'
i = 0
for i in range(0, 2**32):
    str_hex = str(hex(i)).replace('0x', '')
    if len(str_hex) % 2 > 0:
        str_hex = str_hex.zfill((len(str_hex) + 1))
    # 逐个字符拼接
    s = ''.join(chr(int(str_hex[k:k+2], 16)) for k in range(0, len(str_hex), 2))
    # binascii用法
    # s = binascii.unhexlify(str_hex)
    s_md5 = hashlib.md5(s.encode()).hexdigest()[0:6]
    if s_md5 == captcha:
        print(i, s, s_md5)
        break
