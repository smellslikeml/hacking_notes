#!/usr/bin/env python from PIL import Image
from PIL import Image

def Set_LSB(value, bit):
    if bit == '0':
        value = value & 254
    else:
        value = value | 1
    return value

def Hide_message(carrier, message, outfile):
    message += chr(0)
    c_image = Image.open(carrier)
    c_image = c_image.convert('RGBA')

    out = Image.new(c_image.mode, c_image.size)
    pixel_list = list(c_image.getdata())
    new_array = []

    for i in range(len(message)):
        char_int = ord(message[i])
        cb = str(bin(char_int))[2:].zfill(8)
        pix1 = pixel_list[i*2]
        pix2 = pixel_list[(i*2) + 1]
        newpix1 = []
        newpix2 = []
        for j in range(0,4):
            newpix1.append(Set_LSB(pix1[j], cb[j]))
            newpix2.append(Set_LSB(pix2[j], cb[j+4]))
        new_array.append(tuple(newpix1))
        new_array.append(tuple(newpix2))
    new_array.extend(pixel_list[len(message)*2:])
    out.putdata(new_array)
    out.save(outfile)
    print('steg image saved to ' + outfile)


def get_pixel_pairs(iterable):
    a = iter(iterable)
    return zip(a, a)

def get_LSB(value):
    if value & 1 == 0:
        return '0'
    else:
        return '1'

def extract_message(carrier):
    c_image = Image.open(carrier)
    pixel_list = list(c_image.getdata())
    message = ""

    for pix1, pix2 in get_pixel_pairs(pixel_list):
        message_byte = '0b'
        for p in pix1:
            message_byte += get_LSB(p)

        for p in pix2:
            message_byte += get_LSB(p)

        if message_byte == '0b00000000':
            break

        message += chr(int(message_byte, 2))
    return message


if __name__ == '__main__':
    Hide_message('/home/funk/Downloads/image.png', 'my hidden msg', 'tst.png')
    print(extract_message('tst.png'))

































