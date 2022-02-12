# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:12:57 2022

@author: Andrey
"""

from matplotlib import pyplot as plt
import math
import pygame

'''
Generate equally spaced floating point
numbers between two given values
'''
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment 
    return numbers


'''
Draw the trajectory of a body in projectile motion
'''

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')


def draw_trajectory(u, theta, gravity, xPositions = [], yPositions = []):
    theta = math.radians(theta)
    # Time of flight
    t_flight = 2 * u * math.sin(theta) / gravity
    # Find time intervals
    intervals = frange(0, t_flight, 0.01) 

    for t in intervals:
        xPositions.append(u * math.cos(theta) * t)
        yPositions.append(u * math.sin(theta) * t - 0.5 * gravity * t *t)



pygame.init()
width = 1024
height = 800
screen = pygame.display.set_mode((width, height))
myfont = pygame.font.SysFont("Comic Sans MS", 20)
textSurface = pygame.Surface((350, 80))


clock = pygame.time.Clock()

x = []
y = []

draw_trajectory(90, 60, 9.8, x, y)

running = True
while running:
    tick = clock.tick(60) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if(len(x) > 0 and len(y)  > 0): 
        xCoordinate = x.pop(0)
        yCoordinate = y.pop(0)
        labelX = myfont.render("X coordinate:" + str(xCoordinate), 1, (255,0,0))
        labelY = myfont.render("Y coordinate:" + str(yCoordinate), 1, (255,0,0))
        #change its background color
        textSurface.fill((0,0,0))
        textSurface.blit(labelX, (10, 10))
        textSurface.blit(labelY, (10, 40))
        screen.blit(textSurface, (0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (xCoordinate, height - yCoordinate, 15, 15))
    pygame.display.flip()
    
pygame.quit() 
