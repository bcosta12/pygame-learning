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

#Because 96x96 img
SHIP_WIDTH = 96
SHIP_HEIGHT = 96

def spaceShip(x, y):
    gameDisplay.blit(SPACESHIP_IMG, (x,y))




def game_loop():

    x = (DISPLAY_WIDTH * 0.45)
    y = (DISPLAY_HEIGHT * 0.8)

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get(): # list of event for frame for second
            if event.type == pygame.QUIT: #type red x - on macosx
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: x_change += -SPEED
                if event.key == pygame.K_RIGHT: x_change += SPEED
                if event.key == pygame.K_UP: y_change += -SPEED
                if event.key == pygame.K_DOWN: y_change += SPEED

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:  x_change += SPEED
                if event.key == pygame.K_RIGHT: x_change += -SPEED
                if event.key == pygame.K_UP: y_change += SPEED
                if event.key == pygame.K_DOWN: y_change += -SPEED


        if x + x_change and x + x_change < DISPLAY_WIDTH - SHIP_WIDTH:
            x += x_change
        if y + y_change and y + y_change < DISPLAY_HEIGHT - SHIP_HEIGHT:
            y += y_change

        gameDisplay.fill(BLACK)
        spaceShip(x, y)
        #print(x, y)

        pygame.display.update() #update or flip
        clock.tick(120) #define frames per seconds

game_loop()
pygame.quit()
quit()


