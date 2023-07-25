import struct
from PIL import Image
import io
import numpy as np
import os

"""
typedef struct
{
 char signature [12];             0
 unsigned char verhi:8;           1
 unsigned char verlo:8;           2
 unsigned char verlo2:8;          3
 unsigned char verlo3:8;          4
 unsigned long int nb_groups:32;  5
 unsigned long int nb_imgs:32;    6
 unsigned long int sub_offset:32; 7
 unsigned long int sub_size:32;   8
 char palette_type;               9
 char blank [3];                 10
 char comments [476];            11
} sff_head;
typedef struct
{
 unsigned long int next_offset:32;0
 unsigned long int length:32;     1
 short int xcoord:16;             2
 short int ycoord:16;             3
 unsigned short int group:16;     4
 unsigned short int img:16;       5
 unsigned short int prev:16;      6
 unsigned char same_pal:8;        7
 char comments [13];              8
} sff_subhead;
"""

res = []

def yeah():
    res = []
    # Iterate directory
    for path in os.listdir('chars'):
        if not os.path.isfile(os.path.join('chars', path)):
            res.append(path)
    return res

def yeahsff(folder):
    res = ""
    for path in os.listdir("chars\\"+ folder):
        if str(path[-3:]).capitalize() == "sff".capitalize():
            res = os.path.join("chars\\"+folder, path)
    return res

def makeprofile(folder):
    f = open(yeahsff(folder), "rb")
    head = f.read(512)
    var = struct.unpack("12sBBBBLLLLc3s476s",head)

    groups = [9000]
    try:
        sub = f.read(32)
        var = struct.unpack("LLhhHHHB13s",sub)
        print(var)
        print("group = "+ str(var[4]))
    except:
        print("group not found")

    while not var[4] in groups:
        try:
            sub = f.read(32)
            var = struct.unpack("LLhhHHHB13s",sub)
            if not var[4] in groups:
                f.read(var[1])
            print("group = "+ str(var[4]))
        except:
            print("group not found")
            break

    for im in range (0,1):
        if im != 0:
            try:
                sub = f.read(32)
                var = struct.unpack("LLhhHHHB13s",sub)
                print(var)
                print("group for 1 = "+ str(var[4]))
            except:
                print("group not found")
        ft = open("ve","wb")
        ft.write(f.read(var[1]))
        ft.close
    """
        try:
            img = Image.open(io.BytesIO(f.read(var[1])))
            try:
                back = img.getpalette()[:3]
            except:
                print("no pallete")
                back = [255,0,255]

            img = img.convert("RGBA")

            data = np.array(img)
            red, green, blue, alpha = data.T
            background = (red == back[0]) & (blue == back[2]) & (green == back[1])
            data[...][background.T] = (0, 0, 0, 0)

            img = Image.fromarray(data)

            img.save("images/"+ folder +str(im)+".png","png")
        except:
            print("sla")
    """

res = yeah()


print(res[0])
makeprofile(res[0])