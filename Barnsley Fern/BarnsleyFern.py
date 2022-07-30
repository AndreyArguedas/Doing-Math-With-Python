# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 20:09:21 2022

Draw a Barnsley Fern

@author: Andrey
"""

import random
import pygame



width = 1024
height = 800
FPS = 60

transformation_1 = lambda x, y : (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)

transformation_2 = lambda x, y : (0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6)

transformation_3 = lambda x, y : (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)

transformation_4 = lambda x, y : (0,  0.16 * y)

transformations = [transformation_1, transformation_2, transformation_3, transformation_4]
probabilities = (0.85, 0.07, 0.07, 0.01)


def transform(x, y, transformations, probabilities):
    func = random.choices(transformations, weights = probabilities, k = 1).pop()
    tx, ty = func(x, y)
    return tx, ty


pygame.init()

screen = pygame.display.set_mode((width, height))



clock = pygame.time.Clock()



def build_fern_points(transformations, probabilities,  n = 10000):
    x_list = [0]
    y_list = [0]
    x1, y1 = 0, 0
    for i in range(n):
        x1, y1 = transform(x1, y1, transformations, probabilities)
        x_list.append(x1)
        y_list.append(y1)
    return x_list, y_list
    

x_list, y_list = build_fern_points(transformations, probabilities, 10000)

print(x_list)

running = True
while running:
    #tick = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if(len(x_list) > 0 and len(y_list) > 0): 
         xCoordinate = x_list.pop(0)
         yCoordinate = y_list.pop(0)
         pygame.draw.circle(screen, (0, 255, 0), (xCoordinate * 150 + 400 ,height - yCoordinate * 80), 5)

    print("Finished Painting")  
    pygame.display.flip()
    
pygame.quit() 