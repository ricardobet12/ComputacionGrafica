import pygame
import random

ancho = 900
alto = 500
Negro=[0,0,0]
Blanco=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        #self.rect.y=alto-100
        self.rect.y=100
        self.vel_x=0
        self.vel_y=0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Muro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([90,90])
        self.image.fill([0,0,255])
        self.rect = self.image.get_rect()

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Grupos
    todos = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    muros = pygame.sprite.Group()

    jugador = Jugador()
    todos.add(jugador)
    jugadores.add(jugador)

    m=Muro()
    m.rect.x = 200
    m.rect.y = 200
    todos.add(m)
    muros.add(m)

    m=Muro()
    m.rect.x = 400
    m.rect.y = 200
    todos.add(m)
    muros.add(m)

    reloj=pygame.time.Clock()
    fin=False
    #ciclo del programa
    while not  fin:
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

        #Logica del juego
        ls_col = pygame.sprite.spritecollide(jugador,muros,False) #Se va almacenar contra que muro mi jugador a chocado
        for m in ls_col:
            if (jugador.vel_x >0)and(jugador.rect.right >= m.rect.left):
                jugador.vel_x=0
                jugador.rect.right = m.rect.left
            if (jugador.vel_y > 0)and(jugador.rect.bottom >= m.rect.top):
                jugador.vel_y=0
                jugador.rect.bottom = m.rect.top
            if (jugador.vel_x < 0)and(jugador.rect.left <= m.rect.right):
                jugador.vel_x=0
                jugador.rect.left = m.rect.right
            if (jugador.vel_y < 0)and(jugador.rect.top <= m.rect.bottom):
                jugador.vel_y=0
                jugador.rect.top = m.rect.bottom

        #Ciclo de refresco
        todos.update()
        pantalla.fill(Negro)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(40)
