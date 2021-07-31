from PIL import Image
import os, math

infile = input("Insert input file (ex : C:/Users/myuser/Desktop/) oublie pas le / à la fin ! ") #Input folder
outfile = input("Insert input file (ex : C:/Users/myuser/Desktop/output/) oublie pas le / à la fin !") #Output folder


if(not os.path.isdir(outfile)): #Making output folder if he doesn't exist
    print('Making Output Folder...')
    os.mkdir(outfile)

#Combine 2 .tga images into 1 png
def combineimg(image1,image2):
    img1 = Image.open(image1)
    img2 = Image.open(image2)
    try:
        rgb1 = img1.split() #Split RGB
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


    new_img = Image.merge('RGBA', (rgb2[r],rgb1[0],rgb2[b],rgb1[1])) #Merge RGBA into 1 image
    output_name = os.path.basename(image1)[:-6]
    print(os.path.join(outfile,output_name)+'.png')
    new_img.save(os.path.join(outfile,output_name)+'.png') #Export into png


print("Loading ... ")
for root, dirs, files in os.walk(infile, topdown=False): #Check all the input folder
    for name in files:
        file, ext = os.path.splitext(name)
        if(ext.lower()+"" == ".tga" and file[len(file)-1].lower()+"" == "s"): #Check for tga file
            if(os.path.isfile(infile+file[:-1]+"n"+ext)):
                print("Image en cours de traitement : "+name)
                combineimg(infile+file[:-1]+"n"+ext,name)
                print("+1 Image")

        
