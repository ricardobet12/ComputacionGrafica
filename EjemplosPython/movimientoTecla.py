import pygame
ancho = 600
alto = 480
a=[200,200]
b=[200,200]
c=[200,200]
d=[200,200]
x=0
y=0

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
                    a[0]-=5
                    b[0]+=5
                    c[1]-=5
                    d[1]+=5
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,0,255],a,5)
                    pygame.draw.circle(pantalla,[0,0,255],b,5)
                    pygame.draw.circle(pantalla,[0,0,255],c,5)
                    pygame.draw.circle(pantalla,[0,0,255],d,5)
                    pygame.display.flip()
                if event.key == pygame.K_b:
                    a[0]+=5
                    b[0]-=5
                    c[1]+=5
                    d[1]-=5
                    pantalla.fill([0,0,0])
                    pygame.draw.circle(pantalla,[0,0,255],a,5)
                    pygame.draw.circle(pantalla,[0,0,255],b,5)
                    pygame.draw.circle(pantalla,[0,0,255],c,5)
                    pygame.draw.circle(pantalla,[0,0,255],d,5)
                    pygame.display.flip()
