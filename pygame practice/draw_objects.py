import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pixAr = pygame.PixelArray(gameDisplay)
    pixAr[10][20] = green

    pygame.display.update()
    gameDisplay.fill(black)