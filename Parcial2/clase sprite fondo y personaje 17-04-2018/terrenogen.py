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
    imagen = pygame.image.load('terrenogen.png')
    info = imagen.get_rect()#para cojer las posiciones de la imagen
    print info
    an_img = info[2]
    al_img = info[3]
    print an_img,al_img
    an_corte = an_img / 32
    al_corte = al_img /12
    print an_img,al_img
    x_corte = 16
    y_corte = 3

    cuadro= imagen.subsurface(x_corte*an_corte,y_corte*al_corte,32,32)#valor de recorte


    pantalla.blit(cuadro,[0,0])#Donde voy a poner el sprite
    pygame.display.flip()

    #Grupos
    fin=False
    #ciclo del programa
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
