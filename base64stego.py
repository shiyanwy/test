import base64
b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
f = open(r'doc\stego.txt')
bin_str = ''
for line in f.readlines():
    # stegb64 = str(line, "utf-8").strip("\n")
    stegb64 = line.strip("\n")
    # print(stegb64)
    rowb64 = str(base64.b64encode(base64.b64decode(stegb64)), "utf-8")
    # print(rowb64)
    offset = abs(b64chars.index(stegb64.replace('=', '')[-1]) - b64chars.index(rowb64.replace('=', '')[-1]))
    equalnum = stegb64.count('=')  # no equalnum no offset
    if equalnum:
        bin_str += bin(offset)[2:].zfill(equalnum*2)
# bytes_str = bytes.fromhex(bin_str).decode()
# print(bytes(int(bin_str,2)))
# bytes_str = bytes('0b'+bin_str)
print(''.join([chr(int(bin_str[i:i + 8], 2)) for i in range(0, len(bin_str), 8)]))  # 8 位一组
