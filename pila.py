import pygame
import time

import numpy as np
class pilaDataS:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_vacio():
            return self.items.pop()

    def is_vacio(self):
        return len(self.items) == 0

    def pico(self):
        if not self.is_vacio():
            return self.items[-1]

def AutomataDePila(string, file):
    n = len(string)
    pila = pilaDataS()
    i = 0
    file.write("Pila Inicial: vacio\n")
    while i < n:
        if string[i] == '0':
            pila.push('0')
            file.write(f" se lee  {string[i]}\n")
            file.write(f"pila: {pila.items}\n")
        elif string[i] == '1':
            if pila.is_vacio():
                file.write(" NO pertenece\n")
                return False
            if pila.pico() == '0':
                pila.pop()
                file.write(f"se lee {string[i]}\n")
                file.write(f"pila: {pila.items}\n")
            else:
                file.write("*********NO pertenece*********\n")
                return False
        i += 1
    if pila.is_vacio():
        file.write("SI pertenece\n")
        return True
    else:
        file.write(" NO pertenece\n")
        return False
def menu():
    opcion = input("Cadena Random Y/N:  ")
    longitud = 0       
    operations = ''      

    if (opcion == 'Y' or opcion == 'y'):

        longitud = int(input("Longitud:  "))
        while(longitud > 1000): 
            longitud = int(input("Longitud:  "))

        operations = np.random.randint(2, size=longitud)
        operations= ''.join(str(num) for num in operations)

    else:
        operations = input("Cadena:  ")
        longitud = len(operations)
    return operations,longitud

operations,longitud = menu()
print (operations)
f = open("Pila.txt", "w")
AutomataDePila(operations,f)
f.close()


if longitud < 11:

    pygame.init()

    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Animación de una pila')

    WHITE = (255, 255, 255)
    BLUE = (0, 255, 255)

    stack_size = 10

    stack_x = width // 2
    stack_y = height - 50
    stack_height = 20
    stack_width = 100

    stack = []
    def push(value):
        if len(stack) < stack_size:
            stack.append(value)

    def pop():
        if len(stack) > 0:
            stack.pop()

    def draw_stack():
        pygame.draw.rect(screen, WHITE, (stack_x - stack_width/2, stack_y - stack_height/2, stack_width, stack_height), 2)
        for i, value in enumerate(stack):
            pygame.draw.rect(screen, BLUE, (stack_x - stack_width/2, stack_y - stack_height/2 - (i+1)*stack_height, stack_width, stack_height))

    running = True
    index = 0  
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if index < len(operations):
            operation = operations[index]
            if operation == '0':
                push('Elemento')
            elif operation == '1':
                pop()
            index += 1
        screen.fill((0, 0, 0))
        draw_stack()
        pygame.display.flip()
        time.sleep(1)
        if index >= len(operations) and len(stack) == 0:
            running = False
    pygame.quit()
