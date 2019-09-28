from PIL import Image

#  load a color image
im = Image.open('C:/Users/19845/Desktop/123.jpg' )#当前目录创建picture文件夹

#  convert to grey level image
Lim = im.convert('L' )
Lim.save('pice.jpg' )

#  setup a converting table with constant threshold
threshold = 175
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

# convert to binary image by the table
bim = Lim.point(table, '1' )

bim.save('picf.png' )
