import pygame
import random

ancho = 900
alto = 500

Negro=[0,0,0]
Blanco=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):# m es para llamar a ken
        pygame.sprite.Sprite.__init__(self)
        self.m=m#Asociar la imagen
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=100
        self.vel_x=0
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Grupos
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()

    imagen = pygame.image.load('ken.png').convert_alpha()
    info = imagen.get_rect()#para cojer las posiciones de la imagen
    an_img = info[2]
    al_img = info[3]
    an_corte = an_img / 7
    al_corte = al_img /10
    m=[]
    x_corte = 0
    y_corte = 1
    limites=[4,4,3,5,2,4,5,5,7,1]

    for y in range(10):
        fila=[]
        for i in range(limites[y]): #Recorte
            cuadro= imagen.subsurface(i*an_corte,y_corte*al_corte,an_corte,al_corte)#valor de recorte
            fila.append(cuadro)
        m.append(fila)

    jugador=Jugador(m)
    jugadores.add(jugador)
    todos.add(jugador)
    reloj=pygame.time.Clock()
    fin=False
    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.vel_x=5
                    jugador.vel_y=0
                if event.key == pygame.K_LEFT:
                    jugador.vel_x=-5
                    jugador.vel_y=0
                if event.key == pygame.K_UP:
                    jugador.vel_x=0
                    jugador.vel_y=-5
                if event.key == pygame.K_DOWN:
                    jugador.vel_x=0
                    jugador.vel_y=5
            if event.type == pygame.KEYUP:
                jugador.vel_x=0
                jugador.vel_y=0
        #Logica
        #Refresco
        todos.update()
        pantalla.fill(Negro)
        todos.draw(pantalla)
        #pantalla.blit(m[1][0],[10,10])#Donde voy a poner el sprite
        pygame.display.flip()
        reloj.tick(10)
