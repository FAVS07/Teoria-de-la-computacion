import random
import math
archivo = open("Palindro.txt", "w")

def creacion(longitud):
    num =0
    resultado = "P" 
    par = longitud % 2
    longitud =math.floor(longitud/2)
    while(num != longitud):  
        numero  = random.randint(0,1)
        if numero == 1:
            resultado = "1"+ resultado +"1"
            archivo.write("(5)-> 1P1 "+resultado+"\n")
            num+=1
        else:
            resultado = "0"+ resultado +"0"
            archivo.write("(4)-> 0P0 "+resultado+"\n")
            num+=1
    nueva_cadena = " "
    if par == 0:
        nueva_cadena = resultado.replace("P", "e")
        archivo.write("(1) P-> e "+nueva_cadena + "\n")
    else:
         numero  = random.randint(0,1)
         if numero == 1:
            nueva_cadena = resultado.replace("P", "1")
            archivo.write("(3) P-> 1 "+nueva_cadena+"\n")
            
         else:
            nueva_cadena = resultado.replace("P", "0")
            archivo.write("(2) P-> 0 "+nueva_cadena+ "\n")
        
    print(nueva_cadena)

def menu():
    opcion = input("Longitud Aleatoria Y/N")
    longitud = 0
    error = 1
    if (opcion == 'Y' or opcion == 'y'):
       longitud= random.randint(3,100000)
    else: 
        while( error == 1):
            longitud = int(input("longitud Maxima:  "))
            if longitud > 100000:
                error = 1
            else:
                error = 0
    print("longitud real ",longitud)
    return longitud
longitud = menu()
creacion(longitud)

        

