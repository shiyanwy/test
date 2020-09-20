# 打开并读取文件里的字符串
with open(r'doc\stego.txt') as f:
    s = f.read()
res = ""

# 循环字符串里的每个字符，判断是否为数字
for char in s:
    if char.isdigit():
        res += char
print(res)