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

def rot(angulo,pto):
    a = math.radians(angulo)
    x=pto[0]*math.cos(a) + pto[1]*math.sin(a)
    y=-pto[0]*math.sin(a) + pto[1]*math.cos(a)
    i_x =int(x)
    i_y =int(y)
    return [i_x,i_y]

def AntRot(angulo,pto):
    a = math.radians(angulo)
    x=pto[0]*math.cos(a) - pto[1]*math.sin(a)
    y=pto[0]*math.sin(a) + pto[1]*math.cos(a)
    i_x =int(x)
    i_y =int(y)
    return [i_x,i_y]


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pantalla=pygame.display.set_mode([ancho,alto])
    c=[300,220]
    ejes(pantalla, c)
    triangulo=[[50,50],[100,50],[100,80]]
    r_triangulo=[]
    ra_triangulo=[]
    p_triangulo=[]
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    for pto in triangulo:
                        n_pto=APant(c,pto)
                        p_triangulo.append(n_pto)

                    for rpto in triangulo:
                        r_punt0 =rot(90,rpto)
                        r_triangulo.append(r_punt0)

                    for apto in r_triangulo:
                        a_punt =APant(c,apto)
                        ra_triangulo.append(a_punt)

                        pygame.draw.polygon(pantalla,[0,0,255],ra_triangulo,1)
                        print "a"
                        r_triangulo = triangulo
                        ra_triangulo = triangulo
                        pygame.display.flip()
                if event.key == pygame.K_DOWN:
                    for pto in triangulo:
                        n_pto=APant(c,pto)
                        p_triangulo.append(n_pto)

                    for rpto in triangulo:
                        r_punt0 =AntRot(90,rpto)
                        r_triangulo.append(r_punt0)

                    for apto in r_triangulo:
                        a_punt =APant(c,apto)
                        ra_triangulo.append(a_punt)
                    pygame.draw.polygon(pantalla,[0,0,255],ra_triangulo,1)
                    pygame.display.flip()
