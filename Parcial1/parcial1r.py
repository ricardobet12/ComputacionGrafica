import pygame
import math
ancho = 600
alto = 480
contador=0
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                contador+=1
                if contador ==1:
                    a=event.pos
                if contador ==2:
                    b=event.pos
                    pygame.draw.line(pantalla,[255,0,0],a, b,4)
                if contador==3:
                    c=event.pos
                    als=event.pos[0]
                if contador ==4:
                    d=event.pos
                    dls=event.pos[0]
                    pygame.draw.line(pantalla,[0,255,0],c, d,4)
                    pygame.display.flip()
            if event.type == pygame.KEYDOWN:
                pantalla.fill([0,0,0])
                pygame.draw.line(pantalla,[255,0,0],a, b,4)
                if event.key == pygame.K_a:
                    dls+=15
                    als-=15
                    pygame.draw.line(pantalla,[0,255,0],c, (dls,als),4)
                    pygame.display.flip()
