import pygame


if __name__ == '__main__':

    pygame.init()
    puntos=[]
    pto1=[50,50]
    pto2=[100,50]
    pto3=[100,80]
    a=(20,18)
    b=(40,10)
    c=(40,20)
    s=(2,2)
    contador=0
    pantalla=pygame.display.set_mode([600,600])
    fin=False
    var=5
    pygame.display.flip()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    fin=True
                    pantalla.fill([0,0,0])
            pygame.draw.polygon(pantalla,[0,255,0],[pto1,pto2,pto3],1)
            pygame.display.flip()
