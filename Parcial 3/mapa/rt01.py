import pygame

ancho = 900
alto = 500

Negro=[0,0,0]
Blanco=[255,255,255]

class Cuadro(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.Surface([an,al])
        self.image.fill([255,0,255])
        self.rect = self.image.get_rect()
        self.click=False

if __name__ == '__main__':
    #definicion de variables
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])

    #Declaracion de grupos
    todos=pygame.sprite.Group()
    jugadores = pygame.sprite.Group()

    c=Cuadro(50,50)
    jugadores.add(c)
    todos.add(c)

    reloj=pygame.time.Clock()
    fin=False
    go=False
    ptos=0
    #ciclo del programa
    while not  fin:
        pos=pygame.mouse.get_pos()
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c.rect.collidepoint(pos):
                    c.click=True
            if event.type == pygame.MOUSEBUTTONUP:
                c.click=False

        #Logica
        if c.click:
            c.rect.center=pos


        #refresco de pantalla
        pantalla.fill([0,0,0])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
