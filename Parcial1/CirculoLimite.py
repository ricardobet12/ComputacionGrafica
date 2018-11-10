import pygame
ancho = 600
alto = 480

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    x=10
    x2=10
    x1=470
    y=10
    y1=470
    pos=[10,10]
    reloj=pygame.time.Clock()
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x=event.pos[0]
                x1=event.pos[0]
                x2=event.pos[0]
                pos[0]=event.pos[0]
                y=event.pos[1]
                pos[1]=event.pos[1]
        x+=5
        pos[0]=x
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[255,0,0],pos,5)
        if(x>=ancho-10):
            x=ancho-10
            y+=5
            pos[1]=y
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla,[255,0,0],pos,5)
        if(y>=alto-10):
            y=alto-10
            x1-=5
            pos[0]=x1
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla,[255,0,0],pos,5)
        if(x1<=ancho-580):
            x1=ancho-580
            y1-=5
            pos[1]=y1
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla,[255,0,0],pos,5)
        if(y1<=alto-470):
            y1=alto-470
            x2+=5
            pos[0]=x2
            pantalla.fill([0,0,0])
            pygame.draw.circle(pantalla,[255,0,0],pos,5)
        pygame.display.flip()
        #print x
        reloj.tick(50)

        #Usuario da 3 click 1 por cada click dibuja una circunferencia 2 cuando se da el 3 click todas empiezan a caer
