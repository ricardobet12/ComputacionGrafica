import pygame
ancho = 600
alto = 480
var_y=0
var_x=0
if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ancho,alto])
    pos=[10,10]
    fin=False
    while not  fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    var_y=-1
                if event.key == pygame.K_DOWN:
                    var_y=+1
                if event.key == pygame.K_RIGHT:
                    var_x=+1
                if event.key == pygame.K_LEFT:
                    var_x=-1
                if event.key == pygame.K_SPACE:
                    var_y=0
        pos[0]+=var_x
        pos[1]+=var_y
        if pos[0]==580 or pos[0]==10:
            var_x=0
        if pos[1]==470 or pos[1]==10:
            var_y=0
        pantalla.fill([0,0,0])
        pygame.draw.circle(pantalla,[0,0,255],pos,5)
        pygame.display.flip()
