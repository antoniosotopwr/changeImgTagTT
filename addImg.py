
imgSrcToSearch = "<img src="
ruta ="./images/media/"
onlyMedia = "/media"

onlyImg="image"
rutaSaved = ""

img = ""
data = ""
imgSrc = ""

dataImg = ""

info =""

with open ('49.md', 'r+', encoding='utf8') as myfile,  open ('pruebaSalida.md', 'w') as secondFile: 
    for line in myfile:
        
        if line.find(imgSrcToSearch) != -1:

            i = line.find(imgSrcToSearch)
            imgSrc = line[i:i+36]

            #Busqueda de solo la ruta sin etiquetas
            # if line.find(ruta) != -1:
                # j = line.find(ruta)
                # rutaSaved = line[j:j+25]

            if imgSrc.find(onlyMedia) != -1:
                
                k = imgSrc.find(onlyMedia)
                img = imgSrc[k:k+17]

                if img.find(onlyImg) != -1:
                    l = img.find(onlyImg)
                    dataImg = img[l:l+10]
                    print(f"antes {dataImg}")
                    #agregar un if para que vea si es png o jpg, si es png agrega ng al final, si es jpg solo la g
                    if dataImg[-1] == "g":
                        secondFile.write("![" + dataImg.rstrip('/n') + "](./images/media/" + dataImg.rstrip('/n') + ")")
                    else:
                        dataImg = img[l:l+10]#solo funciona para png,si debe ser para jpg se debe poner 11 y quitar el ng 
                        secondFile.write("![" + dataImg.rstrip('/n') + "ng](./images/media/" + dataImg.rstrip('/n') + "ng)")
                        

        else:
            secondFile.write(line.rstrip('/n'))
            