import pygame

ancho = 900
alto = 500

Negro=[0,0,0]
Blanco=[255,255,255]

class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill(Blanco)
        self.rect = self.image.get_rect()
        self.vel_x=0
        self.vel_y=0

    def update(self):
        if self.vel_y <= 0:
            self.vel_y = 1
        else:
            self.vel_y +=0.4

        self.rect.y += self.vel_y
        #Limites
        if self.rect.y >= (alto - self.rect.height):
            self.rect.y = (alto - self.rect.height)
            self.vel_y = 0
        self.rect.x += self.vel_x


class Plataforma(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill(Blanco)
        self.rect = self.image.get_rect()
        self.vel_y=-5

    #def update(self):
        #self.rect.y += self.vel_y

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    jugadores= pygame.sprite.Group()
    plataformas= pygame.sprite.Group()
    todos= pygame.sprite.Group()

    j=Jugador(40,80)
    jugadores.add(j)
    todos.add(j)

    p=Plataforma(300,40)
    p.rect.x =300
    p.rect.y =400
    plataformas.add(p)
    todos.add(p)


fin=False
reloj=pygame.time.Clock()

while not  fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                j.vel_x=5
            if event.key == pygame.K_LEFT:
                j.vel_x=-5
            if event.key == pygame.K_SPACE:
                j.rect.y +=-100

    #Colisiones jugador y la plataforma
    col_p= pygame.sprite.spritecollide(j,plataformas,False)
    for p in col_p:
        if j.rect.bottom > p.rect.top:
            j.rect.bottom = p.rect.top
            j.vel_y = 0


    todos.update()
    pantalla.fill(Negro)
    todos.draw(pantalla)
    pygame.display.flip()
    reloj.tick(40)
