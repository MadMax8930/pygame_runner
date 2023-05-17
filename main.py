import pygame
from sys import exit
from random import randint

def display_score():
   current_time = (pygame.time.get_ticks() - start_time) // 1000
   text_surface = my_font.render(f'Score: {current_time}', False, (64, 64, 64))
   text_rectangle = text_surface.get_rect(center= (400, 50))
   screen.blit(text_surface, text_rectangle)
   return current_time

def obstacle_movement(obs_list):
   if obs_list:
      for obs_rect in obs_list:
         obs_rect.x -= 5
         
         if obs_rect.bottom == 300:
            screen.blit(snail_surface, obs_rect) 
         else:
            screen.blit(fly_surface, obs_rect)   
         
      # only copy to the list items that are on the screen
      obs_list = [obs for obs in obs_list if obs.x > -100]  
      return obs_list
   else: return []

def collisions(player, obstacles):
   if obstacles:
      for obs_rect in obstacles:
         if player.colliderect(obs_rect):
            return False
   return True
   
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner Pygame')
clock = pygame.time.Clock()
my_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

# Game screen & Obstacles
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly_surface = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
obstacle_list = []

# Player
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom= (80, 300))
player_gravity = 0

# Intro/End screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center= (400, 200))
game_name = my_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rectangle = game_name.get_rect(center= (400, 80))
game_info = my_font.render('Press space to run', False, (111, 196, 169))
game_info_rectangle = game_info.get_rect(center= (400, 330))

# Timer (+1 to avoid conflicts)
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit()
         
      if game_active:
         if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
               player_gravity = -20
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                  player_gravity = -20      
         if event.type == obstacle_timer: # spawn obstacles
            if randint(0, 2 ): # 0 false, 1 true
               obstacle_list.append(snail_surface.get_rect(bottomright= (randint(900, 1100), 300)))
            else:
               obstacle_list.append(fly_surface.get_rect(bottomright= (randint(900, 1100), 210)))
                       
      else:
         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            start_time = pygame.time.get_ticks()
   
   if game_active:      
      # Game screen
      screen.blit(sky_surface, (0, 0))
      screen.blit(ground_surface, (0, 300))
      score = display_score()
      
      # Player
      player_gravity += 1
      player_rectangle.y += player_gravity
      if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
      screen.blit(player_surface, player_rectangle)
      
      # Enemies
      obstacle_list = obstacle_movement(obstacle_list)
      
      # Collision
      game_active = collisions(player_rectangle, obstacle_list)
   else:
      # Init for next game
      obstacle_list.clear()
      player_rectangle.midbottom = (80, 300)
      player_gravity = 0
      
      # Intro/End screen
      screen.fill((94, 129 ,162))
      screen.blit(game_name, game_name_rectangle)
      screen.blit(player_stand, player_stand_rectangle)
      score_message = my_font.render(f'Your score: {score}', False, (111, 196, 169))
      score_message_rectangle = score_message.get_rect(center= (400, 330))      
      if score == 0: screen.blit(game_info, game_info_rectangle)
      else: screen.blit(score_message, score_message_rectangle)
   
   pygame.display.update()
   clock.tick(60)
