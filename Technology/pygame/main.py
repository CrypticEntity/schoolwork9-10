import sys
import pygame
import random

pygame.init()

size = width, height = 720, 620
ballLocation = 360, 510
leftBarLocation = 20, 260, 15, 100
rightBarLocation = 680, 130, 15, 100
red = 255, 0, 0
black = 0, 0, 0
white = 255, 255, 255
anglex = 0.5
angley = 0.5
angleChanged = False 

screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.circle((screen), (red), (ballLocation), 10)
    pygame.draw.rect((screen), (white), pygame.Rect(leftBarLocation))
    pygame.draw.rect((screen), (white), pygame.Rect(rightBarLocation))

    if ballLocation[1] < 10 or ballLocation[1] > 610:
        angley = angley * -1
    #wall bounce

    if ballLocation[1] > leftBarLocation[1] and ballLocation[1] < leftBarLocation[1] + 100 and ballLocation[0] < 45 and ballLocation[0] > 35:
        if anglex < 0:
            anglex = random.randrange(2, 10) / 10
        elif anglex > 0:
            anglex = random.randrange(2, 10) / -10
    #left bounce

    if ballLocation[1] > rightBarLocation[1] and ballLocation[1] < rightBarLocation[1] + 100 and ballLocation[0] > 680 and ballLocation[0] < 700:
        print('right bounce')
        if anglex < 0:
            anglex = random.randrange(2, 10) / 10
        elif anglex > 0:
            anglex = random.randrange(2, 10) / -10
    #right bounce
    
    
    rightBarLocation = rightBarLocation[0], ballLocation[1] - 50, rightBarLocation[2], rightBarLocation[3]
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            if leftBarLocation[1] < 520:
                leftBarLocation = leftBarLocation[0], leftBarLocation[1] + 2, leftBarLocation[2], leftBarLocation[3]
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if leftBarLocation[1] > 0:
                leftBarLocation = leftBarLocation[0], leftBarLocation[1] - 2, leftBarLocation[2], leftBarLocation[3]
    ballLocation = ballLocation[0] + anglex, ballLocation[1] + angley
    pygame.display.flip()
    screen.fill(black)