import sys
import os
import pygame
import random
pygame.init()
size=width,height=1000,500
speed=[5,5]
background=120,255,255
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Bouncing Ball')
ball=pygame.image.load('Python\download.jpg')
ballrect=ball.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit()
    ballrect=ballrect.move(speed)
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(background)
    screen.blit(ball,ballrect)
    pygame.display.flip()
pygame.hide()