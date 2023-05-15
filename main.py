import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pygamer runner')
clock = pygame.time.Clock()
my_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = my_font.render('My game', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom= (80, 300))

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
         
   screen.blit(sky_surface, (0, 0))
   screen.blit(ground_surface, (0, 300))
   screen.blit(text_surface, (300, 50))
   snail_x_pos -= 4
   if snail_x_pos < -100: snail_x_pos = 800
   screen.blit(snail_surface, (snail_x_pos, 270))
   screen.blit(player_surface, player_rectangle)
   
   pygame.display.update()
   clock.tick(60)
