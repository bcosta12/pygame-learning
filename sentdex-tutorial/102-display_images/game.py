import pygame

#RESOLUTION
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 700

#RGB COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

SPACESHIP_IMG = pygame.image.load('assets/SpaceShip.png')

def spaceShip(x, y):

    gameDisplay.blit(SPACESHIP_IMG, (x,y))

x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get(): # list of event for frame for second
        if event.type == pygame.QUIT: #type red x - on macosx
            crashed = True

    gameDisplay.fill(BLACK)
    spaceShip(x, y)

    pygame.display.flip() #update or flip
    clock.tick(60) #define frames per seconds

pygame.quit()
quit()


