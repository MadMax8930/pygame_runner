import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pygamer runner')
clock = pygame.time.Clock()
my_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_surface = my_font.render('My game', False, (64, 64, 64))
text_rectangle = text_surface.get_rect(center= (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright= (600, 300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom= (80, 300))
player_gravity = 0

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         if player_rectangle.collidepoint(event.pos):
            player_gravity = -20
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            player_gravity = -20
         
   screen.blit(sky_surface, (0, 0))
   screen.blit(ground_surface, (0, 300))
   pygame.draw.rect(screen, '#c0e8ec', text_rectangle)
   screen.blit(text_surface, text_rectangle)
   
   snail_rectangle.x -= 4
   if snail_rectangle.right < 0: snail_rectangle.left = 800
   screen.blit(snail_surface, snail_rectangle)
   
   # Player
   player_gravity += 1
   player_rectangle.y += player_gravity
   screen.blit(player_surface, player_rectangle)
   
   pygame.display.update()
   clock.tick(60)
