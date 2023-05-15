import pygame
from sys import exit # close any code opened

pygame.init() # to start pygame
screen = pygame.display.set_mode((800, 400)) # tuple: width, height (Display surface)
pygame.display.set_caption('Runner') # window game title
clock = pygame.time.Clock()  # clock object : controlling time and fps

'''
test_font = pygame.font.Font(None, 50) # font object : font type and font size
test_image = pygame.image.load('graphics/sky.png') # any graphical import is a new surface
player_rectangle = pygame.Rect(left, top, width, height) # creates a rectangle
'''

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(topleft= (80, 200)) # creates a rectangle around the image

test_surface = pygame.Surface((100, 200))  # tuple: width, height (surface)
test_surface.fill('red')


while True:
   for event in pygame.event.get(): # loops through all the event (use input)
      if event.type == pygame.QUIT: # cross to close
         pygame.quit() # opposite of pygame.init()
         exit() # loop gone (code is going to end)
         
   screen.blit(test_surface, (200, 100)) # blit: block image transfer (put one surface on another surface) : blit(surface, position)
   screen.blit(player_surface, player_rect) # placing the surface in the position of the rectangle
   pygame.display.update() # updates the display surface (top)
   clock.tick(60) # while loop not running faster than 60 fps
