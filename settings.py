import pygame
import random
from objects import *

pygame.init()

version = 'v0.0.5.9'

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 780

game_font = pygame.font.Font('joystix monospace.ttf', 20)
helvetica = pygame.font.Font('Helvetica 400.ttf', 20)

'''     Player settings     '''
coors = [0, 1]  # Room
x = 256
y = 256

fight_number_for_st_potions = {}
sum_values_in_fnfsp = 0


health = 100
added_strength = 0
strength = 2 + added_strength
sword_strength = 4 + added_strength
bow_strength = 5 + added_strength
speed = 8

gold = 10
ruby = 0

score = 0
backpack = {}

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

'''      Probabilities       '''
probability_chest = (0, 1, 1, 1, 1)  # 80% YES
probability_monster = (0, 0, 1, 1, 1)  # 60% YES
probability_elf = (0, 1)  # 50% YES, if not monster

chest_voc = {'Strength potion': s_potion, 'Strong strength potion': ss_potion, 'Light health potion': lh_potion,
             'Health potion': h_potion, 'Strong health potion': sh_potion}
# chest_stuff = ['Strength potion', 'Strong strength potion', 'Light health potion', 'Health potion', 'Strong health potion']
chest_stuff = ['Health potion'] * 12 + ['Light health potion'] * 7 + ['Strength potion'] * 3 + ['Strong health potion'] * 1 + ['Strong strength potion'] * 1 + ['NOTHING'] * 6  # 12:7:3:1:1

prize_chest = {'Gold': range(10, 30), 'Ruby': (0, 0, 0, 1, 1, 2), 'Other': chest_stuff}  # 33% = 1  16% = 2
prize_monster = {'Gold': range(20, 50), 'Ruby': (0, 1, 1, 1, 2), 'Other': chest_stuff}  # 60% = 1  20% = 2
