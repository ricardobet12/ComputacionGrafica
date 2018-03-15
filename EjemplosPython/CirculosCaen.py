import pygame

if __name__ == '__main__':

    pygame.init()
    puntos=[]
    punto1=[0,0]
    punto2=[0,0]
    punto3=[0,0]
    punto4=[0,0]
    pantalla=pygame.display.set_mode([480,600])
    fin=False
    caida=0
    contador =0
    pygame.display.flip()
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    fin=True
            if event.type==pygame.MOUSEBUTTONDOWN:

                contador+=1
                if contador==1:
                    punto1[0] = event.pos[0]
                    punto1[1] = event.pos[1]
                    print punto1
                    z=punto1
                    puntos.append(punto1)
                    pygame.draw.circle(pantalla,[255,0,0], punto1 , 5,1)
                    pygame.display.flip()
                if contador==2:
                    punto2[0] = event.pos[0]
                    punto2[1] = event.pos[1]
                    print punto2
                    puntos.append(punto2)
                    print puntos
                    pygame.draw.circle(pantalla,[255,0,0], punto2 , 5,1)
                    pygame.display.flip()
##                if contador==3:
##                    punto3[0] = event.pos[0]
##                    punto3[1] = event.pos[1]
##                    print punto2
##                    puntos.append(punto3)
##                    print puntos
##                    pygame.draw.circle(pantalla,[255,0,0], punto3, 5,1)
##                    pygame.display.flip()
##                if contador==4:
##                    punto4[0] = event.pos[0]
##                    punto4[1] = event.pos[1]
##                    print punto4
##                    puntos.append(punto4)
##                    print puntos
##                    pygame.draw.circle(pantalla,[255,0,0], punto3, 5,1)
##                    pygame.display.flip()
                    for caida in range (0,600):#2 donde empieza el ciclo 10 donde termima el ciclo 3 salto entre numeros
                        puntos [0][1]+=1
                        puntos [1][1]+=1
##                        puntos [2][0]+=1
##                        puntos[3][0]-=1
                        print puntos
                        pygame.draw.circle(pantalla,[255,0,0], puntos[0] , 5,1)
                        pygame.draw.circle(pantalla,[255,0,0], puntos[1] , 5,1)
##                        pygame.draw.circle(pantalla,[255,0,0], puntos[2] , 5,1)
##                        pygame.draw.circle(pantalla,[255,0,0], puntos[3] , 5,1)
                        pygame.display.flip()
                        pantalla.fill([0,0,0])
