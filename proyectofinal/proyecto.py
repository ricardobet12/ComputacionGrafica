import pygame
import random

ancho = 1366
alto = 768

Negro=[0,0,0]
Blanco=[255,255,255]
AzulMarino=[0,255,255]
Amarillo=[255,255,0]
Verde=[0,255,0]
Rojo=[255,0,0]

class Menu():
    def menuInicial(self):
        intro=True
        while intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                mouse=pygame.mouse.get_pos()
                print mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #INICIAR HISTORIA Y JUEGO
                    if mouse[0] >=960 and mouse[0] <=1180:
                        if mouse[1] >= 410 and mouse[1] <= 450:
                            menu.historia()
                            intro=False
                    #INSTRUCCIONES
                    if mouse[0] >=960 and mouse[0] <=1180:
                        if mouse[1] >= 510 and mouse[1] <= 548:
                            menu.instrucciones()
                            intro=False
                    #CREDITOS
                    if mouse[0] >=960 and mouse[0] <=1100:
                        if mouse[1] >= 563 and mouse[1] <= 590:
                            menu.creditos()
                            intro=False
                    #SALIR
                    if mouse[0] >=960 and mouse[0] <=1040:
                        if mouse[1] >= 630 and mouse[1] <= 680:
                            pygame.quit()
                            quit()

            pantalla.fill(Negro)
            imagenn=pygame.image.load('images/menu.jpg')
            imagen=pygame.transform.scale(imagenn,(1376,768))
            pantalla.blit(imagen,[0,0])
            pygame.display.update()
            reloj.tick(15)

    def creditos(self):
        intro2=True
        while intro2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        intro2 = False
                    if event.key == pygame.K_ESCAPE:
                        menu.menuInicial()
            pantalla.fill(Negro)
            imagenn=pygame.image.load('images/creditos.png')
            imagen=pygame.transform.scale(imagenn,(1200,700))
            # texto2 = Fuente.render(str("Prologo"), False, Blanco)
            pantalla.blit(imagen,[0,0])
            pygame.display.update()
            reloj.tick(15)

    def historia(self):
        pag=1
        intro3=True
        while intro3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        intro3=False
                    if event.key == pygame.K_SPACE:
                        pag+=1
                    if event.key == pygame.K_LEFT:
                        pag-=1
                    if event.key == pygame.K_ESCAPE:
                        menu.menuInicial()

            if pag == 1:
                imagenn = pygame.image.load('images/historia1.png')
                imagen=pygame.transform.scale(imagenn,(1200,600))
                pantalla.fill(Negro)
                pantalla.blit(imagen,[0,0])
                pygame.display.flip()
                pygame.display.update()

                # menu.menuInicial()
            if pag ==2:
                imagenn2=pygame.image.load('images/historia2.png')
                imagen2=pygame.transform.scale(imagenn2,(1200,600))
                pantalla.fill(Negro)
                pantalla.blit(imagen2,[0,0])
                pygame.display.update()

            if pag == 3:
                intro3=False
                sonidojuego.play()

    def instrucciones(self):
        intro4=True
        while intro4:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        intro4 = False
                    if event.key == pygame.K_ESCAPE:
                        menu.menuInicial()
            pantalla.fill(Negro)
            imagenn = pygame.image.load('images/instrucciones.png')
            imagen=pygame.transform.scale(imagenn,(1200,600))
            pantalla.blit(imagen,[0, 0])
            pygame.display.update()
            reloj.tick(15)


class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=1
        self.rect.x=100
        self.rect.y=540
        self.salud=3
        self.vel_x=0
        self.vel_y=0
    def update(self):
        if self.vel_y == 0:
           self.vel_y = 1
        else:
           self.vel_y += .35
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.accion==9:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0
        elif self.accion==10:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
                self.accion=0
        else:
            self.i+=1
            if self.i >= len(self.m[self.accion]):
                self.i=0
        self.image=self.m[self.accion][self.i]

class nojugable(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=0
        self.rect.x=0
        self.vel_x=0
        self.vel_y=0
    def update(self):
        if self.accion==1:
            self.vel_x=-3
            self.rect.x+=self.vel_x
            self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class eneestatico(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=0
        self.rect.x=0
        self.vel_x=0
        self.salud=2
        self.con=0
        self.temp = random.randrange(50)
        self.tempdis=random.randrange(50)
        self.disparar=True
    def update(self):
        if self.tempdis > 0:
            self.tempdis-=1
        else:
            self.disparar=True
        if self.temp > 0:
            self.temp-=1
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class final(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=0
        self.rect.x=0
        self.vel_x=0
        self.salud=10
        self.con=0
        self.temp = random.randrange(50)
        self.tempdis=random.randrange(50)
        self.disparar=True
    def update(self):
        if self.tempdis > 0:
            self.tempdis-=1
        else:
            self.disparar=True
        if self.temp > 0:
            self.temp-=1
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Pico(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/pl.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Balaestatico(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        #self.image.fill([255,255,255])
        self.i=0
        self.rect = self.image.get_rect()
        self.vel_x=-15
    def update(self):
        self.rect.x+=self.vel_x
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class Balafinal(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        #self.image.fill([255,255,255])
        self.i=0
        self.rect = self.image.get_rect()
        self.vel_x=+15
    def update(self):
        self.rect.x+=self.vel_x
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Enemigo1(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=0
        self.rect.x=0
        self.vel_x=-3
        self.vel_y=0
        self.salud=2
        self.con=0
        #self.temp = random.randrange(50)
        # self.tempdis=random.randrange(50)
        self.disparar=False

    def update(self):
        if self.vel_y <= 0:
            self.vel_y = 1
        else:
            self.vel_y +=0.5
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class EnemigoNave(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.sonidonave=pygame.mixer.Sound('sound/sonidonave.ogg')
        self.i=0
        self.rect.y=0
        self.rect.x=0
        self.vel_x=0
        self.salud=4
        self.con=0
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
            self.rect.x+=self.vel_x
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        # if self.rect.x < 30:
        #     self.vel_x=+5
        #     #self.accion=1

class BalaNave(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        #self.image.fill([255,255,255])
        self.i=0
        self.rect = self.image.get_rect()
        self.vel_y=+20
    def update(self):
        self.rect.y+=self.vel_y
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class BalaSoldado(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        #self.image.fill([255,255,255])
        self.i=0
        self.rect = self.image.get_rect()
    def update(self):
        self.vel_x=0
        if self.accion==0:
            self.vel_x-=8
        if self.accion==1:
            self.vel_x+=8
        self.rect.x+=self.vel_x
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Plataforma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/o2.png").convert_alpha()
        #self.image.fill(Blanco)
        self.rect = self.image.get_rect()
        self.vel_xx=0

    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
            self.vel_xx=0
        else:
            self.rect.move_ip(-8,0)

        self.rect.x-=self.vel_xx

class SoldadoRazo(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=2
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=0
        self.rect.x=0
        self.vel_x=3
        self.vel_y=0
        self.salud=2
        self.con=0
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
            self.rect.x += self.vel_x
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class MuroMovimiento(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/p.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y=380
        self.vel_y=+3
        self.vel_xx=0
    def update(self):
        # self.rect.y+=self.vel_y
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
            self.vel_xx=0
        else:
            self.rect.move_ip(-8,0)
        self.rect.x-=self.vel_xx

class Arma(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/arma.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y=610
        self.sonido=pygame.mixer.Sound('sound/yeah.ogg')
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Cuadro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/cajita.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y=380
        self.vel_xx=0
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
            self.vel_xx=0
        else:
            self.rect.move_ip(-8,0)
        self.rect.x-=self.vel_xx

class Bala(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        #self.image.fill([255,255,255])
        self.i=0
        self.rect = self.image.get_rect()
        self.vel_x=30
        self.vel_y=0
        self.rect.y=380
        self.sonido=pygame.mixer.Sound('sound/sonidoBalaJugador.ogg')
    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y-=self.vel_y
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class mejora1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/modificador_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=850
        self.rect.y=485
        self.sonido=pygame.mixer.Sound('sound/recargaArma.ogg')
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class mejora2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/modificador_2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=2000
        self.rect.y=400
        self.sonido=pygame.mixer.Sound('sound/recargaArma.ogg')
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class mejora3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/modificador_3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=5200
        self.rect.y=375
        self.sonido=pygame.mixer.Sound('sound/recargaArma.ogg')
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Salud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/salud.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=2400
        self.rect.y=400
        self.sonido=pygame.mixer.Sound('sound/recargaArma.ogg')
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Velocidad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/velocidad.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=3400
        self.rect.y=300
        self.sonido=pygame.mixer.Sound('sound/recargaArma.ogg')
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Moneda(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("images/Moneda.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y=380
        self.vel_x=0
    def update(self):
        if j.rect.x <= 640:
            self.rect.move_ip(0,0)
        else:
            self.rect.move_ip(-8,0)

class Explosion(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
    def update(self):
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class PlataformasNivel1(pygame.sprite.Sprite):
    def __init__(self):
        self.ListaPlataformas = pygame.sprite.Group()
        nivel = [[800, 260],
                 [810, 510],
                 [1180, 340],
                 [1780, 500],
                 [2780, 500],
                 [2980, 350],
                 [3180, 200],
                 [3480, 500],
                 [3580, 200],
                 [4000, 300],
                 [4200, 500],
                 [4680, 300],
                 [4780, 500],
                 [5400, 700],
                 [2500, 600],
                 [5600, 700]
                   ]
        for plataforma in nivel:
            bloque = Plataforma()
            bloque.rect.x = plataforma[0]
            bloque.rect.y = plataforma[1]
            self.ListaPlataformas.add(bloque)

    def update(self):
        self.ListaPlataformas.update()

    def draw(self, pantalla):
        self.ListaPlataformas.draw(pantalla)

class CuadrosNivel1(pygame.sprite.Sprite):
    def __init__(self):
        self.ListaCuadros = pygame.sprite.Group()
        nivel = [[800, 220],
                 [1200, 470],
                 [1580, 290],
                 [1780, 460],
                 [2880, 460],
                 [3080, 300],
                 [3280, 160],
                 [3580, 460],
                 [3680, 160],
                 [4200, 260],
                 [4300, 460],
                 [4780, 260],
                 [4880, 460]
                   ]
        for plataforma in nivel:
            bloque = Cuadro()
            bloque.rect.x = plataforma[0]
            bloque.rect.y = plataforma[1]
            self.ListaCuadros.add(bloque)

    def update(self):
        self.ListaCuadros.update()

    def draw(self, pantalla):
        self.ListaCuadros.draw(pantalla)

class PicosNivel1(pygame.sprite.Sprite):
    def __init__(self):
        self.ListaPicos = pygame.sprite.Group()
        self.radius=5
        nivel = [[1180, 190],
                 [990, 560],
                 [2200, 420],
                 [3980, 120]
                   ]
        for plataforma in nivel:
            bloque = Pico()
            bloque.rect.x = plataforma[0]
            bloque.rect.y = plataforma[1]
            self.ListaPicos.add(bloque)

    def update(self):
        self.ListaPicos.update()

    def draw(self, pantalla):
        self.ListaPicos.draw(pantalla)

class MonedasNivel1(pygame.sprite.Sprite):
    def __init__(self):
        self.ListaMonedas = pygame.sprite.Group()
        nivel = [[1000, 200],
                 [1400, 450],
                 [1680, 270],
                 [1980, 450],
                 [3080, 440],
                 [3280, 280],
                 [3480, 140],
                 [3780, 440],
                 [3880, 140],
                 [4400, 240],
                 [4500, 440],
                 [4980, 240],
                 [5080, 440],
                 [5380, 440]
                   ]
        for plataforma in nivel:
            bloque = Moneda()
            bloque.rect.x = plataforma[0]
            bloque.rect.y = plataforma[1]
            self.ListaMonedas.add(bloque)

    def update(self):
        self.ListaMonedas.update()

    def draw(self, pantalla):
        self.ListaMonedas.draw(pantalla)

#Cortes de sprites
def cortarSoldadoRazo(imagen):
    imagen2 = pygame.image.load(imagen)
    info2=imagen2.get_rect()
    an_img2=info2[2]
    al_img2 = info2[3]
    #print an_img,al_img
    an_corte2= an_img2/7
    al_corte2=al_img2 /4
    limites2=[7,7,3,3]
    m2=[]
    for y in range(4):
        fila2=[]
        for i in range(limites2[y]):
            cuadro2=imagen2.subsurface(i*an_corte2,y*al_corte2,an_corte2,al_corte2)
            fila2.append(cuadro2)
        m2.append(fila2)
    return m2
def cortarnojugable(imagen):
    imagen2 = pygame.image.load(imagen)
    info2=imagen2.get_rect()
    an_img2=info2[2]
    al_img2 = info2[3]
    #print an_img,al_img
    an_corte2= an_img2/4
    al_corte2=al_img2 /2
    limites2=[1,4]
    m2=[]
    for y in range(2):
        fila2=[]
        for i in range(limites2[y]):
            cuadro2=imagen2.subsurface(i*an_corte2,y*al_corte2,an_corte2,al_corte2)
            fila2.append(cuadro2)
        m2.append(fila2)
    return m2
def cortarestetico(imagen):
    imagen2 = pygame.image.load(imagen)
    info2=imagen2.get_rect()
    an_img2=info2[2]
    al_img2 = info2[3]
    #print an_img,al_img
    an_corte2= an_img2/4
    al_corte2=al_img2 /3
    limites2=[1,4,4]
    m2=[]
    for y in range(3):
        fila2=[]
        for i in range(limites2[y]):
            cuadro2=imagen2.subsurface(i*an_corte2,y*al_corte2,an_corte2,al_corte2)
            fila2.append(cuadro2)
        m2.append(fila2)
    return m2
def cortarjugador(imagen):
    imagen2 = pygame.image.load(imagen)
    info2=imagen2.get_rect()
    an_img2=info2[2]
    al_img2 = info2[3]
    #print an_img,al_img
    an_corte2= an_img2/6
    al_corte2=al_img2 /15
    limites2=[1,1,6,6,4,4,1,1,4,5,4,4,4,1,1]
    m2=[]
    for y in range(15):
        fila2=[]
        for i in range(limites2[y]):
            cuadro2=imagen2.subsurface(i*an_corte2,y*al_corte2,an_corte2,al_corte2)
            fila2.append(cuadro2)
        m2.append(fila2)
    return m2
def cortarBalas(archivo):
    archivo=pygame.image.load(archivo)
    info=archivo.get_rect()
    an_img=info[2]
    al_img = info[3]
    an_corte= an_img/ 1
    al_corte=al_img / 1
    fila=[]
    m=[]
    for y in range(1):
        for i in range(1):
            cuadro=archivo.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m
def cortarBalaNave(archivo):
    archivo=pygame.image.load(archivo)
    info=archivo.get_rect()
    an_img=info[2]
    al_img = info[3]
    an_corte= an_img/ 16
    al_corte=al_img / 2
    fila=[]
    limites=[1,16]
    m=[]
    for y in range(1):
        for i in range(limites[y]):
            cuadro=archivo.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m
def cortarenemigo(archivo):
    archivo=pygame.image.load(archivo)
    info=archivo.get_rect()
    an_img=info[2]
    al_img = info[3]
    an_corte= an_img/ 5
    al_corte=al_img / 1
    fila=[]
    m=[]
    for y in range(1):
        for i in range(5):
            cuadro=archivo.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m
def cortarexplosion(archivo):
    archivo=pygame.image.load(archivo)
    info=archivo.get_rect()
    an_img=info[2]
    al_img = info[3]
    an_corte= an_img/ 16
    al_corte=al_img / 1
    fila=[]
    m=[]
    for y in range(1):
        for i in range(16):
            cuadro=archivo.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m
def cortarnave(archivo):
    #archivo=pygame.image.load(archivo)
    info=archivo.get_rect()
    an_img=info[2]
    al_img = info[3]
    an_corte= an_img/ 4
    al_corte=al_img / 2
    fila=[]
    m=[]
    for y in range(1):
        for i in range(2):
            cuadro=archivo.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m
def cortarfinal(imagen):
    imagen2 = pygame.image.load(imagen)
    info2=imagen2.get_rect()
    an_img2=info2[2]
    al_img2 = info2[3]
    #print an_img,al_img
    an_corte2= an_img2/5
    al_corte2=al_img2 /2
    limites2=[5,3]
    m2=[]
    for y in range(2):
        fila2=[]
        for i in range(limites2[y]):
            cuadro2=imagen2.subsurface(i*an_corte2,y*al_corte2,an_corte2,al_corte2)
            fila2.append(cuadro2)
        m2.append(fila2)
    return m2

if __name__ == '__main__':

    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pygame.display.set_caption("RANDY WARRIOR")
    fondo = pygame.image.load("images/fondo.png")
    vida1 = pygame.image.load('images/0.png').convert_alpha()
    vida2 = pygame.image.load('images/0.png').convert_alpha()
    vida3 = pygame.image.load('images/0.png').convert_alpha()

    MenuX = 410
    MenuY = 478
    DimensionMenu = [MenuX,MenuY]

    #Grupos
    jugadores= pygame.sprite.Group()
    enemigos1=pygame.sprite.Group()
    enemigosnaves=pygame.sprite.Group()
    plataformas= pygame.sprite.Group()
    armas=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balasnaves=pygame.sprite.Group()
    cuadros=pygame.sprite.Group()
    mejoras= pygame.sprite.Group()
    todos= pygame.sprite.Group()
    balasesteticos=pygame.sprite.Group()
    nojugables= pygame.sprite.Group()
    eneesteticos= pygame.sprite.Group()
    picos= pygame.sprite.Group()
    saluds=pygame.sprite.Group()
    soldadosrazos= pygame.sprite.Group()
    muros= pygame.sprite.Group()
    monedas = pygame.sprite.Group()
    velocidades = pygame.sprite.Group()
    finales = pygame.sprite.Group()
    balassoldados = pygame.sprite.Group()
    balasfinales = pygame.sprite.Group()
    #Imagen
    nave = pygame.image.load("images/nave.png")

    #Para recortar al jugador con cuchillo
    imagen = pygame.image.load("images/jugadorCuchillo.png").convert_alpha()
    info=imagen.get_rect()
    an_img=info[2]
    al_img = info[3]

    #print an_img,al_img
    an_corte= an_img/ 6
    al_corte=al_img / 4
    limites=[1,1,6,6]
    m=[]
    x_corte=0
    for y in range(4):
        fila=[]
        for i in range(limites[y]):
            cuadro=imagen.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)

    #Sonidos
    sonidonave=pygame.mixer.Sound('sound/balaNave.ogg')
    sonidojuego=pygame.mixer.Sound('sound/sonidoFondo.ogg')
    sonidomoneda=pygame.mixer.Sound('sound/monedasonido.ogg')


    #Para recortar al jugador con arma
    j=Jugador(m)
    jugadores.add(j)
    todos.add(j)

    #Para crear salud
    salud=Salud()
    saluds.add(salud)
    todos.add(salud)

    #Para crear velocidad
    velocidad=Velocidad()
    velocidades.add(velocidad)
    todos.add(velocidad)

    # Crear jugador no jugable
    nojuga=cortarnojugable("images/nojugable.png")
    nojugab=nojugable(nojuga)
    nojugab.rect.y=590
    nojugab.rect.x=370
    nojugables.add(nojugab)
    todos.add(nojugab)

    # Crear jugador no jugable final
    nojugab2=nojugable(nojuga)
    nojugab2.rect.y=140
    nojugab2.rect.x=4000
    nojugables.add(nojugab2)
    todos.add(nojugab2)

    #Crear soldados razos
    soldadorazo=cortarSoldadoRazo("images/soldadorazo.png")
    soldadorazo1=SoldadoRazo(soldadorazo)
    soldadorazo1.rect.x=1090
    soldadorazo1.rect.y=220
    soldadosrazos.add(soldadorazo1)
    todos.add(soldadorazo1)

    soldadorazo2=SoldadoRazo(soldadorazo)
    soldadorazo2.rect.x=1900
    soldadorazo2.rect.y=460
    soldadosrazos.add(soldadorazo2)
    todos.add(soldadorazo2)

    #Crear enemigo final
    cfinal=cortarfinal("images/final.png")
    final=final(cfinal)
    final.rect.x=5700
    final.rect.y=600
    finales.add(final)
    todos.add(final)

    #Crear enemigo eneestetico
    eneest=cortarestetico("images/enemigoEstatico.png")
    enemigoesta=eneestatico(eneest)
    enemigoesta.rect.x=700
    enemigoesta.rect.y=590
    eneesteticos.add(enemigoesta)
    todos.add(enemigoesta)

    soldadoEstatico2=eneestatico(eneest)
    soldadoEstatico2.rect.x=2900
    soldadoEstatico2.rect.y=430
    eneesteticos.add(soldadoEstatico2)
    todos.add(soldadoEstatico2)

    soldadoEstatico3=eneestatico(eneest)
    soldadoEstatico3.rect.x=3300
    soldadoEstatico3.rect.y=130
    eneesteticos.add(soldadoEstatico3)
    todos.add(soldadoEstatico3)

    soldadoEstatico4=eneestatico(eneest)
    soldadoEstatico4.rect.x=3600
    soldadoEstatico4.rect.y=430
    eneesteticos.add(soldadoEstatico4)
    todos.add(soldadoEstatico4)

    soldadoEstatico5=eneestatico(eneest)
    soldadoEstatico5.rect.x=4200
    soldadoEstatico5.rect.y=190
    eneesteticos.add(soldadoEstatico5)
    todos.add(soldadoEstatico5)

    #Crear enemigo 1
    ene1=cortarenemigo("images/robot.png")
    e1=Enemigo1(ene1)
    e1.rect.y=450
    e1.rect.x=1100
    enemigos1.add(e1)
    todos.add(e1)

    moto2=Enemigo1(ene1)
    moto2.rect.y=450
    moto2.rect.x=3800
    enemigos1.add(moto2)
    todos.add(moto2)

    moto3=Enemigo1(ene1)
    moto3.rect.y=450
    moto3.rect.x=4600
    enemigos1.add(moto3)
    todos.add(moto3)

    moto4=Enemigo1(ene1)
    moto4.rect.y=250
    moto4.rect.x=4980
    enemigos1.add(moto4)
    todos.add(moto4)

    #Crear enemigo nave
    ene2=cortarnave(nave)
    e2=EnemigoNave(ene2)
    e2.rect.y=50
    e2.rect.x=800
    enemigosnaves.add(e2)
    todos.add(e2)

    #Crear enemigo nave 2
    e3=EnemigoNave(ene2)
    e3.rect.y=90
    e3.rect.x=3200
    enemigosnaves.add(e3)
    todos.add(e3)

    #Crear arma jugador
    arma=Arma()
    armas.add(arma)
    todos.add(arma)

    #Crear las plataformas
    p=Plataforma()
    p.rect.x =0
    p.rect.y =630
    plataformas.add(p)
    todos.add(p)

    #
    p2=Plataforma()
    p2.rect.x=600
    p2.rect.y=630
    plataformas.add(p2)
    todos.add(p2)

    #Crear plataforma
    pl=PlataformasNivel1()
    plataformas.add(pl.ListaPlataformas)
    todos.add(pl.ListaPlataformas)

    #Crear cuadros
    cua=CuadrosNivel1()
    cuadros.add(cua.ListaCuadros)
    todos.add(cua.ListaCuadros)

    #Crear monedas
    moneda=MonedasNivel1()
    monedas.add(moneda.ListaMonedas)
    todos.add(moneda.ListaMonedas)

    #Crear Picos
    pic=PicosNivel1()
    picos.add(pic.ListaPicos)
    todos.add(pic.ListaPicos)

    mejora1=mejora1()
    mejora2=mejora2()
    mejora3=mejora3()
    mejoras.add(mejora1)
    mejoras.add(mejora2)
    mejoras.add(mejora3)
    todos.add(mejora1)
    todos.add(mejora2)
    todos.add(mejora3)

fin=False
reloj=pygame.time.Clock()
Fuente=pygame.font.Font(None,34)
seg=0
tasa=15
limite=120
tipoarma=0
creditos=0
mejora=0
eliminados=0
sonidomuerteenemigo=pygame.mixer.Sound('sound/death.ogg')
sonidodolor=pygame.mixer.Sound('sound/ouch.ogg')
pos_x=0
vel_xx=0
velpla=0
menu=Menu()
menu.menuInicial()
while not  fin:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                j.accion=2
                j.vel_x=10
                # if j.rect.right == (ancho - 700):
                #     j.vel_x=10
                #     p.vel_xx=-2
                #     p2.vel_xx=-2
                # elif j.rect.x == (ancho-750):
                #     p.vel_xx=-2
                #     p2.vel_xx=-2
            if event.key == pygame.K_LEFT:
                j.accion=3
                j.vel_x=-10
            if event.key == pygame.K_p:
                j.accion=10
            if event.key == pygame.K_UP:
                if j.accion == 0 or j.accion ==2:
                    j.accion=13
                if j.accion == 1 or j.accion == 3:
                    j.accion=14
            if event.key == pygame.K_x:
                b=0
                if j.accion == 13:
                    if mejora==0:
                        misil = cortarBalas("images/bala.png")
                        e=Bala(misil)
                    if mejora==1:
                        misil = cortarBalas("images/bala2.png")
                        e=Bala(misil)
                    if mejora==2:
                        misil = cortarBalas("images/bala3.png")
                        e=Bala(misil)
                    if mejora==3:
                        misil = cortarBalas("images/bala4.png")
                        e=Bala(misil)
                    e.sonido.play()
                    e.vel_y=30
                    balas.add(e)
                    e.rect.x=j.rect.x
                    e.rect.y=j.rect.y+20
                    todos.add(e)
                if j.accion == 14:
                    if mejora==0:
                        misil = cortarBalas("images/bala.png")
                        e=Bala(misil)
                    if mejora==1:
                        misil = cortarBalas("images/bala2.png")
                        e=Bala(misil)
                    if mejora==2:
                        misil = cortarBalas("images/bala3.png")
                        e=Bala(misil)
                    if mejora==3:
                        misil = cortarBalas("images/bala4.png")
                        e=Bala(misil)
                    e.sonido.play()
                    e.vel_y=30
                    e.vel_x=-20
                    balas.add(e)
                    e.rect.x=j.rect.x
                    e.rect.y=j.rect.y
                    todos.add(e)
                if j.accion == 2 or j.accion == 0:
                    j.accion=4
                    if mejora==0:
                        misil = cortarBalas("images/bala.png")
                        e=Bala(misil)
                    if mejora==1:
                        misil = cortarBalas("images/bala2.png")
                        e=Bala(misil)
                    if mejora==2:
                        misil = cortarBalas("images/bala3.png")
                        e=Bala(misil)
                    if mejora==3:
                        misil = cortarBalas("images/bala4.png")
                        e=Bala(misil)
                    balas.add(e)
                    e.sonido.play()
                    e.rect.x=j.rect.x
                    e.rect.y=j.rect.y+15
                    todos.add(e)
                if j.accion == 1 or j.accion == 3:
                    j.accion=5
                    if mejora==0:
                        misil = cortarBalas("images/bala.png")
                        e=Bala(misil)
                    if mejora==1:
                        misil = cortarBalas("images/bala2.png")
                        e=Bala(misil)
                    if mejora==2:
                        misil = cortarBalas("images/bala3.png")
                        e=Bala(misil)
                    if mejora==3:
                        misil = cortarBalas("images/bala4.png")
                        e=Bala(misil)
                    balas.add(e)
                    e.sonido.play()
                    e.vel_x=-20
                    e.rect.x=j.rect.x
                    e.rect.y=j.rect.y+20
                    todos.add(e)
            if event.key == pygame.K_SPACE:
                if j.accion == 2:
                    j.accion=6
                if j.accion == 3:
                    j.accion=7
                j.rect.y +=-100
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                j.vel_x=0
                j.accion=0
            if event.key == pygame.K_LEFT:
                j.accion=1
                j.vel_x=0
            if event.key == pygame.K_x:
                if j.accion == 4:
                    j.accion=0
                if j.accion == 5:
                    j.accion=1
            if event.key == pygame.K_SPACE:
                j.rect.y +=0

    #Logica
    if j.rect.x==(e2.rect.x-500):
        e2.vel_x=-5
    #Enemigo estatico 1
    if j.rect.x ==(enemigoesta.rect.x-200):
        enemigoesta.accion=2
        balaestatico=cortarBalas("images/balaEstatico.png")
        b=Balaestatico(balaestatico)
        b.vel_x=-10
        b.rect.x = enemigoesta.rect.x
        b.rect.y = enemigoesta.rect.y+20
        balasesteticos.add(b)
        todos.add(b)

    #Colisiones jugador y la plataforma
    col_p= pygame.sprite.spritecollide(j,plataformas,False)
    for p in col_p:
        if j.rect.bottom > p.rect.top:
            j.rect.bottom = p.rect.top
            j.vel_y = 0
            if j.accion==6:
                j.accion=2
            if j.accion==7:
                j.accion=3

    # dialogo=Fuente.render("Hey,buena suerte campeon",False,Verde)
    #Colision jugador con el jugador nojugable
    col_noju= pygame.sprite.spritecollide(j,nojugables,False)
    for e in col_noju:
        # pantalla.blit(dialogo,[100,400])
        # pygame.display.flip()
        e.accion=1

    #Colision jugador con balasestetico
    for b in balasesteticos:
        if b.rect.x < 0:
            balasesteticos.remove(b)
            todos.remove(b)
        if b.rect.x > ancho:
            balasesteticos.remove(b)
            todos.remove(b)
        ls_balas_e=pygame.sprite.spritecollide(b,jugadores,False)
        for j in ls_balas_e:
            j.salud-=1
            balasesteticos.remove(b)
            todos.remove(b)

    #Colision jugador con mejoras
    col_mej1= pygame.sprite.spritecollide(j,mejoras,True)
    for e in col_mej1:
        mejora1.sonido.play()
        mejora+=1
        mejoras.remove(e)
        todos.remove(e)

    #Colision jugador con salud
    col_salud= pygame.sprite.spritecollide(j,saluds,True)
    for e in col_salud:
        mejora1.sonido.play()
        j.salud+=1
        saluds.remove(e)
        todos.remove(e)

    #Colision jugador con velocidad
    col_velocidad= pygame.sprite.spritecollide(j,velocidades,True)
    for e in col_velocidad:
        mejora1.sonido.play()
        j.vel_x=6
        velocidades.remove(e)
        todos.remove(e)

    #Colision jugador con moneda
    col_moneda= pygame.sprite.spritecollide(j,monedas,True)
    for e in col_moneda:
        sonidomoneda.play()
        creditos+=3
        monedas.remove(e)
        todos.remove(e)

    #Colision jugador con cuadro
    col_c= pygame.sprite.spritecollide(j,cuadros,False)
    for c in col_c:
        if j.rect.bottom > c.rect.top:
            j.rect.bottom = c.rect.top


    #Colision enemigo cuados
    col_e= pygame.sprite.spritecollide(e1,cuadros,False)
    for e in col_e:
        if e.rect.bottom > e1.rect.top:
            e1.vel_x = 0
            # if j.accion==6:
            #     j.accion=2
            # if j.accion==7:
            #     j.accion=3

    #Colision bala con jugador
    col_bajug=pygame.sprite.spritecollide(j,balasnaves,False)
    for e in col_bajug:
        j.salud-=1
        sonidodolor.play()
        balasnaves.remove(e)
        sonidonave.play()
        todos.remove(e)

    #Balas enemigos naves
    for e in enemigosnaves:
        if e.disparar:
         balanave=cortarBalas("images/balanave.png")
         b=BalaNave(balanave)
         b.vel_y=10
         b.rect.x = e.rect.x
         b.rect.y = e.rect.y+20
         balasnaves.add(b)
         todos.add(b)
         e.disparar=False
         e.tempdis=random.randrange(150)

    #Balas soldado razo
    for e in soldadosrazos:
        if e.disparar:
         balasoldado=cortarBalas("images/balaEstatico.png")
         c=BalaSoldado(balasoldado)
         c.vel_x=7
         c.rect.x = e.rect.x
         c.rect.y = e.rect.y+20
         balassoldados.add(c)
         todos.add(c)
         e.disparar=False
         e.tempdis=random.randrange(150)

    #Balas enemigo final
    for e in finales:
        if e.disparar:
         balaf=cortarBalas("images/balafinal.png")
         d=Balafinal(balaf)
         d.vel_x=-7
         d.rect.x = e.rect.x
         d.rect.y = e.rect.y+40
         balasfinales.add(d)
         todos.add(d)
         e.disparar=False
         e.tempdis=random.randrange(150)

    #Colision plataforma con balanave
    for b in balasnaves:
        col_balN= pygame.sprite.spritecollide(b,plataformas,False)
        for e in col_balN:
            if b.rect.bottom > e.rect.top:
                balasnaves.remove(b)
                sonidonave.play()
                todos.remove(b)
#---------------------COLISIONES SOLDADO RAZO--------------------------------------------------------
#Colision cuadros con SoldadoRazo
    for b in cuadros:
        col_balsol= pygame.sprite.spritecollide(b,soldadosrazos,False)
        for e in col_balsol:
            if b.rect.right > e.rect.left:
                e.accion=1
                e.vel_x+=2

    #Colision plataformas con SoldadoRazo
    for b in plataformas:
        col_balpla= pygame.sprite.spritecollide(b,soldadosrazos,False)
        for e in col_balpla:
            if b.rect.top > e.rect.bottom:
                b.rect.top = e.rect.bottom

    #colision picos con soldado razo
    for b in picos:
        col_balpic= pygame.sprite.spritecollide(b,soldadosrazos,False)
        for e in col_balpic:
            if b.rect.left < e.rect.right:
                e.accion=0
                e.vel_x-=2

    #Colision balas soldados razos con cuadros
    for b in balassoldados:
        col_bals= pygame.sprite.spritecollide(b,cuadros,False)
        for e in col_bals:
            if b.rect.left < e.rect.right or b.rect.left > e.rect.right:
                balassoldados.remove(b)
                sonidonave.play()
                todos.remove(b)

#----------------------COLISION SOLDADO ESTATICO---------------------------------------------


#---------------------COLISIONES MOTO--------------------------------------------------------
    #colision picos con moto
    for b in picos:
        col_balpic2= pygame.sprite.spritecollide(b,enemigos1,False)
        for e in col_balpic2:
            if b.rect.right < e.rect.left:
               b.rect.right < e.rect.left

    #Colision plataformas con moto
    for b in enemigos1:
        col_balpla2= pygame.sprite.spritecollide(b,plataformas,False)
        for e in col_balpla2:
            if b.rect.bottom > e.rect.top:
               b.rect.bottom = e.rect.top
               b.vel_y=0

    #Colision cuadros con moto
    for b in cuadros:
            col_balsol2= pygame.sprite.spritecollide(b,enemigos1,False)
            for e in col_balsol2:
                if b.rect.right > e.rect.left:
                   b.rect.right = e.rect.left
                   e.vel_x=0

    #Colision jugador con moto
    col_balsol3= pygame.sprite.spritecollide(j,enemigos1,True)
    for e in col_balsol3:
            if j.rect.right > e.rect.left:
                j.salud-=1
                sonidomuerteenemigo.play()
                enemigos1.remove(e)
                todos.remove(e)

    #Colision jugador con balafinen
    col_balfin= pygame.sprite.spritecollide(j,balasfinales,True)
    for e in col_balfin:
            if j.rect.right > e.rect.left:
                j.salud-=1
                sonidomuerteenemigo.play()
                balasfinales.remove(e)
                todos.remove(e)

    #Colision jugador con balas soldado razo
    col_balsol2= pygame.sprite.spritecollide(j,balassoldados,True)
    for e in col_balsol2:
            if j.rect.right > e.rect.left:
                j.salud-=1
                sonidomuerteenemigo.play()
                balasfinales.remove(e)
                todos.remove(e)

    #Colision jugador con balas soldado razo
    col_balsol3= pygame.sprite.spritecollide(j,balasfinales,True)
    for e in col_balsol3:
            if j.rect.right > e.rect.left:
                j.salud-=1
                sonidomuerteenemigo.play()
                balasfinales.remove(e)
                todos.remove(e)

    #Colision jugador con picos
    col_balsol4= pygame.sprite.spritecollide(j,picos,False)
    for e in col_balsol4:
            if j.rect.right > e.rect.left or j.rect.bottom > e.rect.top or j.rect.left > e.rect.right or j.rect.top > e.rect.bottom:
                j.rect.x = e.rect.x-300
                sonidodolor=pygame.mixer.Sound('sound/ouch.ogg')
                sonidodolor.play()
                j.salud-=1

    #Colision balasjugador con naveliminados
    for b in balas:
        ls_colbalas=pygame.sprite.spritecollide(b,enemigosnaves,True)
        for e in ls_colbalas:
            e.salud-=1
            sonidomuerteenemigo.play()
            balas.remove(b)
            todos.remove(b)
            creditos+=10
            eliminados+=1

    #Colision balasjugador con enemigo1
    for b in balas:
        if b.rect.x > ancho:

            balas.remove(b)
            todos.remove(b)
        if b.rect.y < 0:
            balas.remove(b)
            todos.remove(b)
            sonidomuerteenemigo.play()
        ls_colbalas1=pygame.sprite.spritecollide(b,enemigos1,True)
        for e in ls_colbalas1:
            e.salud-=1
            balas.remove(b)
            todos.remove(b)
            creditos+=2
            eliminados+=1

    #Colision balasjugador con soldado estatico
    for b in balas:
        if b.rect.x > ancho:
            balas.remove(b)
            todos.remove(b)
        if b.rect.y < 0:
            balas.remove(b)
            todos.remove(b)
        ls_colbalas3=pygame.sprite.spritecollide(b,eneesteticos,True)
        for e in ls_colbalas3:
            e.salud-=1
            sonidodolor.play()
            balas.remove(b)
            todos.remove(b)
            creditos+=2
            eliminados+=1

    #Colision balasjugador con soldado razo
    for b in balas:
        if b.rect.x > ancho:
            balas.remove(b)
            todos.remove(b)
        if b.rect.y < 0:
            balas.remove(b)
            todos.remove(b)
        ls_colbalas4=pygame.sprite.spritecollide(b,soldadosrazos,True)
        for e in ls_colbalas4:
            e.salud-=1
            balas.remove(b)
            todos.remove(b)
            sonidomuerteenemigo.play()
            creditos+=2
            eliminados+=1

    #Colicion cuadros con balas
    for b in balasnaves:
        col_balC= pygame.sprite.spritecollide(b,cuadros,False)
        for e in col_balC:
            if b.rect.bottom > e.rect.top:
                balasnaves.remove(b)
                sonidonave.play()
                todos.remove(b)

    #Colision jugador y del arma
    col_arma= pygame.sprite.spritecollide(j,armas,True)
    for e in col_arma:
        armas.remove(e)
        todos.remove(e)
        jugadores.remove(j)
        todos.remove(j)
        arma.sonido.play()
        tipoarma=1

        #Aparece jugadorConArma
        jugadorarma=cortarjugador("images/jugadorArma.png")
        j=Jugador(jugadorarma)
        jugadores.add(j)
        todos.add(j)
        j.rect.x=270
        j.rect.y=550

    #Colision balas jugador con enemigo final
    for b in balas:
        if b.rect.x > ancho:
            balas.remove(b)
            todos.remove(b)
        if b.rect.y < 0:
            balas.remove(b)
            todos.remove(b)
        ls_colbalas5=pygame.sprite.spritecollide(b,finales,True)
        for e in ls_colbalas5:
            e.salud-=1
            balas.remove(b)
            todos.remove(b)
            sonidomuerteenemigo.play()
            creditos+=2
            eliminados+=1

    if e2.rect.x > ancho:
        e2.vel_x-=5
    if e2.rect.x < 0:
        e2.vel_x+=5

    if j.rect.x >=(soldadoEstatico2.rect.x-200):
        soldadoEstatico2.accion=2
        balaestatico=cortarBalas("images/balaEstatico.png")
        b=Balaestatico(balaestatico)
        b.vel_x=-10
        b.rect.y = soldadoEstatico2.rect.y+20
        b.rect.x = soldadoEstatico2.rect.x
        balasesteticos.add(b)
        todos.add(b)

    if j.rect.x >=(soldadoEstatico3.rect.x-200):
        soldadoEstatico3.accion=2
        balaestatico=cortarBalas("images/balaEstatico.png")
        b=Balaestatico(balaestatico)
        b.vel_x=-10
        b.rect.x = soldadoEstatico3.rect.x
        b.rect.y = soldadoEstatico3.rect.y+20
        balasesteticos.add(b)
        todos.add(b)

    if j.rect.x >=(soldadoEstatico4.rect.x-200):
        soldadoEstatico4.accion=2
        balaestatico=cortarBalas("images/balaEstatico.png")
        b=Balaestatico(balaestatico)
        b.vel_x=-10
        b.rect.x = soldadoEstatico4.rect.x
        b.rect.y = soldadoEstatico4.rect.y+20
        balasesteticos.add(b)
        todos.add(b)

    if j.rect.x >=(soldadoEstatico5.rect.x-200):
        soldadoEstatico5.accion=2
        balaestatico=cortarBalas("images/balaEstatico.png")
        b=Balaestatico(balaestatico)
        b.vel_x=-10
        b.rect.x = soldadoEstatico5.rect.x
        b.rect.y = soldadoEstatico5.rect.y+20
        balasesteticos.add(b)
        todos.add(b)

    # if e3.rect.x > ancho:
    #     e3.vel_x-=5
    # if e3.rect.x < 0:
    #     e3.vel_x+=5

    # Si el jugador se sale de la pantalla
    if j.rect.y > alto:
        j.salud=0
        jugadores.remove(j)
        todos.remove(j)
        sonidodolor.play()



    if j.rect.x < 0:
        j.vel_x=0
        j.rect.x=0
    if j.rect.x > (ancho - 700):
        j.rect.x=ancho-700
        j.vel_x=0

    if j.rect.right >= 640:
        vel_xx=0
    if j.rect.left >= 639:
        vel_xx=-8

        # p.vel_x=+2
    #     # p2.vel_x=+2
    # elif j.rect.x == 300:
    #     vel_x=+2
    # else:
    #     vel_x=0

    creditot=Fuente.render("Creditos:",False,Blanco)
    credito=Fuente.render(str(creditos),False,Blanco)

    muertost=Fuente.render("Muertos:",False,Blanco)
    muerto=Fuente.render(str(eliminados),False,Blanco)

    texto=Fuente.render("Tiempo",False,Blanco)
    tipocuchillo=Fuente.render("Arma: Cuchillo",False,Blanco)
    tipopistola=Fuente.render("Arma: AK-47",False,Rojo)

    segundo= limite - (seg // tasa)
    txt_reloj='{0:00} '.format(segundo)
    texto_reloj=Fuente.render(txt_reloj,True,Blanco)

    todos.update()
    pantalla.fill(Negro)
    pantalla.blit(fondo,[pos_x,0])
    pos_x+=vel_xx
    todos.draw(pantalla)

    if tipoarma ==0:
        pantalla.blit(tipocuchillo,[220,10])
    if tipoarma ==1:
        pantalla.blit(tipopistola,[220,10])

    #Vida del jugador
    if j.salud == 1:
      pantalla.blit(vida1,(20,20))
    elif j.salud == 2:
      pantalla.blit(vida1,(20,20))
      pantalla.blit(vida2,(80,20))
    elif j.salud == 3:
      pantalla.blit(vida1,(20,20))
      pantalla.blit(vida2,(80,20))
      pantalla.blit(vida3,(140,20))

    if j.salud ==0:
        game_over = gaste =pygame.image.load('images/game_over.png').convert_alpha()
        pantalla.blit(game_over,[200,50])
        pygame.display.flip()
        reloj.tick(0.2)
        fin=True
    if final.salud ==0:
        gano=Fuente.render("GANASTE",False,Blanco)
        pantalla.blit(gano,[400,360])

    if txt_reloj ==0:
        game_over2 = gaste =pygame.image.load('images/game_over.png').convert_alpha()
        pantalla.blit(game_over2,[40,40])
        pygame.display.flip()
        reloj.tick(0.2)
        fin=True
    pantalla.blit(texto,[540,10])
    pantalla.blit(texto_reloj,[560,40])
    pantalla.blit(creditot,[900,10])
    pantalla.blit(credito,[1020,10])
    pantalla.blit(muertost,[700,10])
    pantalla.blit(muerto,[820,10])
    pygame.display.flip()
    reloj.tick(15)
    seg+=1
