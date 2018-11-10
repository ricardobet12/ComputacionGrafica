import pygame
import math

ancho=640
alto=480

def Escalar(s,pto):
    x=pto[0]*s[0]
    y=pto[1]*s[1]
    return [x,y]

def RotacionAntihoraria(pto,ang):
    n_ang=math.radians(ang)
    x=int(pto[0]*math.cos(n_ang)-pto[1]*math.sin(n_ang))
    y=int(pto[0]*math.sin(n_ang)+pto[1]*math.cos(n_ang))
    return [x,y]
def RotacionHoraria(pto,ang):
    n_ang=math.radians(ang)
    x=int(pto[0]*math.cos(n_ang)+pto[1]*math.sin(n_ang))
    y=int(-pto[0]*math.sin(n_ang)+pto[1]*math.cos(n_ang))
    return [x,y]

def puntomedio(pto1,pto2):
    x=int((pto1[0]+pto2[0])/2)
    y=int((pto1[1]+pto2[1])/2)
    return [x,y]

if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[320,240]
    cont=0
    ls=[]
    ang=15
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                if cont == 1:
                    a=event.pos
                    ls.append(list(a))
                if cont == 2:
                    b=event.pos
                    ls.append(list(b))
                if cont == 3:
                    c=event.pos
                    ls.append(list(c))
                if cont == 4:
                    d=event.pos
                    ls.append(list(d))
                    pygame.draw.line(pantalla,[0,255,0],a,b)
                    pygame.draw.line(pantalla,[0,255,0],c,d)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ls[3]=RotacionHoraria(ls[3],15)
                    pantalla.fill([0,0,0])
                    pygame.draw.line(pantalla,[0,255,0],a,b)
                    pygame.draw.line(pantalla,[0,255,0],ls[2],ls[3])
        pygame.display.flip()
