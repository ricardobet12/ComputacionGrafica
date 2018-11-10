import pygame
ancho = 900
alto = 600
Negro=[0,0,0]
Blanco=[255,255,255]

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    tux=pygame.image.load('homero.jpeg')
    fondo=pygame.image.load('fondo2.jpg')
    info= tux.get_rect()
    anc=info[2]
    alt=info[3]
    print info[2],info[3]
    pos_x=100
    pos_y=100
    vel_x=0
    vel_y=0
    reloj=pygame.time.Clock()
    fin=False
    #ciclo del programa
    while not  fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    vel_y=0
                    vel_x=+2
                if event.key == pygame.K_LEFT:
                    vel_x=-2
                if event.key == pygame.K_SPACE:
                    vel_y=0
                    vel_x=0
                if event.key == pygame.K_UP:
                    vel_x=0
                    vel_y=-2
                if event.key == pygame.K_DOWN:
                    vel_x=0
                    vel_y=+2
        #logica del programa
        if jugador.rect.x > (ancho - jugador.rect.width):
            jugador.rect.x=0
            jugador.vel_x=0



        #refresco de pantalla
        pantalla.fill(Blanco)
        pantalla.blit(fondo,[0,0])
        pantalla.blit(tux,[pos_x,pos_y])

        pygame.display.flip()
        pos_x+=vel_x
        pos_y+=vel_y
        reloj.tick(50)
