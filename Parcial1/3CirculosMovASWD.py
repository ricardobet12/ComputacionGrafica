import pygame
ancho = 600
alto = 480
ls=[]
a=[200,200]
b=[200,300]
c=[200,400]
ls.append(a)
ls.append(b)
ls.append(c)
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pos=[10,10]
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    for pto in ls:
                        pto[0]-=5
                        pantalla.fill([0,0,0])
                    for pto in ls:
                        pygame.draw.circle(pantalla,[0,0,255],pto,5)
                    pygame.display.flip()
                if event.key == pygame.K_d:
                    for pto in ls:
                        pto[0]+=5
                        pantalla.fill([0,0,0])
                    for pto in ls:
                        pygame.draw.circle(pantalla,[0,0,255],pto,5)
                    pygame.display.flip()
                if event.key == pygame.K_s:
                    for pto in ls:
                        pto[1]+=5
                        pantalla.fill([0,0,0])
                    for pto in ls:
                        pygame.draw.circle(pantalla,[0,0,255],pto,5)
                    pygame.display.flip()
                if event.key == pygame.K_w:
                    for pto in ls:
                        pto[1]-=5
                        pantalla.fill([0,0,0])
                    for pto in ls:
                        pygame.draw.circle(pantalla,[0,0,255],pto,5)
                    pygame.display.flip()
