import pygame
ancho = 600
alto = 480

def ejes(p,c):
    pygame.draw.line(p,[255,0,0],(c[0], 0), (c[0], alto), 3)
    pygame.draw.line(p,[255,0,0],(0, c[1]), (ancho, c[1]), 3)
    pygame.display.flip()

def Acarte(c,pto):
    x=pto[0] - c[0]
    y=c[1] - pto[1]
    return [x,y]

def SumaVectores(v,v2):
    x=v[0]+v2[0]
    y=v[1]+v2[1]
    return [x,y]

def APant(c,pto):
    x=c[0]+pto[0]
    y=c[1]-pto[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[300,220]
    ejes(pantalla, centro)
    contador=0
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print 'click' ,  Acarte(centro,event.pos)
                contador+=1
                if contador == 1:
                    a=event.pos
                    print a
                if contador==2:
                    b=event.pos
                    print b
                if contador==3:
                    c=event.pos
                    print c
                if contador==4:
                    d=event.pos
                    print d
                    pygame.draw.line(pantalla,[255,0,0],a, b)
                    pygame.draw.line(pantalla,[255,0,0],c, d)
                    contador=0
                    #calcular canonico
                    Ac=Acarte(centro,a)
                    Bc=Acarte(centro,b)
                    Cc=Acarte(centro,c)
                    Dc=Acarte(centro,d)
                    v=[Bc[0] - Ac[0],Bc[1] - Ac[1]]
                    v2=[Dc[0] - Cc[0],Dc[1] - Cc[1]]
                    pygame.draw.line(pantalla,[0,255,0],centro,APant(centro,v))
                    pygame.draw.line(pantalla,[0,255,0],centro,APant(centro,v2))
                    pygame.draw.line(pantalla,[0,0,255],centro,SumaVectores(v,v2))
                    pygame.display.flip()
