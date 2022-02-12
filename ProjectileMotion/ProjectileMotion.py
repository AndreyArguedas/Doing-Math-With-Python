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
        xPositions.append(u*math.cos(theta)*t)
        yPositions.append(u*math.sin(theta)*t - 0.5*gravity*t*t)
    #draw_graph(xPositions, yPositions)


#draw_trajectory(25, 60)
#plt.show()


# List of three different initial velocities
'''
u_list = [20, 40, 60]
theta = 45
gravity = 9.8
for u in u_list:
    draw_trajectory(u, theta, gravity)

 # Add a legend and show the graph
plt.legend(['20', '40', '60'])
plt.show()
'''


pygame.init()
screen = pygame.display.set_mode((1024, 800))

clock = pygame.time.Clock()

x = []
y = []

draw_trajectory(600, 70, 9.8, x, y)

running = True
while running:
    tick = clock.tick(60) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    #screen.fill((0,0,0))  # Fill the screen with background color.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if(len(x) > 0 and len(y)  > 0): 
        pygame.draw.rect(screen, (255, 255, 255), (x.pop(0), 800 - y.pop(0), 6, 6))
    pygame.display.flip()
    
pygame.quit()

'''
# Find time intervals
intervals = frange(0, 0.40, 0.02)



for t in intervals:
    print(t)
'''   
    

