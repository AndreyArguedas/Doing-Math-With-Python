# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:12:57 2022

@author: Andrey
"""
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


def draw_trajectory(u, theta, gravity, xPositions = [], yPositions = []):
    theta = math.radians(theta)
    # Time of flight
    t_flight = 2 * u * math.sin(theta) / gravity
    # Find time intervals
    intervals = frange(0, t_flight, 0.01) 

    for t in intervals:
        xPositions.append(u * math.cos(theta) * t)
        yPositions.append(u * math.sin(theta) * t - 0.5 * gravity * t *t)

def coordinatesText(surf, xCord, yCord, font):
    labelX = font.render("X coordinate:" + str(xCord), 1, (255,0,0))
    labelY = font.render("Y coordinate:" + str(yCord), 1, (255,0,0))
    #change its background color
    surf.fill((0,0,0))
    surf.blit(labelX, (10, 10))
    surf.blit(labelY, (10, 40))
    
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, group):
        super().__init__(group)
        self.image = pygame.image.load('BLANK.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def w(self):
        return self.__w
    @w.setter
    def w(self, w):
        self.__w = w
        
    @property
    def h(self):
        return self.__h
    @h.setter
    def h(self, h):
        self.__h = h
    
    def draw(self, screen, screenHeight):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, screenHeight - self.y, self.w, self.h))
    
    def update(self, screenHeight):
        self.rect.center = (self.x, screenHeight - self.y)
        
class CameraGroup(pygame.sprite.Group):
	def __init__(self):
		super().__init__()
		self.display_surface = pygame.display.get_surface()

		# camera offset 
		self.offset = pygame.math.Vector2()
		self.half_w = self.display_surface.get_size()[0] // 2
		self.half_h = self.display_surface.get_size()[1] // 2

		# zoom 
		self.zoom_scale = 1
		self.internal_surf_size = (2500,2500)
		self.internal_surf = pygame.Surface(self.internal_surf_size, pygame.SRCALPHA)
		self.internal_rect = self.internal_surf.get_rect(center = (self.half_w,self.half_h))
		self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surf_size)
		self.internal_offset = pygame.math.Vector2()
		self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
		self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h



	def custom_draw(self,player):
		
		# self.center_target_camera(player)
		# self.box_target_camera(player)
		# self.keyboard_control()
		#self.mouse_control()
		#self.zoom_keyboard_control()

		#self.internal_surf.fill('#71ddee')

		# active elements
		for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
			offset_pos = sprite.rect.topleft - self.offset + self.internal_offset
			self.internal_surf.blit(sprite.image,offset_pos)

		scaled_surf = pygame.transform.scale(self.internal_surf,self.internal_surface_size_vector * self.zoom_scale)
		scaled_rect = scaled_surf.get_rect(center = (self.half_w,self.half_h))

		self.display_surface.blit(scaled_surf,scaled_rect)


pygame.init()

width = 800
height = 800
FPS = 60

velocity = 90
angle = 68
gravity = 9.8

screen = pygame.display.set_mode((width, height))
coordinatesFont = pygame.font.SysFont("Comic Sans MS", 20)
textSurface = pygame.Surface((350, 80))



clock = pygame.time.Clock()

#Camera setup

camera_group = CameraGroup()
p1 = Projectile(0, height, 15, 15, camera_group)

#Lists to store multiple coordinates
x = []
y = []

draw_trajectory(velocity, angle, gravity, x, y)

running = True
while running:
    #tick = clock.tick(FPS) / 1000  # Returns milliseconds between each call to 'tick'. The convert time to seconds.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if(len(x) > 0 and len(y)  > 0): 
        p1.x = x.pop(0)
        p1.y  = y.pop(0)
        coordinatesText(textSurface, p1.x, p1.y, coordinatesFont)
        screen.blit(textSurface, (0, 0))
        p1.draw(screen, height)
    
    camera_group.update(height)
    #camera_group.draw(screen)
    camera_group.custom_draw(p1)
    pygame.display.update()
    
pygame.quit() 
