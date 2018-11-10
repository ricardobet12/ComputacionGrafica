# Dibujar el plano cartesiano, capturar 2 puntos, dibujar un triangulo entre los 2 puntos y el centro. cada vez que se pulse la tecla espacio, mover el pto mas a la derecha 20 pixeles redibujar el triangulo
import pygame
import math

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

def APant(c,pto):
    x=c[0]+pto[0]
    y=c[1]-pto[1]
    return [x,y]

def Esca (s,pto):
    x=pto[0]*s[0]
    y=pto[1]*s[1]
    return [x,y]


def rotacion(angulo,pto):
    ang=math.radians(angulo)
    x= pto[0]*math.cos(ang) + pto[1]*math.sin(ang)
    y=-pto[0]*math.sin(ang) + pto[1]*math.cos(ang)
    xint=int(x)
    yint=int(y)
    return [xint,yint]

def rotacionAnti(angulo,pto):
    ang=math.radians(angulo)
    x= pto[0]*math.cos(ang) - pto[1]*math.sin(ang)
    y=pto[0]*math.sin(ang) + pto[1]*math.cos(ang)
    xint=int(x)
    yint=int(y)

    return [xint,yint]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[300,220]
    ejes(pantalla, centro)
    puntos=[]
    triangulo_transformado=[]
    triangulo_transformado2=[]
    contador=0
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:

                contador+=1
                if contador==1:
                    pto1=list(event.pos)
                    puntos.append(pto1)
                    print 'primer punto',pto1
                if contador==2:
                    pto2=list(event.pos)
                    puntos.append(pto2)
                    puntos.append(centro)
                    print 'segundo punto',pto2

                if len(puntos) == 3:
                    pygame.draw.polygon(pantalla,[0,255,0],puntos,1)
                    pygame.display.flip()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    maximo = puntos[0][0]
                    for i in range(len(puntos)):
                        if puntos[i][0] > maximo:
                            maximo = puntos[i][0]
                            pto2=puntos[i]
                            print pto2
                            pto2[0]+=20
                            print 'nuevo pto2', pto2
                        if len(puntos) == 3:
                            pantalla.fill([0,0,0])
                            ejes(pantalla,centro)
                            pygame.draw.polygon(pantalla,[0,255,0],puntos,1)
                            pygame.display.flip()
