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
        self.rect.y=400
        self.vel_x=0
        self.salud=3


    def update(self):
        self.rect.x += self.vel_x

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([0,0,255])
        self.rect = self.image.get_rect()
        self.rect.y=-40
        self.vel_y=2
        self.temp=random.randrange(50)
        self.tempdis=random.randrange(100)
        self.disparar=10

    def update(self):
        if self.tempdis > 0:
            self.tempdis -=1
        else:
            self.disparar=True

        if self.temp >0:
            self.temp -=1
        else:
            self.rect.y += self.vel_y


class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([30,30])
        self.image.fill([255,0,255])
        self.rect = self.image.get_rect()
        self.vel_y = -10

    def update(self):
        self.rect.y += self.vel_y


if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Declaracion de grupos
    todos=pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    balas = pygame.sprite.Group()
    balas_e= pygame.sprite.Group()

    jugador=Jugador()
    jugadores.add(jugador)
    todos.add(jugador)

    num_enemigos=10

    for i in range(num_enemigos):
        e=Enemigo()
        e.rect.x=random.randrange(ancho)
        e.rect.y=-10
        enemigos.add(e)
        todos.add(e)

    reloj=pygame.time.Clock()
    fin=False
    go=False
    ptos=0
    #ciclo del programa
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.vel_x=+2
                if event.key == pygame.K_LEFT:
                    jugador.vel_x=-2
                if event.key == pygame.K_SPACE:
                    b=Bala()
                    b.rect.x=jugador.rect.x
                    b.rect.y=jugador.rect.y
                    balas.add(b)
                    todos.add(b)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.KEYUP:
                    jugador.vel_x=0

        #logica juego
        for e in enemigos:
            if e.disparar:
                b=Bala()
                b.vel_y=10
                b.rect.x= e.rect.x
                b.rect.y= e.rect.y
                todos.add(b)
                balas_e.add(b)
                e.disparar=False
                e.tempdis=random.randrange(50)

        for e in balas_e:
            if b.rect.y > alto:
                balas_e.remove(b)
                todos.remove(b)
            ls_colbe = pygame.sprite.spritecollide(b, jugadores, False)
            for j in ls_colbe:
                j.salud -=1
                balas_e.remove
                todos.remove(b)



        if jugador.rect.x < 0:
            jugador.rect.x=0
            jugador.vel_x=0
        if jugador.rect.x > (ancho - jugador.rect.width):
            jugador.rect.x=870
            jugador.vel_x=0

        eliminados=0
        #Colision jugador
        ls_col = pygame.sprite.spritecollide(jugador, enemigos, True) # Se elimina el enemigo

        for e in ls_col:
            ptos+=1
            print ptos
            enemigos.remove(e)
            todos.remove(e)
            eliminados+=1

        #Colision de balas
        for b in balas:
            ls_colb=pygame.sprite.spritecollide(b, jugadores,True)  # Se elimina el jugador
            for e in ls_col:
                enemigos.remove(e)
                todos.remove(e)
                enemigos.remove(b)
                todos.remove(b)
                eliminados+=1

            # Enemigos fuera de pantalla
        for e in enemigos:
            if e.rect.y > alto:
                enemigos.remove(e)
                todos.remove(e)
                eliminados+=1
        #Crea enemigos nuevos

        for i in range(eliminados):
            e=Enemigo()
            e.rect.x=random.randrange(ancho)
            e.rect.y=-10
            enemigos.add(e)
            todos.add(e)

        for j in jugadores:
            if j.salud ==0:
                jugadores.remove(j)
                todos.remove(j)
        #refresco de pantalla
        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(100)
