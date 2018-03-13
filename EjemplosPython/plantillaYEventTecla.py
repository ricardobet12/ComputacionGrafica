import pygame
ancho = 600
alto = 480

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pos=[10,10]
    reloj=pygame.time.Clock()
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                print 'tecla'
                if event.key == pygame.K_UP:
                    print 'arriba'
