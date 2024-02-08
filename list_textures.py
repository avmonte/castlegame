import pygame
from PIL import Image

#   PLAYER'S TEXTURES
print(pygame.image.get_extended())

image_1 = Image.open("textures/player/left1.png")
raw_str = image_1.tobytes("raw", 'RGBA')
pygame_surface = pygame.image.fromstring(raw_str, image_1.size, 'RGBA')
just_left = pygame.image.load("textures/player/left1.png")
left_with_nothing = [pygame.image.load('textures/player/left1.png'),
                     pygame.image.load('textures/player/left_2.png'),
                     pygame.image.load('textures/player/left_3.png'),
                     pygame.image.load('textures/player/left1.png'),
                     pygame.image.load('textures/player/left_2.png'),
                     pygame.image.load('textures/player/left_3.png'),
                     pygame.image.load('textures/player/left1.png'),
                     pygame.image.load('textures/player/left_2.png'),
                     pygame.image.load('textures/player/left_3.png')]

just_left_sword = pygame.image.load('textures/player/left_sword_1.png')
left_with_sword = [pygame.image.load('textures/player/left_sword_1.png'),
                   pygame.image.load('textures/player/left_sword_2.png'),
                   pygame.image.load('textures/player/left_sword_3.png'),
                   pygame.image.load('textures/player/left_sword_1.png'),
                   pygame.image.load('textures/player/left_sword_2.png'),
                   pygame.image.load('textures/player/left_sword_3.png'),
                   pygame.image.load('textures/player/left_sword_1.png'),
                   pygame.image.load('textures/player/left_sword_2.png'),
                   pygame.image.load('textures/player/left_sword_3.png')]

just_left_bow = pygame.image.load('textures/player/left_bow_1.png')
left_with_bow = [pygame.image.load('textures/player/left_bow_1.png'),
                 pygame.image.load('textures/player/left_bow_2.png'),
                 pygame.image.load('textures/player/left_bow_3.png'),
                 pygame.image.load('textures/player/left_bow_1.png'),
                 pygame.image.load('textures/player/left_bow_2.png'),
                 pygame.image.load('textures/player/left_bow_3.png'),
                 pygame.image.load('textures/player/left_bow_1.png'),
                 pygame.image.load('textures/player/left_bow_2.png'),
                 pygame.image.load('textures/player/left_bow_3.png')]


just_right = pygame.image.load('textures/player/right_1.png')
right_with_nothing = [pygame.image.load('textures/player/right_1.png'),
                      pygame.image.load('textures/player/right_2.png'),
                      pygame.image.load('textures/player/right_3.png'),
                      pygame.image.load('textures/player/right_1.png'),
                      pygame.image.load('textures/player/right_2.png'),
                      pygame.image.load('textures/player/right_3.png'),
                      pygame.image.load('textures/player/right_1.png'),
                      pygame.image.load('textures/player/right_2.png'),
                      pygame.image.load('textures/player/right_3.png')]

just_right_sword = pygame.image.load('textures/player/right_sword_1.png')
right_with_sword = [pygame.image.load('textures/player/right_sword_1.png'),
                    pygame.image.load('textures/player/right_sword_2.png'),
                    pygame.image.load('textures/player/right_sword_3.png'),
                    pygame.image.load('textures/player/right_sword_1.png'),
                    pygame.image.load('textures/player/right_sword_2.png'),
                    pygame.image.load('textures/player/right_sword_3.png'),
                    pygame.image.load('textures/player/right_sword_1.png'),
                    pygame.image.load('textures/player/right_sword_2.png'),
                    pygame.image.load('textures/player/right_sword_3.png')]

just_right_bow = pygame.image.load('textures/player/right_bow_1.png')
right_with_bow = [pygame.image.load('textures/player/right_bow_1.png'),
                  pygame.image.load('textures/player/right_bow_2.png'),
                  pygame.image.load('textures/player/right_bow_3.png'),
                  pygame.image.load('textures/player/right_bow_1.png'),
                  pygame.image.load('textures/player/right_bow_2.png'),
                  pygame.image.load('textures/player/right_bow_3.png'),
                  pygame.image.load('textures/player/right_bow_1.png'),
                  pygame.image.load('textures/player/right_bow_2.png'),
                  pygame.image.load('textures/player/right_bow_3.png')]


just_up = pygame.image.load('textures/player/up_1.png')
up_with_nothing = [pygame.image.load('textures/player/up_1.png'),
                   pygame.image.load('textures/player/up_2.png'),
                   pygame.image.load('textures/player/up_3.png'),
                   pygame.image.load('textures/player/up_1.png'),
                   pygame.image.load('textures/player/up_2.png'),
                   pygame.image.load('textures/player/up_3.png'),
                   pygame.image.load('textures/player/up_1.png'),
                   pygame.image.load('textures/player/up_2.png'),
                   pygame.image.load('textures/player/up_3.png')]

just_up_sword = pygame.image.load('textures/player/up_sword_1.png')
up_with_sword = [pygame.image.load('textures/player/up_sword_1.png'),
                 pygame.image.load('textures/player/up_sword_2.png'),
                 pygame.image.load('textures/player/up_sword_3.png'),
                 pygame.image.load('textures/player/up_sword_1.png'),
                 pygame.image.load('textures/player/up_sword_2.png'),
                 pygame.image.load('textures/player/up_sword_3.png'),
                 pygame.image.load('textures/player/up_sword_1.png'),
                 pygame.image.load('textures/player/up_sword_2.png'),
                 pygame.image.load('textures/player/up_sword_3.png')]

just_up_bow = pygame.image.load('textures/player/up_bow_1.png')
up_with_bow = [pygame.image.load('textures/player/up_bow_1.png'),
               pygame.image.load('textures/player/up_bow_2.png'),
               pygame.image.load('textures/player/up_bow_3.png'),
               pygame.image.load('textures/player/up_bow_1.png'),
               pygame.image.load('textures/player/up_bow_2.png'),
               pygame.image.load('textures/player/up_bow_3.png'),
               pygame.image.load('textures/player/up_bow_1.png'),
               pygame.image.load('textures/player/up_bow_2.png'),
               pygame.image.load('textures/player/up_bow_3.png')]


just_down = pygame.image.load('textures/player/down_1.png')
down_with_nothing = [pygame.image.load('textures/player/down_1.png'),
                     pygame.image.load('textures/player/down_2.png'),
                     pygame.image.load('textures/player/down_3.png'),
                     pygame.image.load('textures/player/down_1.png'),
                     pygame.image.load('textures/player/down_2.png'),
                     pygame.image.load('textures/player/down_3.png'),
                     pygame.image.load('textures/player/down_1.png'),
                     pygame.image.load('textures/player/down_2.png'),
                     pygame.image.load('textures/player/down_3.png')]

just_down_sword = pygame.image.load('textures/player/down_sword_1.png')
down_with_sword = [pygame.image.load('textures/player/down_sword_1.png'),
                   pygame.image.load('textures/player/down_sword_2.png'),
                   pygame.image.load('textures/player/down_sword_3.png'),
                   pygame.image.load('textures/player/down_sword_1.png'),
                   pygame.image.load('textures/player/down_sword_2.png'),
                   pygame.image.load('textures/player/down_sword_3.png'),
                   pygame.image.load('textures/player/down_sword_1.png'),
                   pygame.image.load('textures/player/down_sword_2.png'),
                   pygame.image.load('textures/player/down_sword_3.png')]

just_down_bow = pygame.image.load('textures/player/down_bow_1.png')
down_with_bow = [pygame.image.load('textures/player/down_bow_1.png'),
                 pygame.image.load('textures/player/down_bow_2.png'),
                 pygame.image.load('textures/player/down_bow_3.png'),
                 pygame.image.load('textures/player/down_bow_1.png'),
                 pygame.image.load('textures/player/down_bow_2.png'),
                 pygame.image.load('textures/player/down_bow_3.png'),
                 pygame.image.load('textures/player/down_bow_1.png'),
                 pygame.image.load('textures/player/down_bow_2.png'),
                 pygame.image.load('textures/player/down_bow_3.png')]


walkUp = up_with_nothing
walkDown = down_with_nothing
walkLeft = left_with_nothing
walkRight = right_with_nothing


e_left = [pygame.image.load('textures/elf/e_left_1.png'),
          pygame.image.load('textures/elf/e_left_2.png'),
          pygame.image.load('textures/elf/e_left_3.png'),
          pygame.image.load('textures/elf/e_left_1.png'),
          pygame.image.load('textures/elf/e_left_2.png'),
          pygame.image.load('textures/elf/e_left_3.png'),
          pygame.image.load('textures/elf/e_left_1.png'),
          pygame.image.load('textures/elf/e_left_2.png'),
          pygame.image.load('textures/elf/e_left_3.png')]


e_right = [pygame.image.load('textures/elf/e_right_1.png'),
           pygame.image.load('textures/elf/e_right_2.png'),
           pygame.image.load('textures/elf/e_right_3.png'),
           pygame.image.load('textures/elf/e_right_1.png'),
           pygame.image.load('textures/elf/e_right_2.png'),
           pygame.image.load('textures/elf/e_right_3.png'),
           pygame.image.load('textures/elf/e_right_1.png'),
           pygame.image.load('textures/elf/e_right_2.png'),
           pygame.image.load('textures/elf/e_right_3.png')]


e_up = [pygame.image.load('textures/elf/e_up_1.png'),
        pygame.image.load('textures/elf/e_up_2.png'),
        pygame.image.load('textures/elf/e_up_3.png'),
        pygame.image.load('textures/elf/e_up_1.png'),
        pygame.image.load('textures/elf/e_up_2.png'),
        pygame.image.load('textures/elf/e_up_3.png'),
        pygame.image.load('textures/elf/e_up_1.png'),
        pygame.image.load('textures/elf/e_up_2.png'),
        pygame.image.load('textures/elf/e_up_3.png')]


e_down = [pygame.image.load('textures/elf/e_down_1.png'),
          pygame.image.load('textures/elf/e_down_2.png'),
          pygame.image.load('textures/elf/e_down_3.png'),
          pygame.image.load('textures/elf/e_down_1.png'),
          pygame.image.load('textures/elf/e_down_2.png'),
          pygame.image.load('textures/elf/e_down_3.png'),
          pygame.image.load('textures/elf/e_down_1.png'),
          pygame.image.load('textures/elf/e_down_2.png'),
          pygame.image.load('textures/elf/e_down_3.png')]


m_left = [pygame.image.load('textures/monster/m_left_1.png'),
          pygame.image.load('textures/monster/m_left_2.png'),
          pygame.image.load('textures/monster/m_left_3.png'),
          pygame.image.load('textures/monster/m_left_1.png'),
          pygame.image.load('textures/monster/m_left_2.png'),
          pygame.image.load('textures/monster/m_left_3.png'),
          pygame.image.load('textures/monster/m_left_1.png'),
          pygame.image.load('textures/monster/m_left_2.png'),
          pygame.image.load('textures/monster/m_left_3.png')]


m_right = [pygame.image.load('textures/monster/m_right_1.png'),
           pygame.image.load('textures/monster/m_right_2.png'),
           pygame.image.load('textures/monster/m_right_3.png'),
           pygame.image.load('textures/monster/m_right_1.png'),
           pygame.image.load('textures/monster/m_right_2.png'),
           pygame.image.load('textures/monster/m_right_3.png'),
           pygame.image.load('textures/monster/m_right_1.png'),
           pygame.image.load('textures/monster/m_right_2.png'),
           pygame.image.load('textures/monster/m_right_3.png')]


m_up = [pygame.image.load('textures/monster/m_up_1.png'),
        pygame.image.load('textures/monster/m_up_2.png'),
        pygame.image.load('textures/monster/m_up_3.png'),
        pygame.image.load('textures/monster/m_up_1.png'),
        pygame.image.load('textures/monster/m_up_2.png'),
        pygame.image.load('textures/monster/m_up_3.png'),
        pygame.image.load('textures/monster/m_up_1.png'),
        pygame.image.load('textures/monster/m_up_2.png'),
        pygame.image.load('textures/monster/m_up_3.png')]


m_down = [pygame.image.load('textures/monster/m_down_1.png'),
          pygame.image.load('textures/monster/m_down_2.png'),
          pygame.image.load('textures/monster/m_down_3.png'),
          pygame.image.load('textures/monster/m_down_1.png'),
          pygame.image.load('textures/monster/m_down_2.png'),
          pygame.image.load('textures/monster/m_down_3.png'),
          pygame.image.load('textures/monster/m_down_1.png'),
          pygame.image.load('textures/monster/m_down_2.png'),
          pygame.image.load('textures/monster/m_down_3.png')]


#   BACKGROUND AND OTHER STAFF
bar = pygame.image.load('textures/bar.png')
scroll = pygame.image.load('textures/scroll.png')

chest_left = pygame.image.load('textures/chest_left.png')
chest_left_empty = pygame.image.load('textures/chest_left_empty.png')
chest_right = pygame.image.load('textures/chest_right.png')
chest_right_empty = pygame.image.load('textures/chest_right_empty.png')
chest_up = pygame.image.load('textures/chest_up.png')
chest_up_empty = pygame.image.load('textures/chest_up_empty.png')
chest_down = pygame.image.load('textures/chest_down.png')
chest_down_empty = pygame.image.load('textures/chest_down_empty.png')

arrow_left = pygame.image.load('textures/arrow_left.png')
arrow_right = pygame.image.load('textures/arrow_right.png')
arrow_up = pygame.image.load('textures/arrow_up.png')
arrow_down = pygame.image.load('textures/arrow_down.png')

health_mark = pygame.image.load('textures/health.png')
strength_mark = pygame.image.load('textures/strength.png')
gold_mark = pygame.image.load('textures/gold.png')
ruby_mark = pygame.image.load('textures/ruby.png')

potion_health_light = pygame.image.load('textures/potion_health_light.png')
potion_health = pygame.image.load('textures/potion_health.png')
potion_health_hard = pygame.image.load('textures/potion_health_hard.png')
potion_strength = pygame.image.load('textures/potion_strength.png')
potion_strength_hard = pygame.image.load('textures/potion_strength_hard.png')

backpack_frame = pygame.image.load('textures/frame.png')
# icon = pygame.image.load('textures\icon.png')   # error