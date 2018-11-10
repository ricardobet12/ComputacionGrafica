import pygame
ancho = 1300
alto = 900
Negro=[0,0,0]
Blanco=[255,255,255]

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    fondo=pygame.image.load('fondo2.jpg')
    pos_x=0
    vel_x=-1
    fin=False
    #ciclo del programa
    while not fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        pos=pygame.mouse.get_pos()
        if pos[0] == 1299:
            vel_x=+2
            print pos_x
        if pos[0] == 1:
            vel_x=-2
            print pos_x

        pantalla.blit(fondo,[pos_x,0])
        pygame.display.flip()
        pos_x+=vel_x
