import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

crashed = False

while not crashed:

    for event in pygame.event.get(): # list of event for frame for seecond
        if event.type == pygame.QUIT: #type red x - on macosx
            crashed = True

        print(event)


    pygame.display.update() #update or flip
    clock.tick(60) #define frames per seconds



pygame.quit()
quit()


