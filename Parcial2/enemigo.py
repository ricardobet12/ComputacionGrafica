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
        self.rect.y=alto-100
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
        self.temp = random.randrange(50)
        self.tempdis=random.randrange(50)
        self.disparar=False

    def update(self):
        if self.tempdis > 0:
            self.tempdis-=1
        else:
            self.disparar=True
        if self.temp > 0:
            self.temp-=1
        else:
            self.rect.y+=self.vel_y


class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([10,20])
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()
        self.vel_y=-10
    def update(self):
        self.rect.y+=self.vel_y


if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Declaracion de Grupos
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_e=pygame.sprite.Group()

    jugador=Jugador()
    jugadores.add(jugador)
    todos.add(jugador)

    num_enemigos=10

    for i in range(num_enemigos):
        e=Enemigo()
        e.rect.x=random.randrange(ancho)

        enemigos.add(e)
        todos.add(e)

    fuente=pygame.font.Font(None,25)
    texto=fuente.render("Vida",False,[255,255,255])


    reloj=pygame.time.Clock()
    ptos=0
    fin=False
    go=False
    #ciclo del programa
    while not fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.vel_x=5
                if event.key == pygame.K_LEFT:
                    jugador.vel_x=-5
                if event.key == pygame.K_SPACE:
                    b=Bala()
                    b.rect.x = jugador.rect.x
                    b.rect.y = jugador.rect.y
                    balas.add(b)
                    todos.add(b)
            if event.type == pygame.KEYUP:
                jugador.vel_x=0

        #logica juego

        for e in enemigos:
            if e.disparar:
                b=Bala()
                b.vel_y=10
                b.rect.x = e.rect.x
                b.rect.y = e.rect.y
                todos.add(b)
                balas_e.add(b)
                e.disparar=False
                e.tempdis=random.randrange(150)

        for b in balas_e:
            if b.rect.y > alto:
                balas_e.remove(b)
                todos.remove(b)
            ls_colbe=pygame.sprite.spritecollide(b,jugadores,False)
            for j in ls_colbe:
                j.salud-=1
                balas_e.remove(b)
                todos.remove(b)

        if jugador.rect.x < 0:
            jugador.vel_x=0
            jugador.rect.x=0
        if jugador.rect.x > (ancho - jugador.rect.width):
            jugador.rect.x=ancho-jugador.rect.width
            jugador.vel_x=0

        #Lista de colisiones
        eliminados=0
        ls_col = pygame.sprite.spritecollide(jugador,enemigos,True)
        for e in ls_col:
            ptos+=1
            print ptos
            enemigos.remove(e)
            todos.remove(e)
            eliminados+=1

        #Enemigos fuera de pantalla
        for e in enemigos:
            if e.rect.y > alto:
                enemigos.remove(e)
                todos.remove(e)
                eliminados+=1

        #Colision de Balas
        for b in balas:
            ls_colb=pygame.sprite.spritecollide(b,enemigos,True)
            for e in ls_colb:
                enemigos.remove(e)
                todos.remove(e)
                balas.remove(b)
                todos.remove(b)
                eliminados+=1

        #Crea enemigos nuevos
        for i in range(eliminados):
            e=Enemigo()
            e.rect.x=random.randrange(ancho)
            enemigos.add(e)
            todos.add(e)

        for j in jugadores:
            if j.salud == 0:
                jugadores.remove(j)
                todos.remove(j)
                go=True

        if go:
            break

        texto1=fuente.render(str(jugador.salud),False,[255,255,255])

        #refresco de pantalla
        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pantalla.blit(texto,[10,alto-50])
        pantalla.blit(texto1,[60,alto-50])
        pygame.display.flip()
        reloj.tick(60)

    if go:
        fintxt= fuente.render("Fin del juego",False,[255,0,0])
        pantalla.fill([0,255,0])
        pantalla.blit(fintxt,[250,200])
        pygame.display.flip()
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
