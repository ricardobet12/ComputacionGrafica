import pygame
import math
ancho = 600
alto = 480
contador=0
lista=[]
anguloo=15

def rotacion(pto,angulo):
    ang=math.radians(angulo)
    x= pto[0]*math.cos(ang) + pto[1]*math.sin(ang)
    y=-pto[0]*math.sin(ang) + pto[1]*math.cos(ang)
    xint=int(x)
    yint=int(y)
    return [xint,yint]

def APant(c,pto):
    x=c[0]+pto[0]
    y=c[1]-pto[1]
    return [x,y]

def rotacionAnti(angulo,pto):
    ang=math.radians(angulo)
    x= pto[0]*math.cos(ang) - pto[1]*math.sin(ang)
    y=pto[0]*math.sin(ang) + pto[1]*math.cos(ang)
    xint=int(x)
    yint=int(y)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                print event.pos
                contador+=1
                if contador ==1:
                    a=event.pos
                if contador ==2:
                    b=event.pos
                    pygame.draw.line(pantalla,[255,0,0],a, b,4)
                    pygame.display.flip()
                if contador==3:
                    c=event.pos
                    als=event.pos[1]
                    cl=list(event.pos)
                    lista.append(cl)
                if contador ==4:
                    d=event.pos
                    dls=event.pos[0]
                    dl=list(event.pos)
                    lista.append(dl)
                    pygame.draw.line(pantalla,[0,255,0],c, d,4)
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla,[255,0,0],a, b,4)
                if event.key == pygame.K_a:
                    dls+=15
                    als-=15
                    #centro=a
                    #lista[0]=rotacion(lista[0],anguloo)
                    #lista[1]=rotacion(lista[1],anguloo)
                    #pygame.draw.polygon(pantalla,[0,255,0],[APant(centro,lista[0]),APant(centro,lista[1])],4)
                    pygame.draw.line(pantalla,[0,255,0],c, (dls,als),4)
                    pygame.display.flip()
