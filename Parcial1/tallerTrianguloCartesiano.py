import pygame


if __name__ == '__main__':

    pygame.init()
    puntos=[]
    pto1=[]
    pto2=[]
    pto3=[]
    contador=0
    pantalla=pygame.display.set_mode([600,600])

    fin=False
    var=5
    pygame.display.flip()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:

                contador+=1
                if contador==1:
                    pto1=list(event.pos)
                    puntos.append(pto1)
                    print 'primer punto',pto1
                if contador==2:
                    pto2=list(event.pos)
                    puntos.append(pto2)
                    print 'segundo punto',pto2
                if contador==3:
                    pto3=list(event.pos)
                    puntos.append(pto3)
                    print 'tercer punto',pto3
                    print 'todo los puntos' , puntos

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    for pto in puntos:
                        pto[0]-=var
                if event.key == pygame.K_d:
                    for pto in puntos:
                        pto[0]+=var
                if event.key == pygame.K_w:
                    for pto in puntos:
                        pto[1]-=var
                if event.key == pygame.K_s:
                    for pto in puntos:
                        pto[1]+=var
            pantalla.fill([0,0,0])
            for pto in puntos:
                pygame.draw.circle(pantalla,[255,0,0],pto, 5,1)
                pygame.draw.polygon(pantalla,[0,255,0],[pto1,pto2,pto3],1)
            pygame.display.flip()
