import pygame

#RESOLUTION
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 650

#RGB COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

SPEED = 5

pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

SPACESHIP_IMG = pygame.image.load('../assets/SpaceShip.png')

def spaceShip(x, y):

    gameDisplay.blit(SPACESHIP_IMG, (x,y))

x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.8)
x_change = 0
y_change = 0
crashed = False

while not crashed:

    for event in pygame.event.get(): # list of event for frame for second
        if event.type == pygame.QUIT: #type red x - on macosx
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += -SPEED

            if event.key == pygame.K_RIGHT:
                x_change += SPEED

            if event.key == pygame.K_UP:
                y_change += -SPEED

            if event.key == pygame.K_DOWN:
                y_change += SPEED

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change += SPEED

            if event.key == pygame.K_RIGHT:
                x_change += -SPEED

            if event.key == pygame.K_UP:
                y_change += SPEED

            if event.key == pygame.K_DOWN:
                y_change += -SPEED


    gameDisplay.fill(BLACK)
    spaceShip(x, y)
    #print(x, y)

    pygame.display.update() #update or flip
    clock.tick(60) #define frames per seconds

pygame.quit()
quit()


