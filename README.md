# SFF extractor
![](https://img.shields.io/badge/PYTHON-%233776AB?style=for-the-badge&logo=python&logoColor=white)

SFFv1 and v2 sprites extractor (far from done but working on it)


## SFF Files Headers information

SFFv1 header structure

|type|description|size|identifier|
|:-----------------:|:------------:|:-----:|:----:|
| Char              | signature    | [12]  | 12s  |
| Unsigned char     | verhi        | 2     | B    |
| Unsigned char     | verlo        | 2     | B    |
| Unsigned char     | verlo2       | 2     | B    |
| Unsigned char     | verlo3       | 2     | B    |
| Unsigned long int | nb_groups    | 4     | L    |
| Unsigned long int | nb_imgs      | 4     | L    |
| Unsigned long int | sub_offset   | 4     | L    |
| Unsigned long int | sub_size     | 4     | L    |
| Char              | palette_type | 1     | c    |
| Char              | blank        | [3]   | 3s   |
| Char              | comments     | [476] | 476s |

total size of 512 bytes

    head = f.read(512)
    var = struct.unpack("12sBBBBLLLLc3s476s",head)

SFFv1 sprite node subhead structure

|type|description|size|identifier|
|:------------------:|:-------------:|:----:|:---:|
| unsigned long int  |  next_offset  | 4    | L   |
| unsigned long int  |   length      | 4    | L   |
| short int          |   xcoord      | 2    | h   |
| short int          |   ycoord      | 2    | h   |
| unsigned short int |   group       | 2    | H   |
| unsigned short int |   img         | 2    | H   |
| unsigned short int |   prev        | 2    | H   |
| unsigned char      |  same_pal     | 1    | H   |
| char               | comments      | [13] | 13s |

total size of 32 bytes

    sub = f.read(32)
    var = struct.unpack("LLhhHHHB13s",sub)

SFFv2 header structure

|type|description|size|identifier|
|:-----------------:|:------------:|:-----:|:----:|
| char              | signature    | [12]  | 12s  |
| unsigned char     | verlo3       | 1     | B    |
| unsigned char     | verlo2       | 1     | B    |
| unsigned char     | verlo1       | 1     | B    |
| unsigned char     | verhi        | 1     | B    |
| unsigned long int | reserved1    | 4     | L    |
| unsigned long int | reserved2    | 4     | L    |
| unsigned char     | Compatverlo3 | 1     | B    |
| unsigned char     | Compatverlo2 | 1     | B    |
| unsigned char     | Compatverlo1 | 1     | B    |
| unsigned char     | Compatverhi  | 1     | B    |
| unsigned long int | reserved3    | 4     | L    |
| unsigned long int | reserved4    | 4     | L    |
| unsigned long int | img_off      | 4     | L    |
| unsigned long int | nb_imgs      | 4     | L    |
| unsigned long int | Pal_off      | 4     | L    |
| unsigned long int | nb_pal       | 4     | L    |
| unsigned long int | Ldata_off    | 4     | L    |
| unsigned long int | Ldata_Len    | 4     | L    |
| unsigned long int | Tdata_off    | 4     | L    |
| unsigned long int | Tdata_Len    | 4     | L    |
| unsigned long int | reserved5    | 4     | L    |
| unsigned long int | reserved6    | 4     | L    |
| char              | comments     | [436] | 436s |

total size of 512 bytes

    head = f.read(512)
    var = struct.unpack("12sBBBBLLBBBBLLLLLLLLLLLL436s",head)

SFFv2 sprite node subhead structure

|type|description|size|identifier|
|:------------------:|:------:|:---:|:---:|
| unsigned short int | nb_Grp | 2 | H |
| unsigned short int | nb_spr | 2 | H |
| unsigned short int | Width  | 2 | H |
| unsigned short int | Height | 2 | H |
| short int          | X      | 2 | h |
| short int          | Y      | 2 | h |
| unsigned short int | lnki   | 2 | H |
| unsigned char      | Fmt    | 2 | B |
| unsigned char      | Coldep | 2 | B |
| unsigned long int  | Dt_off | 4 | L |
| unsigned long int  | Dt_len | 4 | L |
| unsigned short int | pali   | 2 | H |
| unsigned short int | Flag   | 2 | H |

total size of 28 bytes

    sub = f.read(28)
    var = struct.unpack("HHHHhhHBBLLHH",sub)

SFFv2 pallete node subhead structure

|type|description|size|identifier|
|:------------------:|:------:|:---:|:---:|
| unsigned short int | ????   | 2 | H |
| unsigned short int | ????   | 2 | H |
| unsigned short int | ????   | 2 | H |
| unsigned short int | ????   | 2 | H |
| unsigned long int  | Dt_off | 4 | L |
| unsigned long int  | Dt_len | 4 | L |

total size of 28 bytes

    pal = f.read(28)
    var = struct.unpack("HHHHLL",pal)
