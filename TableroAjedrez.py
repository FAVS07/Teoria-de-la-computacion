import random
archivo = open("Rutas.txt", "w")
archivo2 = open("RutasValidas.txt", "w")
archivo3 = open("RutasPieza2.txt", "w")
switch = {
    'a': {'b': 'f', 'r': 'be'},
    'b': {'b': 'acf', 'r': 'eg'},
    'c': {'b': 'fh', 'r': 'bdg'},
    'd': {'b': 'ch', 'r': 'g'},
    'e': {'b': 'afi', 'r': 'bj'},
    'f': {'b': 'acik', 'r': 'begj'},
    'g': {'b': 'cfhk', 'r': 'bdjl'},
    'h': {'b': 'ck', 'r': 'dgl'},
    'i': {'b': 'fn', 'r': 'ejm'},
    'j': {'b': 'fikn', 'r': 'egmo'},
    'k': {'b': 'fhnp', 'r': 'gjlo'},
    'l': {'b': 'hkp', 'r': 'go'},
    'm': {'b': 'in', 'r': 'j'},
    'n': {'b': 'ik', 'r': 'jmo'},
    'o': {'b': 'nkp', 'r': 'jl'},
    'p': {'b': 'k', 'r': 'lo'},
}
def routes(current, path):
    if not path:
        yield (current,)
        return
    first, *newpath = path
    for state in switch[current][first]:
        for route in routes(state, newpath):
            yield (current,) + route

def chess(cadena,inicio):
    for i, r in enumerate(routes(inicio, cadena), 1):
        output = ''.join(map(str, r))
        archivo.write(output +"\n")

def automata(estado, caracter ):
    if estado == 1:
        if caracter == 'r':
            estado = 2
        else:
            estado = 3
        return estado
    if estado == 2:
        if caracter == 'r':
            estado = 4
        else:
            estado = 5
        return estado
    if estado == 3:
        if caracter == 'r':
            estado = 4
        else:
            estado = 6
        return estado
    if estado == 4:
        if caracter == 'r':
            estado = 7
        else:
            estado = 8
        return estado
    if estado == 5:
        if caracter == 'r':
            estado = 9
        else:
            estado = 8
        return estado
    if estado == 6:
        if caracter == 'r':
            estado = 7
        else:
            estado = 10
        return estado
    if estado == 7:
        if caracter == 'r':
            estado = 7
        else:
            estado = 11
        return estado
    if estado == 8:
        if caracter == 'r':
            estado = 7
        else:
            estado = 11
        return estado
    if estado == 9:
        if caracter == 'r':
            estado = 7
        else:
            estado = 8
        return estado
    if estado == 10:
        if caracter == 'r':
            estado = 7
        else:
            estado = 6
        return estado
    if estado == 11:
        if caracter == 'r':
            estado = 7
        else:
            estado = 11
        return estado
def rutasValidas(longitud):
    archivo1 = open('Rutas.txt', 'r')
    for linea in archivo1:
        if linea[0] == 'a' and linea[longitud]== 'p' :
            archivo2.write(linea)
        if linea[0] == 'd' and linea[longitud]== 'm':
            archivo2.write(linea)
        
  
def menu():
    opcion = input("Cadena Random Y/N:  ")
    longitud = 0       
    cadena = ''      
    if (opcion == 'Y' or opcion == 'y'):
        longitud = int(input("Longitud:  "))
        while(longitud > 100): 
            longitud = int(input("Longitud:  "))

        caracteres_posibles = ['r', 'b']
        cadena = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
        print (cadena)

    else:
        cadena = input("Cadena:  ")
        longitud = len(cadena)
    return cadena,longitud

cadena, longitud = menu()
estado = 1

for i in cadena:
    estado = automata(estado,i)
if estado == 11 or estado == 10:
    print("Si es una cadena valida")
else:
    print("NOOO es una cadena de juego valida")

chess(cadena,'a')
opcion = input("quiere una segunda pieza Y/N")
if (opcion == 'Y' or opcion == 'y'): 
    estado = 4
    for i in cadena:
        estado = automata(estado,i)
    if estado == 9 or estado == 7:
        print("Si es una cadena valida Para pieza 2")
       
    else:
        print("No es una cadena valida Para pieza 2")
    chess(cadena,'d')

archivo.close()
rutasValidas(longitud)
archivo2.close()

if longitud < 6: 

    import pygame
    import time

    archivo = open("RutasValidas.txt",'r')
    cadena = ""
    for line in archivo:
        cadena = line
        break
    print(cadena)

    # Inicializar Pygame
    pygame.init()

    # Dimensiones del tablero
    width, height = 400, 400

    # Crear la ventana
    window = pygame.display.set_mode((width, height))

    # Colores
    white = (0, 0, 0)
    black = (255, 0, 0)
    red = (255, 255, 255)

    # Tamaño de cada casilla del tablero
    square_size = width // 4

    # Posición inicial del círculo
    circle_row = 0
    circle_col = 0

    # Bucle principal del juego
    running = True
    i =0
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        circle_col = 0
        circle_row = 0
        if cadena[i] == 'a':
            circle_col = 0
            circle_row = 0
        if cadena[i] == 'b':
            circle_col = 1
            circle_row = 0
        if cadena[i] == 'c':
            circle_col = 2
            circle_row = 0
        if cadena[i] == 'd':
            circle_col = 3
            circle_row = 0
        if cadena[i] == 'e':
            circle_col = 0
            circle_row = 1
        if cadena[i] == 'f':
            circle_col = 1
            circle_row = 1
        if cadena[i] == 'g':
            circle_col = 2
            circle_row = 1
        if cadena[i] == 'h':
            circle_col = 3
            circle_row = 1
        if cadena[i] == 'i':
            circle_col = 0
            circle_row = 2
        if cadena[i] == 'j':
            circle_col = 1
            circle_row = 2
        if cadena[i] == 'k':
            circle_col = 2
            circle_row = 2
        if cadena[i] == 'l':
            circle_col = 3
            circle_row = 2
        if cadena[i] == 'm':
            circle_col = 0
            circle_row = 3
        if cadena[i] == 'n':
            circle_col = 1
            circle_row = 3
        if cadena[i] == 'o':
            circle_col = 2
            circle_row = 3
        if cadena[i] == 'p':
            circle_col = 3
            circle_row = 3
        print( circle_col," ",circle_row)
        # Dibujar el tablero
        for row in range(4):
            for col in range(4):
                x = col * square_size
                y = row * square_size

                # Alterna el color de las casillas
                if (row + col) % 2 == 0:
                    color = white
                else:
                    color = black

                pygame.draw.rect(window, color, (x, y, square_size, square_size))

        # Dibujar el círculo en la casilla actual
        circle_x = circle_col * square_size + square_size // 2
        circle_y = circle_row * square_size + square_size // 2
        pygame.draw.circle(window, red, (circle_x, circle_y), square_size // 2)

        # Actualizar la ventana
        pygame.display.flip()
        time.sleep(1.2)
        i+=1
        if i == len(cadena):
            running = False
        
    # Cerrar Pygame
    pygame.quit()
