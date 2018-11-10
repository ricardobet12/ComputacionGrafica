import pygame
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

s=[2,2]

def AEsc(s,pto):
    x= pto[0]*s[0]
    y= pto[1]*s[1]
    return (x,y)

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    c=[300,220]
    ejes(pantalla, c)
    triangulo=[[50,50],[100,50],[100,80]]
    p_triangulo=[]
    e_triangulo=[]
    n_triangulo=[]
    for pto in triangulo:
        n_pto=APant(c,pto)
        p_triangulo.append(n_pto)

    for pto2 in triangulo:
        n2_pto=AEsc(s,pto2)
        e_triangulo.append(n2_pto)

    for npto in e_triangulo:
        n_punt0 =APant(c,npto)
        n_triangulo.append(n_punt0)

    pygame.draw.polygon(pantalla,[0,255,0],p_triangulo,1)
    pygame.draw.polygon(pantalla,[0,0,255],n_triangulo,1)
    pygame.display.flip()
    contador=0
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
