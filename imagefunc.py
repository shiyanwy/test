from PIL import Image
im = Image.open(r'E:\Project\123.png')
# im.show()
pixdata = im.load()
print(im.height,im.width)
print(im.filename)
print(im.format)
print(im.size)
print(im.info)
print(im.getpixel((5,20)))
print(pixdata[5,20][0])
im.close()