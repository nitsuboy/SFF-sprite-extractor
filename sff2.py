import struct
from PIL import Image
import io

"""
sff

 char signature [12]              0 12s
 unsigned char verhi:8            1 B
 unsigned char verlo:8            2 B
 unsigned char verlo2:8           3 B
 unsigned char verlo3:8           4 B
 unsigned long int nb_groups:32   5 L
 unsigned long int nb_imgs:32     6 L
 unsigned long int sub_offset:32  7 L
 unsigned long int sub_size:32    8 L
 char palette_type:8              9 c
 char blank [3]                  10 3s
 char comments [476]             11 476s
 sff_head;

head = f.read(512)
var = struct.unpack("12sBBBBLLLLc3s476s",head)

 unsigned long int next_offset:32 0 L
 unsigned long int length:32      1 L
 short int xcoord:16              2 h
 short int ycoord:16              3 h
 unsigned short int group:16      4 H
 unsigned short int img:16        5 H
 unsigned short int prev:16       6 H
 unsigned char same_pal:8         7 H
 char comments [13]               8 13s
 sff_subhead 

sub = f.read(32)
var = struct.unpack("LLhhHHHB13s",sub)

sffv2

 char signature [12]              0 12s
 unsigned char verlo3:8           1 B
 unsigned char verlo2:8           2 B
 unsigned char verlo1:8           3 B
 unsigned char verhi:8            4 B
 unsigned long int reserved1:32   5 L
 unsigned long int reserved2:32   6 L
 unsigned char Compatverlo3:8     7 B
 unsigned char Compatverlo2:8     8 B
 unsigned char Compatverlo1:8     9 B
 unsigned char Compatverhi:8     10 B
 unsigned long int reserved3:32  11 L
 unsigned long int reserved4:32  12 L
 unsigned long int img_off:32    13 L
 unsigned long int nb_imgs:32    14 L
 unsigned long int Pal_off:32    15 L
 unsigned long int nb_pal:32     16 L
 unsigned long int Ldata_off:32  17 L
 unsigned long int Ldata_Len:32  18 L
 unsigned long int Tdata_off:32  19 L
 unsigned long int Tdata_Len:32  20 L
 unsigned long int reserved5:32  21 L
 unsigned long int reserved6:32  21 L
 char comments [436]             22 436s
 sffv2_head;

head = f.read(512)
var = struct.unpack("12sBBBBLLBBBBLLLLLLLLLLLL436s",head)

 unsigned short int nb_Grp        0 H
 unsigned short int nb_spr        1 H
 unsigned short int Width         2 H
 unsigned short int Height        3 H
 short int X                      4 h
 short int Y                      5 h
 unsigned short int lnki          6 H
 unsigned char Fmt                7 B
 unsigned char Coldep             8 B
 unsigned long int Dt_off         9 L
 unsigned long int Dt_len        10 L
 unsigned short int pali         11 H
 unsigned short int Flag         12 H
 sffv2_subhead;

sub = f.read(28)
var = struct.unpack("HHHHhhHBBLLHH",sub)

 unsigned short int               0 H
 unsigned short int               1 H
 unsigned short int               2 H
 unsigned short int               3 H
 unsigned long int                4 L
 unsigned long int                5 L
 sffv2_pal

pal = f.read(28)
var = struct.unpack("HHHHLL",pal)

"""

def RLE8_Decode(dstlen, src):
    dstpos = 0
    srcpos = 4
    len_ = len(src)
    dst = bytearray(dstlen)

    while srcpos < len_:
        if (src[srcpos] & 0xC0) == 0x40:
            for run in range(src[srcpos] & 0x3F):
                dst[dstpos] = src[srcpos + 1]
                dstpos += 1
            srcpos += 2
        else:
            dst[dstpos] = src[srcpos]
            dstpos += 1
            srcpos += 1

    return dst

def get_pal(header,file,index):
    file.seek(header[15],0)

    for i in range(0,index + 1):
        pal = file.read(16)
        var = struct.unpack("HHHHLL",pal)

    file.seek(var[4] + header[17],0)

    p = []
    aux = 0
    while True :
        p.append(struct.unpack("B",file.read(1))[0])
        aux+=1
        if aux >= var[5]:
            break
    return p

def get_spr(header,file,index):
    file.seek(header[13],0)

    for i in range(0,index+1):
        sub = file.read(28)
        var = struct.unpack("HHHHhhHBBLLHH",sub)
    print(var)

    file.seek(var[9] + header[17],0)

    imgdt = file.read(var[10])

    ft = open("view","wb")
    ft.write(RLE8_Decode(var[2]*var[3],imgdt))
    ft.close()

    img = Image.open(io.BytesIO(imgdt))
    img.putpalette(get_pal(header,file,var[11]),rawmode="RGBA")

    return img


def extractsffv2():

    f = open("chars\gigachadRyu\Sprite.sff", "rb")

    head = struct.unpack("12sBBBBLLBBBBLLLLLLLLLLLL436s",f.read(512))
    print(head[18])
    print(head[20])

    get_spr(head,f,70).show()

extractsffv2()