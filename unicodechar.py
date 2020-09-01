import binascii
# str.encode() -> bytes()
# bytes.decode() -> str

#汉字的unicode、utf-8编码示例
a = "北"
b = "e58c97"
c = "\xe5\x8c\x97"
d = b"\u1f001\u1f002\u1f003\u1f004\u1f005\u1f006\u1f007"
print(a.encode("utf-8"))                  #汉字utf-8实现 相当于bytes(a,encoding="utf-8"))
print(a.encode("unicode_escape"))         #汉字unicode编码
print(bytes(b,encoding=("utf-8")))
#print(binascii.unhexlify(b).decode())     #十六进制格式的字符串转换为对应二进制流,再按utf-8解码
#print(decode('unicode_escape'))

#print(d.decode('unicode_escape'))

#16进制字符转换示例
#e = '\xe6\x82\xa8\xe7\x9a\x84\xe6\xb5\x8f\xe8\xa7\x88\xe5\x99\xa8\xe8\xa2\xab\xe7\xa6\x81\xe7\x94\xa8\xef\xbc\x8c\xe9\x9c\x80\xe5\xbc\x80\xe5\x90\xaf\xe5\x90\x8e\xe4\xbd\x93\xe9\xaa\x8c\xe5\xae\x8c\xe6\x95\xb4\xe5'