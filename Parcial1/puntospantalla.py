import pygame
ancho = 600
alto = 480
var_y=0
var_x=0
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pos=[10,10]
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos[0]=event.pos[0]
                pos[1]=event.pos[1]
                pygame.draw.circle(pantalla,[0,0,255],pos,5)
                pos[0]=10
                pygame.draw.circle(pantalla,[0,250,0],pos,5)
