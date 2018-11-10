import pygame
import random

ancho = 900
alto = 500

Negro=[0,0,0]
Blanco=[255,255,255]


if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    imagen = pygame.image.load('kate.png').convert_alpha()
    info = imagen.get_rect()#para cojer las posiciones de la imagen
    print info
    an_img = info[2]
    al_img = info[3]
    print an_img,al_img
    an_corte = an_img / 4
    al_corte = al_img /4
    print an_img,al_img

    fila=[]
    x_corte = 0
    y_corte = 3

    for i in range(3):
        cuadro= imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)#valor de recorte
        fila.append(cuadro)

    pantalla.blit(fila[1],[0,0])#Donde voy a poner el sprite
    pygame.display.flip()

    #Grupos
    fin=False
    #ciclo del programa
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
