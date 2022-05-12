import os
dir_list = os.listdir()

imgSrcToSearch = "<img src="
onlyMedia = "/media"
onlyImg="image"

img = ""
imgSrc = ""
dataImg = ""
extension =""

for x in dir_list:
    with open ('{x}'.format(x=x), 'r+', encoding='utf8') as myfile,  open ('#{x}'.format(x=x), 'w',encoding='utf8') as secondFile: 
        for line in myfile:
            
            if line.find(imgSrcToSearch) != -1:

                i = line.find(imgSrcToSearch)
                imgSrc = line[i:i+36]

                if imgSrc.find(onlyMedia) != -1:
                    
                    j = imgSrc.find(onlyMedia)
                    img = imgSrc[j:j+17]

                    if img.find(onlyImg) != -1:
                        k = img.find(onlyImg)
                        dataImg = img[k:k+10]

                        l = dataImg.find(".")
                        extension = dataImg[l+1:l+4]

                        print(f"image: {dataImg}")
                        print(f"extension: {extension}")

                        if dataImg[-1] == "g":
                            secondFile.write("![" + dataImg.rstrip('/n') + "](./images/media/" + dataImg.rstrip('/n') + ")")
                        else:
                            if extension[0] == "p":
                                dataImg = img[k:k+10]#solo funciona para png,si debe ser para jpg se debe poner 11 y quitar el ng 
                                secondFile.write("![" + dataImg.rstrip('/n') + "ng](./images/media/" + dataImg.rstrip('/n') + "ng)")
                            elif extension[:1] == "j":
                                dataImg = img[k:k+10] 
                                secondFile.write("![" + dataImg.rstrip('/n') + "g](./images/media/" + dataImg.rstrip('/n') + "g)")
                            elif extension[:1] == "g":
                                dataImg = img[k:k+9] 
                                secondFile.write("![" + dataImg.rstrip('/n') + "if](./images/media/" + dataImg.rstrip('/n') + "if)")
            else:
                secondFile.write(line.rstrip('/n'))
            