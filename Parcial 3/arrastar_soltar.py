import pygame

ancho = 900
alto = 500

Negro=[0,0,0]
Blanco=[255,255,255]

class Cuadro(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()
        self.click=False
        self.vel_x=0
        self.radius=100  # radio del cuadro cuando haga contacto con el enemigo
    def update(self):
        self.rect.x+= self.vel_x
        self.vel_x=0

class Linea(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill([255,255,255])
        self.rect = self.image.get_rect()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill([0,255,0])
        self.rect = self.image.get_rect()
        self.click=False
        self.vel_x=0
    def update(self):
        self.rect.x+= self.vel_x
        self.vel_x=0

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Declaracion de grupos
    todos=pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    cuadros= pygame.sprite.Group()
    lineas=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()

    c=Cuadro(50,50)
    cuadros.add(c)
    todos.add(c)

    l=Linea(300,4)
    l.rect.x=100
    l.rect.y=200
    todos.add(l)
    lineas.add(l)


    reloj=pygame.time.Clock()
    fin=False
    go=False
    ptos=0
    #ciclo del programa
    while not  fin:
        pos=pygame.mouse.get_pos()
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>=200 and pos[0]<=300:
                    if pos[1]>=400:
                        e=Enemigo(50,50)
                        e.rect.x=pos[0]
                        e.rect.y=pos[1]
                        enemigos.add(e)
                        todos.add(e)
                if pos[0]>0 and pos[0]< ancho:
                    if pos[1]< 100 and pos[1]>0:
                        c=Cuadro(50,50)
                        jugadores.add(c)
                        cuadros.add(c)
                        todos.add(c)
                for c in cuadros:
                    if c.rect.collidepoint(pos):#
                        c.click=True
                for e in enemigos:
                    if e.rect.collidepoint(pos):
                        e.click=True
            if event.type == pygame.MOUSEBUTTONUP:
                for c in cuadros:
                    c.click=False
                for e in enemigos:
                    e.click=False

        #Logica
        for c in cuadros:
            if c.click:
                c.rect.center=pos
        for e in enemigos:
            if e.click:
                e.rect.center=pos

        for e in enemigos:
            col = pygame.sprite.spritecollide(e,lineas,False)
            for l in col:
                if not e.click:
                    e.vel_x=5

        for c in cuadros:
            for e in enemigos:
                if pygame.sprite.collide_circle(c,e):
                    print 'disparo'

        #refresco de pantalla
        todos.update()
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
