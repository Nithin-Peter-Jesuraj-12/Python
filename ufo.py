import pygame
#ufo = pygame.image.load('ufo.png')
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
#icon = pygame.image.load('ufo.png')
#pygame.display.set_icon(icon)
#playerl = pygame.image.load('player.png')
playerX = 420
playerY = 350
def player():
    screen.blit('''playerl,''' (playerX, playerY))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.FINGERDOWN and pygame.FINGERMOVE:
            '''i need to know how to get the location of the finger'''
            '''set the player x and y to the finger location'''
            player()
    screen.fill((0,0,0))
    pygame.display.update()