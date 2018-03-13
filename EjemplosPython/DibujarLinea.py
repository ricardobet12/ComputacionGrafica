import pygame

if __name__=='__main__':
    pygame.init() #iniciar libreria
    pantalla=pygame.display.set_mode([600,450]) #para crear la pantalla donde se va a jugar.
    pygame.draw.line(pantalla, [255,0,0],[100,100],[200,200])
    pygame.display.flip() #actualizar la pantalla
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(2):
                    l1=[i]==pygame.mouse.get_pos()
                pygame.draw.line(pantalla, [255,0,0],l1[0],l1[1])
                pygame.display.flip()
