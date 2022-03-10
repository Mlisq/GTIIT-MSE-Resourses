'''
Homework 1
Write a bmp file using Python. The bmp file should be a 24-bit 8x2 pixels greyscale
image where the left most 2 pixels are completely black, the right most 2 pixels
are completely white and the pixels in the middle change gradually from black to
white. Demonstrate your answer by submitting screen shots of the python script
and the result 8x2 image from your image viewer (enlarged). Note: you must write
the hex version of the last 4 digits of your student ID in the reserved field of the
bmp header.
'''

'''HEADER
---bmp file header---
bfType = 0x4d42                         2bytes
bfSize = 0x00000066                     4bytes
#My student number is 999006125         
bfReserved1 = 0x3d                      2bytes
bfReserved2 = 0x19                      2bytes
bfOffBits = 0x00000036                  4bytes
total                                   14bytes
---bitmap information---
biSzie = 0x00000028 (40bytes)           4bytes
biWidth = width of image                4bytes
biHeight = height of image              4bytes
biPlanes = 0x0001                       2bytes
biBitCount = 0x0018 (24bit)             2bytes
biCompression = 0x00000000              4bytes
biSizeImages = 0x00000000               4bytes
biXPelsPerMeter = 0x00000000            4bytes
biYpelsPerMeter = 0x00000000            4bytes
biClrUsed = 0x00000000                  4bytes
biClrlmportant = 0x00000000             4bytes
total                                   40bytes
'''

'''RGB
3bytes for every pixel (24bit)
EG: 0xffffff ---white
'''

'''
Size of BMP : width * 3 * height +     54
                  RGB size         header size

Notice that if width % 4 != 0, windows system will automatically filled the rest of the line with 0

In this case (8x2) Size of BMP = 2*8*3 + 54 = 102
HEX(102) = 0x66 for 4 bytes = 0x00000066
'''

from array import array

class CreateBMP:

    def __init__(self, width=2, height=8):

        self.w = width
        self.h = height

        self.rgbData = []
        for r in range(self.h):
            self.rgbDataRow = []
            for c in range(self.w):
                self.rgbDataRow.append(0xffffff)
            self.rgbData.append(self.rgbDataRow)

    def calc_data_size (self):
        if(self.w % 4 == 0):
            self.dataSize = self.w * 3 * self.h
        else:
            self.dataSize = self.h * 3 * (self.w + self.w % 4)

        self.fileSize = self.dataSize + 54

    def add2header(self, l, num, len):
        #Learn from the internet. Fast trans into hex.
        tmp = num
        for i in range(len):
            l.append(tmp & 0x000000ff)
            tmp >>= 8

    def gen_bmp_header (self):
        self.calc_data_size()
        self.bmp_header = [0x42, 0x4d]                      #bfType
        self.add2header(self.bmp_header, self.fileSize, 4)  #bfSize
        self.add2header(self.bmp_header, 61, 2)             #bfReserved1
        self.add2header(self.bmp_header, 25, 2)             #bfReserved2
        self.add2header(self.bmp_header, 54, 4)             #bfOffBits
        self.add2header(self.bmp_header, 40, 4)             #biSzie
        self.add2header(self.bmp_header, self.w, 4)         #biWidth
        self.add2header(self.bmp_header, self.h, 4)         #biHeight
        self.add2header(self.bmp_header, 1, 2)              #biPlanes
        self.add2header(self.bmp_header, 24, 2)             #biBitCount
        self.add2header(self.bmp_header, 0, 4)              #biCompression
        self.add2header(self.bmp_header, self.dataSize, 4)  #biSizeImages
        self.add2header(self.bmp_header, 0, 4)              #biXPelsPerMeter
        self.add2header(self.bmp_header, 0, 4)              #biYpelsPerMeter
        self.add2header(self.bmp_header, 0, 4)              #biClrUsed
        self.add2header(self.bmp_header, 0, 4)              #biClrlmportant

   # def paint_point(self, x1, y1, color):
   #     self.rgbData[y1][x1] = color
    
    def paint_Vertical_line(self,x,color):
        for i in range(self.h):
            self.rgbData[i][x] = color

    def save_image(self, name="result.bmp"):
        f = open(name, 'wb')

        f.write(array('B', self.bmp_header).tobytes())

        #zeroBytes = self.dataSize // self.h - self.w * 3    #If width can be divided by 4 This term will be 0
        zeroBytes = self.w % 4

        for r in range(self.h):
            l = []
            for i in range(len(self.rgbData[r])):
                p = self.rgbData[r][i]
                l.append(p & 0x0000ff)                      #RED
                p >>= 8 
                l.append(p & 0x0000ff)                      #GREEN
                p >>= 8
                l.append(p & 0x0000ff)                      #BLUE

            f.write(array('B', l).tobytes())

            for i in range(zeroBytes):                      #Filled with 0 if nessaery
                f.write(bytes([0x00]))

        f.close()

if __name__ == '__main__':
    image = CreateBMP(9, 2)

    image.gen_bmp_header()

    image.paint_Vertical_line(0, 0x000000)

    for i in range(1,7):
        image.paint_Vertical_line(i, int(''+hex(31*i).split('0x')[1]*3,base=16))
    
    image.save_image("result.bmp")