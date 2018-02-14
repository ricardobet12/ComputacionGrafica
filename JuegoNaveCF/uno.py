import pygame,sys
from pygame.locals import *

Color=(0,140,60)    #forma 1 para crear color con RGB
ColorDos = pygame.Color(250,120,9)   #forma 2 para crear color

pygame.init() #Sentencia obligatoria para usar pygame
ventana = pygame.display.set_mode((400,300)) #Definir el tamano de la ventana
pygame.display.set_caption("Hola mundo") #El titulo de la ventana

ColorTres = pygame.Color(70,80,150)
pygame.draw.line(ventana,ColorTres,(60,80),(160,100),8)#1pmt donde se va a dibujar el inicio de la linea,2pmt el color de la linea 3pmt dupla posicion en X y en Y 4pmt donde va quedar el segundo punto 5pmt ancho de la linea

while True:
    #ventana.fill(Color)              #Para ingresar color a la ventana
    for evento in pygame.event.get():  #para capturar cada evento con el teclado y el mouse
        if evento.type == QUIT:     #para el boton de cerrar de la pantalla X
            pygame.quit()            #si el if se cumple se detiene todos los modulos
            sys.exit()               #para cerrar la ventana

    pygame.display.update() #Para que la ventana venta se este actualizando
