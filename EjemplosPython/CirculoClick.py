import pygame

if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([640,480])
    reloj=pygame.time.Clock()
    pos=[0,-10]
    pygame.draw.circle(pantalla,[0,255,0],pos,5)
    pygame.display.flip()
    x=0
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x=event.pos[0]
                pos[1]=event.pos[1]
        x+=10
        pos[0]=x
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[0,255,0],pos,5)
        pygame.display.flip()
        #print x
        reloj.tick(10)
