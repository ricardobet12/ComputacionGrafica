import pygame
import math
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
Ancho=600
Alto=480
cont=0
cont1=0
ls=[]
p1=[20,10]
p2=[40,10]
p3=[40,20]
ls.append(p1)
ls.append(p2)
ls.append(p3)
angulo=15
ang=math.radians(15)
def Ahorario(p,a):
    x=int(p[0]*math.cos(a)+p[1]*math.sin(a))
    y=int(p[1]*math.cos(a)-p[0]*math.sin(a))
    return [x,y]


def Anthorario(p,a):
    x=int(p[0]*math.cos(a)-p[1]*math.sin(a))
    y=int(p[0]*math.sin(a)+p[1]*math.cos(a))
    return [x,y]

#for pto in ls:
#    pto=Anthorario(pto,ang)

def Ejes(p,c):
    pass
    pygame.draw.line(p,[255,0,0],[c[0],0],[c[0],Alto])
    pygame.draw.line(p,[255,0,0],[0,c[1]],[Ancho,c[1]])
    pygame.display.flip()

def Acart(c,pto):
    x=pto[0]-c[0]
    y=c[1]-pto[1]
    return[x,y]
def Apant(c,v):
    x=c[0]+v[0]
    y=c[1]-v[1]
    return [x,y]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    centro=[300,220]
    Ejes(pantalla,centro)
    fin=False
    pygame.draw.polygon(pantalla,WHITE,[Apant(centro,ls[0]),Apant(centro,ls[1]),Apant(centro,ls[2])])
    pygame.display.flip()
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                pantalla.fill(BLACK)
                Ejes(pantalla,centro)
                if event.key == pygame.K_UP:
                    ls[0]=Anthorario(ls[0],ang)
                    ls[1]=Anthorario(ls[1],ang)
                    ls[2]=Anthorario(ls[2],ang)
                    pygame.draw.polygon(pantalla,WHITE,[Apant(centro,ls[0]),Apant(centro,ls[1]),Apant(centro,ls[2])])
                    pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    ls[0]=Ahorario(ls[0],ang)
                    ls[1]=Ahorario(ls[1],ang)
                    ls[2]=Ahorario(ls[2],ang)
                    pygame.draw.polygon(pantalla,WHITE,[Apant(centro,ls[0]),Apant(centro,ls[1]),Apant(centro,ls[2])])
                    pygame.display.flip()
