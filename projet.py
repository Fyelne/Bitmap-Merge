from PIL import Image
import numpy as np
import glob, os, shutil, errno, math

infile = "C:\\Users\\Andy\\Desktop\\Nils\\"
outfile = "C:\\Users\\Andy\\Desktop\\Nils\\output\\"
i = 0
nb_images = 0


if(not os.path.isdir(outfile)):
    print('Making Output Folder...')
    os.mkdir(outfile)


def combineimg(image1,image2):
    img1 = Image.open(image1)
    img2 = Image.open(image2)
    try:
        rgb1 = img1.split()
        rgb2 = img2.split()
    except:
        print("Il n'y a pas assez de canaux couleurs")
    
    r = input("Quel canal voulez vous mettre en R ?").lower()+""
    if("rgb".find(r) == -1):
        r = "rvb".find(r)
    else:
        r = "rgb".find(r)

    b = input("Quel canal voulez vous mettre en B ?").lower()+""
    if("rgb".find(b) == -1):
        b = "rvb".find(b)
    else:
        b = "rgb".find(b)


    new_img = Image.merge('RGBA', (rgb2[r],rgb1[0],rgb2[b],rgb1[1]))
    output_name, ext = os.path.splitext(image1)
    output_name = output_name[:-2]
    print(output_name)
    new_img.save(outfile+output_name+'.png')


print("Loading ... ")
for root, dirs, files in os.walk(infile, topdown=False):
    i +=1
    for name in files:
        file, ext = os.path.splitext(name)
        if(ext.lower()+"" == ".tga" and file[len(file)-1].lower()+"" == "s"):
            if(os.path.isfile(infile+file[:-1]+"n"+ext)):
                combineimg(name,infile+file[:-1]+"n"+ext)
                print("+1 Image")

        