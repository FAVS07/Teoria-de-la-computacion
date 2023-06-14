import random
archivo = open("Descripcion.txt", 'w')
archivo2 = open("Cadenas.csv",'w')
def estados(caracter, estado):
    caracterNuevo = ""
    movimiento = ""
    if estado == 1:
        if caracter == "*":
            estado = 2
            caracterNuevo = "X"
            movimiento = "R"
            return estado, caracterNuevo , movimiento
    if estado == 2:
        if caracter == "*":
            estado = 3
            caracterNuevo = "*"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 2
            caracterNuevo = "|"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
    if estado == 3:
        if caracter == "*":
            estado = 4
            caracterNuevo = "X"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 3
            caracterNuevo = "|"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
    if estado == 4:
        if caracter == "*":
            estado = 4
            caracterNuevo = "*"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 5
            caracterNuevo = "a"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
        if caracter == "X":
            estado = 7
            caracterNuevo = "X"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
    if estado == 5:
        if caracter == "*":
            estado = 5
            caracterNuevo = "*"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 5
            caracterNuevo = "|"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
        if caracter == "-":
            estado = 6
            caracterNuevo = "|"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "X":
            estado = 5
            caracterNuevo = "X"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
#######################################
    if estado == 6:
        if caracter == "*":
            estado = 6
            caracterNuevo = "*"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 6
            caracterNuevo = "|"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "a":
            estado = 4
            caracterNuevo = "|"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "X":
            estado = 6
            caracterNuevo = "X"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
######################################
    if estado == 7:
        if caracter == "*":
            estado = 8
            caracterNuevo = "*"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 7
            caracterNuevo = "|"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
###########################################
    if estado == 8:
        if caracter == "-":
            estado = 9
            caracterNuevo = "*"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 8
            caracterNuevo = "|"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
        if caracter == "X":
            estado = 8
            caracterNuevo = "*"
            movimiento = "R"
            return estado, caracterNuevo, movimiento
###############################################3
    if estado == 9:
        if caracter == "*":
            estado = 9
            caracterNuevo = "*"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "|":
            estado = 9
            caracterNuevo = "|"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
        if caracter == "X":
            estado = 10
            caracterNuevo = "*"
            movimiento = "L"
            return estado, caracterNuevo, movimiento
def cadenaAleatoria(longitud):
    num = random.randint(1, longitud-4)
    cadena = "*" 
    i=0
    while i != num:
        cadena += "|"
        i+=1
    cadena += "*"
    num2 = longitud-3-num
    i=0
    while i != num2:
        cadena += "|"
        i+=1
    cadena += "*"
    return cadena

def menu():
    opcion = input("Cadena Random Y/N:  ")
    longitud = 0       
    cadena = ''      
    if (opcion == 'Y' or opcion == 'y'):
        longitud = random.randint(5,20)
        print(longitud)
        #longitud = int(input("Longitud:  "))
        #while(longitud < 5 and longitud > 50): 
         #   longitud = int(input("Longitud:  "))
        cadena = cadenaAleatoria(longitud)
        print (cadena)
    else:
        cadena = input("ingrese la cadena con el formato *||*||* \n")
    return cadena
def maquina():
    estado = 1
    i=0
    lista_cadena = list(cadena)
    caracterNuevo = ""
    movimiento = ""
    archivo.write(cadena+ "\n")
    while(estado != 10): 
        archivo.write(" ("+lista_cadena[i]+" "+movimiento+" " )
        archivo.write(str(estado))
        archivo.write(") --> ")
        estado, caracterNuevo, movimiento = estados(lista_cadena[i],estado)
        lista_cadena[i]= caracterNuevo
        nueva_cadena = ''.join(lista_cadena)
        lista_cadena = list(nueva_cadena)
        archivo.write(nueva_cadena +"\n")
        
        if movimiento == 'L':
            i-=1
        else:
            i+=1
            if i == len(lista_cadena):
                lista_cadena += ["-"]
    print("Cadena Resultante:\n")
    print(nueva_cadena)

cadena = menu()
maquina()

if len(cadena) < 10:
    estado = 1
    i=0
    lista_cadena = list(cadena)
    caracterNuevo = ""
    movimiento = ""      
    import pygame
    import sys
    import time

    # Inicializar pygame
    pygame.init()

    # Configuración de la ventana
    screen_width = 400
    screen_height = 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cadena de caracteres en Pygame")

    # Colores
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Fuente
    font_size = 40
    font = pygame.font.Font(None, font_size)

    # Bucle principal del juego
    index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(white)
        while(estado != 10): 
            screen.fill(white)
            estado, caracterNuevo, movimiento = estados(lista_cadena[i],estado)
            lista_cadena[i]= caracterNuevo
            nueva_cadena = ''.join(lista_cadena)
            j=0
            cadena_Mostrar =" "
            while(j != i):
                cadena_Mostrar+= nueva_cadena[j] +" "
                j+=1
            cadena_Mostrar +="[" + nueva_cadena[i]+"]"
            while(j != len(nueva_cadena)):
                cadena_Mostrar+= nueva_cadena[j] +" "
                j+=1
            text = font.render(cadena_Mostrar, True, black)
            screen.blit(text, (50, 50))
            text = font.render(str(estado), True, black)
            screen.blit(text, (50, 150))
            pygame.display.flip()
            time.sleep(.5)
            lista_cadena = list(nueva_cadena)
            if movimiento == 'L':
                i-=1
            else:
                i+=1
                if i == len(lista_cadena):
                    lista_cadena += ["-"]
            pygame.display.flip()   
            # Actualizar la pantalla
        
