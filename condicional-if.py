import random
archivo = open("Historia.txt", "w")
def creacion(longitud):
    cadena = " iCtSA"
    longitud -=1
    elementos_insertar1 = ["i", "C", "t","S","A"]
    elementos_insertar2 = ["e","S"]
    elementos_insertar3 = ["e"]
    archivo.write("              iCtSA \n")
    lista_cadena = list(cadena)
    num=0
    indice =0
    while(num != longitud ):
        if lista_cadena[indice]== "S":
            remplaza = random.randint(0,1)
            if remplaza == 1:
                del lista_cadena[indice]
                num +=1
                for i, elemento in enumerate(elementos_insertar1):
                    lista_cadena.insert(indice + i, elemento)
                nueva_cadena = "".join(lista_cadena)
                archivo.write("S ->  iCtSA  "+nueva_cadena +"\n") 
        else: 
            if lista_cadena[indice] == "A":
                remplaza = random.randint(0,1)
                if remplaza == 1:
                    del lista_cadena[indice]    
                    for i, elemento in enumerate(elementos_insertar2):
                        lista_cadena.insert(indice + i, elemento) 
                    nueva_cadena = "".join(lista_cadena)
                    archivo.write("A -> eS      "+nueva_cadena +"\n")
                else:
                    del lista_cadena[indice]    
                    for i, elemento in enumerate(elementos_insertar3):
                        lista_cadena.insert(indice + i, elemento) 
                    nueva_cadena = "".join(lista_cadena)
                    archivo.write("A -> e       "+nueva_cadena +"\n")
        indice+=1

        if len(lista_cadena) == indice:
            num+=1
            for i, elemento in enumerate(elementos_insertar1):
                    lista_cadena.insert(indice + i, elemento)
            nueva_cadena = "".join(lista_cadena)
            archivo.write("fS -> iCtSA  "+nueva_cadena +"\n") 


    nueva_cadena = "".join(lista_cadena)
    print(nueva_cadena)
    return nueva_cadena

def codigo(cadena):
    archivocodigo = open("Codigo.txt","w")
    num=-1
    for i in cadena:
        if i == "i":
            num +=1
            archivocodigo.write("\t"*num+"if(){\n")
            
        if i == "e" or i == "A":
            archivocodigo.write("\t"*num+"}\n")
            num-=1
            
def menu():
    opcion = input("Longitud Aleatoria Y/N")
    longitud = 0
    error = 1
    if (opcion == 'Y' or opcion == 'y'):
       longitud= random.randint(2,100)
    else:
   
        while( error == 1):
            longitud = int(input("longitud Maxima:  "))
            if longitud > 100 or longitud < 2:
                error = 1
            else:
                error = 0
    return longitud

longitud = menu()
print (longitud)
cadena = creacion(longitud)
codigo(cadena)


