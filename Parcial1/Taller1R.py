# Capturar 4 puntos con el raton,dibujar la figura y escalarla a la mitad
import pygame
ancho = 600
alto = 480
contador=0
puntos=[]
n_punto=[]

def Esca (s,pto):
    x=pto[0]/s[0]
    y=pto[1]/s[1]
    return [x,y]

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    fin=False
    a=[2,2]
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                contador+=1
                if contador ==1:
                    a=list(event.pos)
                    puntos.append(a)
                    pygame.draw.circle(pantalla,[255,0,0],puntos[0],5)
                    pygame.display.flip()
                if contador ==2:
                    b=list(event.pos)
                    puntos.append(b)
                    pygame.draw.circle(pantalla,[255,0,0],puntos[1],5)
                    pygame.display.flip()
                if contador==3:
                    c=list(event.pos)
                    puntos.append(c)
                    pygame.draw.circle(pantalla,[255,0,0],puntos[2],5)
                    pygame.display.flip()
                if contador ==4:
                    d=list(event.pos)
                    puntos.append(d)
                    pygame.draw.circle(pantalla,[255,0,0],puntos[3],5)
                    pygame.display.flip()
                if len(puntos)==4:
                    for npto in puntos:
                        npto = Esca([2,2],npto)
                        n_punto.append(npto)
                    pygame.draw.polygon(pantalla,[0,255,0],n_punto,1)
                    pygame.display.flip()
