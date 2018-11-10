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
    imagen = pygame.image.load('animals.png').convert_alpha()
    info = imagen.get_rect()#para cojer las posiciones de la imagen
    print info
    an_img = info[2]
    al_img = info[3]
    print an_img,al_img
    an_corte = an_img / 12
    al_corte = al_img /8
    print an_img,al_img

    fila=[]
    m=[]
    x_corte = 0
    y_corte = 0

    for i in range(5):
        cuadro= imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)#valor de recorte
        fila.append(cuadro)


    #Grupos
    reloj=pygame.time.Clock()
    fin=False
    y=0
    x=0
    dirs=0
    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dirs=1
                    x+=1
                if event.key == pygame.K_LEFT:
                    x-=1
                if event.key == pygame.K_UP:
                    dirs=3
                if event.key == pygame.K_DOWN:
                    dirs=0
        #Logica
        #i+=1
        #if i>2:
    #        i=0
    #    y+=1
    #    x+=1
        #Refresco
        pantalla.fill(Negro)
        pantalla.blit(fila[i],[x,y])#Donde voy a poner el sprite
        pygame.display.flip()
        reloj.tick(20)
