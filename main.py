import pygame
from sys import exit # close any code opened

pygame.init() # to start pygame
screen = pygame.display.set_mode((800, 400)) # tuple: width, height (display surface)
pygame.dii

while True:
   for event in pygame.event.get(): # loops through all the event (use input)
      if event.type == pygame.QUIT: # Cross to close
         pygame.quit() # opposite of pygame.init()
         exit() # loop gone (code is going to end)
      
   pygame.display.update() # updates the display surface (top)
