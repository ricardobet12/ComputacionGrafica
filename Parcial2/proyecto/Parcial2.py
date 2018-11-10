import pygame
import random

ancho = 1200
alto = 600

class Jugador(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.salud=3
        self.rect.y=0
        self.var_y=0
        self.var_x=0
        self.con=0
    def update(self):
        self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

        if self.con<2:
            self.con+=1
        else:
            self.con=0

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=1
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.zombies=pygame.mixer.Sound('zombies.ogg')
        #self.zombies.play()
        self.rect.y=500
        self.rect.x=850
        self.vel_x=-2
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
            self.rect.x+=self.vel_x

        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class Enemigo2(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.motosierra=pygame.mixer.Sound('Motosierra.ogg')
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=500
        self.rect.x=850
        self.vel_x=-5
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
            self.rect.x+=self.vel_x

        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class EnemigoFinal(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.rect = self.image.get_rect()
        self.i=0
        self.rect.y=600
        self.rect.x=850
        self.vel_x=-5
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
            self.rect.x+=self.vel_x

        if self.rect.x == 10:
            print 'dd'

        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class Bala(pygame.sprite.Sprite):
    def __init__(self,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.accion=0
        self.image= self.m[self.accion][0]
        self.image.fill([255,255,255])
        self.i=0
        self.grito=pygame.mixer.Sound('sonidoJugador.ogg')
        self.grito.play()
        self.rect = self.image.get_rect()
        self.vel_x=100
    def update(self):
        self.rect.x+=self.vel_x
        self.i+=1
        if self.i >= len(self.m[self.accion]):
            self.i=0
        self.image=self.m[self.accion][self.i]

class BalaE(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([15,5])
        self.image.fill([255,255,255])
        self.i=0
        self.rect = self.image.get_rect()
        self.vel_x=10
    def update(self):
        self.rect.x+=self.vel_x
        # self.i+=1
        # if self.i >= len(self.m[self.accion]):
        #     self.i=0
        # self.image=self.m[self.accion][self.i]

class aumentoVida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("pizza.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y=20
        self.rect.x=100
        self.rect.y=-40
        self.temp= random.randrange(300)
    def update(self):
        if self.temp > 0:
            self.temp-=1
        else:
            self.rect.y+=self.vel_y

class aumentoVelocidad(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load("lataGaseosa.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.vel_y=20
        self.rect.x=80
        self.rect.y=-40
        self.temp= random.randrange(300)
    def update(self):
        if self.temp > 0:
            self.temp-=1
        else:
            self.rect.y+=self.vel_y

def cortar(archivo):
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

def cortaref(archivo):
    archivo=pygame.image.load(archivo)
    info=archivo.get_rect()
    an_img=info[2]
    al_img = info[3]
    an_corte= an_img/ 4
    al_corte=al_img / 1
    fila=[]
    m=[]
    for y in range(1):
        for i in range(4):
            cuadro=archivo.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)
    return m



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

if __name__ == '__main__':
    #Definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    fondo=pygame.image.load('fondo.jpg')

    #GRUPOS
    todos=pygame.sprite.Group()
    jugadores=pygame.sprite.Group()
    enemigos=pygame.sprite.Group()
    enemigos2=pygame.sprite.Group()
    enemigosf=pygame.sprite.Group()
    pizzas=pygame.sprite.Group()
    gaseosas=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_e=pygame.sprite.Group()

    #crear pizza
    piza=aumentoVida()
    piza.rect.x =random.randrange(ancho)
    pizzas.add(piza)
    todos.add(piza)

    #crear gaseosa
    gas=aumentoVelocidad()
    gas.rect.x =random.randrange(ancho)
    gaseosas.add(gas)
    todos.add(gas)

    fuente=pygame.font.Font(None,25)
    texto1=fuente.render("Jugador 1:",False,[255,255,255])
    texto2=fuente.render("Jugador 2:",False,[100,255,255])

    imagen = pygame.image.load("jugador1.png").convert_alpha()
    imagen2= pygame.image.load("jugador2.png").convert_alpha()
    imagen3= pygame.image.load("enemigo.png").convert_alpha()
    imagen4= pygame.image.load("Bala.png").convert_alpha()
    imagen5= pygame.image.load("boss1.png").convert_alpha()
    info=imagen.get_rect()
    info2=imagen3.get_rect()
    info3=imagen4.get_rect()

    #Para recorte imagen4
    an_img4=info3[2]
    al_img4=info3[3]
    an_corte4=an_img4/8
    al_corte4=al_img4/4

    an_img3=info2[2]
    al_img3=info2[3]

    an_corte3=an_img3/9
    al_corte3=al_img3/4

    an_img=info[2]
    al_img = info[3]
    #print an_img,al_img
    an_corte= an_img/ 4
    al_corte=al_img / 4
    limites=[4,4,4,4]
    limites2=[8,8,8,8]
    limites3=[8,4,7,4]
    m=[]
    m2=[]
    m3=[]
    m4=[]
    go=False
    x_corte=0
    for y in range(4):
        fila=[]
        for i in range(limites[y]):
            cuadro=imagen.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila.append(cuadro)
        m.append(fila)

    for y in range(4):
        fila2=[]
        for i in range(limites[y]):
            cuadro2=imagen2.subsurface(i*an_corte,y*al_corte,an_corte,al_corte)
            fila2.append(cuadro2)
        m2.append(fila2)

    for y in range(4):
        fila3=[]
        for i in range(limites2[y]):
            cuadro3=imagen3.subsurface(i*an_corte3,y*al_corte3,an_corte3,al_corte3)
            fila3.append(cuadro3)
        m3.append(fila3)

    #Crear los enemigos esqueletes
    num_enemigos=15
    for i in range(num_enemigos):
        e=Enemigo(m3)
        e.rect.x=random.randrange(900,1600)
        e.rect.y=random.randrange(450,530)
        enemigos.add(e)
        todos.add(e)

    #Crear enemigos 2
    num_enemigos2=5
    for i in range(num_enemigos2):
        ene=cortar('boss1.png')
        e2=Enemigo2(ene)
        e2.rect.x=random.randrange(1500,1800)
        e2.rect.y=random.randrange(450,530)
        enemigos.add(e2)
        todos.add(e2)

    #Crear enemigo final
    ef=cortaref('boss2.png')
    e3=EnemigoFinal(ef)
    e3.rect.x=random.randrange(1700,1800)
    e3.rect.y=random.randrange(390,400)
    enemigosf.add(e3)
    todos.add(e3)

    jugador=Jugador(m)
    jugador2=Jugador(m2)
    jugador.rect.y=500
    jugador.rect.x=80
    jugador2.rect.y=500
    jugador2.rect.x=30
    todos.add(jugador)
    jugadores.add(jugador)
    jugadores.add(jugador2)
    todos.add(jugador2)

    musica_f=pygame.mixer.Sound('nivel1.ogg')
    musica_f.play()
    reloj=pygame.time.Clock()
    con=0
    fin=False
    go=False
    velFond_x=0
    posFond_x=0
    while not  fin:
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x=+20
                    jugador.var_y=0
                    jugador.accion=2
                if event.key == pygame.K_LEFT:
                    jugador.var_x=-20
                    jugador.var_y=0
                    jugador.accion=1
                if event.key == pygame.K_DOWN:
                    jugador.var_y=+20
                    jugador.var_x=0
                    jugador.accion=0
                if event.key == pygame.K_UP:
                    jugador.var_y=-20
                    jugador.var_x=0
                    jugador.accion=3
                if event.key == pygame.K_SPACE:
                    misil = cortarBalas("Bala.png")
                    e=Bala(misil)
                    e.rect.x = jugador.rect.x
                    e.rect.y = jugador.rect.y+20
                    balas.add(e)
                    todos.add(e)

                if event.key == pygame.K_d:
                    jugador2.var_x=+20
                    jugador2.var_y=0
                    jugador2.accion=2
                if event.key == pygame.K_a:
                    jugador2.var_x=-20
                    jugador2.var_y=0
                    jugador2.accion=1
                if event.key == pygame.K_s:
                    jugador2.var_y=+20
                    jugador2.var_x=0
                    jugador2.accion=0
                if event.key == pygame.K_w:
                    jugador2.var_y=-20
                    jugador2.var_x=0
                    jugador2.accion=3
                if event.key == pygame.K_p:
                    misil2 = cortar("Bala.png")
                    f=Bala(misil2)
                    f.rect.x = jugador2.rect.x+15
                    f.rect.y = jugador2.rect.y+ 25
                    balas.add(f)
                    todos.add(f)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    jugador.var_x=0
                    jugador.var_y=0
                if event.key == pygame.K_LEFT:
                    jugador.var_x=0
                    jugador.var_y=0
                if event.key == pygame.K_DOWN:
                    jugador.var_x=0
                    jugador.var_y=0
                if event.key == pygame.K_UP:
                    jugador.var_x=0
                    jugador.var_y=0
                if event.key == pygame.K_d:
                    jugador2.var_x=0
                    jugador2.var_y=0
                if event.key == pygame.K_a:
                    jugador2.var_x=0
                    jugador2.var_y=0
                if event.key == pygame.K_s:
                    jugador2.var_x=0
                    jugador2.var_y=0
                if event.key == pygame.K_w:
                    jugador2.var_x=0
                    jugador2.var_y=0

        jugador.image=m[0+jugador.con][jugador.accion]
        jugador2.image=m2[0+jugador2.con][jugador2.accion]

        #Limites jugadores
        if jugador.rect.x < 10:
            jugador.vel_x=0
            jugador.rect.x=5
        if jugador2.rect.x < 10:
            jugador2.vel_x=0
            jugador2.rect.x=5
        if jugador.rect.y >= alto-60:
            jugador.rect.y=alto-60
            jugador.vel_y=0
        if jugador2.rect.y >= alto-60:
            jugador2.rect.y=alto-60
            jugador2.vel_y=0
        if jugador.rect.x > (ancho - jugador.rect.width):
            jugador.rect.x=ancho-jugador.rect.width
            jugador.vel_x=0
        if(jugador.rect.y <=450):
            jugador.rect.y=450
        if(jugador2.rect.y <=450):
            jugador2.rect.y=450

        if(jugador.rect.x >= 400 and jugador2.rect.x >= 400):
            velFond_x=-8
        elif(jugador.rect.x <= 10 and jugador2.rect.x <= 10):
            velFond_x=+8
        else:
            velFond_x=0

        #Colision jugador con la pizza
        pizza_eliminados=0
        ls_colb=pygame.sprite.spritecollide(jugador,pizzas,True)
        for e in ls_colb:
            pizzas.remove(e)
            todos.remove(e)
            pizza_eliminados+=1
            jugador.salud+=1

        for i in range(pizza_eliminados):
            if pizza_eliminados==1:
                pizza=aumentoVida()
                pizza.rect.x = jugador.rect.x
                pizza.temp=20
                pizzas.add(pizza)
                todos.add(pizza)
            else:
                pizza_eliminados=0

         # # PIZZAS FUERA DE LA PANTALLA
         #   if pizza.rect.y == alto:
         #       pizzas.remove(pizza)
         #       todos.remove(pizza)
         #       pizza_eliminados+=1
         #       print pizza_eliminados

        #Colision jugador con la gaseosa
        gaseosa_eliminados=0
        ls_colg=pygame.sprite.spritecollide(jugador,gaseosas,True)
        for e in ls_colg:
            gaseosas.remove(e)
            todos.remove(e)
            gaseosa_eliminados+=1
            #jugador.var_y=3

        for i in range(gaseosa_eliminados):
            if gaseosa_eliminados==1:
                gas=aumentoVelocidad()
                gas.rect.x = jugador.rect.x
                gas.temp=20
                gaseosas.add(gas)
                todos.add(gas)
            else:
                gaseosa_eliminados=0

            #GASEOSAS FUERA DE LA PANTALLA
             # if gas.rect.y == 400:
             #     gaseosas.remove(gas)
             #     todos.remove(gas)
             #     gaseosa_eliminados+=1

        #Colision de jugadores con moustro EnemigoFinal
        eliminados=0
        ptos=0
        ls_col = pygame.sprite.spritecollide(jugador,enemigos,True)
        for e in ls_col:
            ptos+=1
            e.salud-=1
            enemigos.remove(e)
            todos.remove(e)
            eliminados+=1

        #Colision de Balas
        for b in balas:
            ls_colb=pygame.sprite.spritecollide(b,enemigos,False)
            for e in ls_colb:
                e.salud-=1
                balas.remove(b)
                todos.remove(b)
                eliminados+=1
        #Balas enemigos
        for e in enemigos:
            if e.disparar:
             b=BalaE()
             b.vel_x=-10
             b.rect.x = e.rect.x
             b.rect.y = e.rect.y+20
             todos.add(b)
             balas_e.add(b)
             e.disparar=False
             e.tempdis=random.randrange(1000)

        for b in balas_e:
            if b.rect.x > ancho:
                balas_e.remove(b)
                todos.remove(b)
            ls_colbe=pygame.sprite.spritecollide(b,jugadores,False)
            for j in ls_colbe:
                j.salud-=1
                balas_e.remove(b)
                todos.remove(b)
        #Enemigos fuera de pantalla
        for e in enemigos:
            if e.rect.y < 0:
                enemigos.remove(e)
                todos.remove(e)
                eliminados+=1
        #Salud jugadores
        for j in jugadores:
            if j.salud == 0:
                jugadores.remove(j)
                todos.remove(j)
                go=True
        for e in enemigos:
            if e.salud == 0:
                enemigos.remove(e)
                todos.remove(e)

        salud=0
        if jugador.salud == 0:
            salud=1
        if jugador2.salud == 0:
            salud=2
        if salud==2:
            go = True


        jud1=fuente.render(str(jugador.salud),False,[255,255,255])
        jud2=fuente.render(str(jugador2.salud),False,[255,255,255])

        todos.update()
        pantalla.fill([0,0,0])
        pantalla.blit(fondo,[posFond_x,0])
        todos.draw(pantalla)
        pantalla.blit(texto1,[10,alto-600])
        pantalla.blit(jud1,[110,alto-600])
        pantalla.blit(texto2,[160,alto-600])
        pantalla.blit(jud2,[260,alto-600])

        #pantalla.blit(fondo,[0,0])
        pygame.display.flip()
        posFond_x+=velFond_x
        reloj.tick(5)
    if go:
        fintxt= fuente.render("Fin del juego",False,[255,255,255])
        pantalla.fill([0,255,0])
        pantalla.blit(fintxt,[500,300])
        pygame.display.flip()
        while not fin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
