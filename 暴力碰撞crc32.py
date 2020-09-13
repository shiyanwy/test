import zlib

# 模拟 一串流的crc校验码为crc1，6162636465666768696a6b6c6d6e ======> 0x400d9578
a = bytes('abcdefghijklmn',encoding='utf-8')
crc1 = zlib.crc32(a)
print(a.hex()+" ======> "+hex(crc1))

# 串流中2字节的数据被纂改，CRC_ORI为修改前的正确校验码。
# 循环拼接字符串生成校验码，如果生成的CRC_RES与CRC_ORI一致，则为被纂改前的正确数据。
a1,a2 = '61626364656667','6a6b6c6d6e'
crc_ori = 0x400d9578

for i in range(0,0xffff):
    s1 = a1 + format(i,'x').zfill(4) + a2
    s2 = bytes.fromhex(s1)
    crc_res = zlib.crc32(s2)
    if crc_res == crc_ori :
        print(format(i,'x').zfill(8))
        break




