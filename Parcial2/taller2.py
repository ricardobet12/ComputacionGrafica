import pygame
import random
ancho = 900
alto = 600
Negro=[0,0,0]
Blanco=[255,255,255]
Verde=[0,255,0]
Rojo=[255,0,0]

class Bloque(pygame.sprite.Sprite):
    def __init__(self):
        pass
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,30])
        self.image.fill(Verde)
        self.rect=self.image.get_rect()
        self.vel_x=0


    def update(self):
        self.rect.x += self.vel_x


class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pass
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,30])
        self.image.fill(Rojo)
        self.rect=self.image.get_rect()
        self.vel_x=0


if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    todos=pygame.sprite.Group()

    jugador=Bloque()
    jugador.rect.x=100
    todos.add(jugador)

    num_enemigos=10
    enemigos=pygame.sprite.Group()
    for i in range(num_enemigos):
        e=Enemigo()
        e.rect.x=random.randrange(ancho)
        e.rect.y=random.randrange(alto)
        enemigos.add(e)
        todos.add(e)

    reloj=pygame.time.Clock()
    todos.draw(pantalla)
    pygame.display.flip


    fin=False
    #ciclo del programa
    while not  fin:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    jugador.vel_x=2
        #logica
        #Refresco
        todos.update()
        pantalla.fill(Negro)
        todos.draw(pantalla)
        pygame.display.flip
        reloj.tick(40)
