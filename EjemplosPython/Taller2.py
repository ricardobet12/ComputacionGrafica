# dibujar un cuadrilatero en el plano cartesiano en el primer cuadrante al pulsar la tecla espacio rotarlo en sentido horario 45

import pygame
import math
ancho = 600
alto = 480

def ejes(p,c):
    pygame.draw.line(p,[255,0,0],(c[0], 0), (c[0], alto), 3)
    pygame.draw.line(p,[255,0,0],(0, c[1]), (ancho, c[1]), 3)
    pygame.display.flip()

def APant(c,pto):
    x=c[0]+pto[0]
    y=c[1]-pto[1]
    return [x,y]

def rotacion(pto,angulo):
    ang=math.radians(angulo)
    x= pto[0]*math.cos(ang) + pto[1]*math.sin(ang)
    y=-pto[0]*math.sin(ang) + pto[1]*math.cos(ang)
    xint=int(x)
    yint=int(y)
    return [xint,yint]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    centro=[300,220]
    ejes(pantalla, centro)
    cuadro=[[100,100],[100,50],[200,50],[200,100]]
    p_cuadrado=[]
    angulo=0
    anguloo=45
    fin=False
    for pto in cuadro:
        n_pto=APant(centro,pto)
        p_cuadrado.append(n_pto)
    pygame.draw.polygon(pantalla,[255,0,0],p_cuadrado,1)
    pygame.display.flip()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                pantalla.fill([0,0,0])
                ejes(pantalla, centro)
                if event.key == pygame.K_a:
                    cuadro[0]=rotacion(cuadro[0],anguloo)
                    cuadro[1]=rotacion(cuadro[1],anguloo)
                    cuadro[2]=rotacion(cuadro[2],anguloo)
                    cuadro[3]=rotacion(cuadro[3],anguloo)
                    pygame.draw.polygon(pantalla,[255,0,0],[APant(centro,cuadro[0]),APant(centro,cuadro[1]),APant(centro,cuadro[2]),
                    APant(centro,cuadro[3])],1)
                    pygame.display.flip()
