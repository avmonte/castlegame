
from list_textures import *     # <-- because of extra.objects
from matrix import *
from settings import *
from objects import *
import random

'''     Py game settings     '''
pygame.init()
pygame.font.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('The Castle')
# pygame.display.set_icon(icon)   # error
clock = pygame.time.Clock()

'''     Variables of room change      '''
nope = [[0, 0], [0, 6], [6, 0], [6, 6], [0, 1], [3, 3], [2, 4], [5, 6]]  # Constant coordinates like 'S', 'D' etc.
barrier = []
north = 0
west = 0
south = 0
east = 0
notifications = []
bullets = []
monsters = []
elfs = []
with_weapon = 0

# Cooling variables
cooldown = 0
cooling = 0
cooled = 0
cooled_menu = 5
cooled_menu_2 = 0

last_quote = 'Arr..'
backpack_opened = False
paused = False


'''   CLASSES   '''


class Elf:
    def __init__(self, e_x, e_y, way):
        self.e_x = e_x
        self.e_y = e_y
        self.e_health = 30
        self.e_strength = 1
        self.e_speed = 5
        self.e_animation_count = 0
        self.img = e_left[self.e_animation_count // 2]
        self.angry = False
        self.way = way
        self.direct = 'l'

    def draw(self):
        self.e_animation_count += 1
        if self.e_animation_count >= 17:
            self.e_animation_count = 0
        window.blit(self.img, (self.e_x, self.e_y))

        if self.angry:
            pygame.draw.rect(window, red, (self.e_x + 17, self.e_y + 70, 30, 7))
            pygame.draw.rect(window, (0, 255, 0), (self.e_x + 17, self.e_y + 70, 30 - 1.5 * (20 - self.e_health), 7))

        pygame.display.update()
        self.move()

    def move(self):
        if self.way == 'x':  # horizontal
            if self.e_x >= 400:
                self.img = e_left[self.e_animation_count // 2]
                self.e_x -= self.e_speed
                self.direct = 'l'
            elif self.e_x <= 200:
                self.img = e_right[self.e_animation_count // 2]
                self.e_x += self.e_speed
                self.direct = 'r'
            elif self.e_x in range(200, 400):
                if self.direct == 'l':
                    self.img = e_left[self.e_animation_count // 2]
                    self.e_x -= self.e_speed
                else:
                    self.img = e_right[self.e_animation_count // 2]
                    self.e_x += self.e_speed
        else:  # vertical
            if self.e_y >= 400:
                self.img = e_up[self.e_animation_count // 2]
                self.e_y -= self.e_speed
                self.direct = 'd'
            elif self.e_y <= 200:
                self.img = e_down[self.e_animation_count // 2]
                self.e_y += self.e_speed
                self.direct = 'u'
            elif self.e_y in range(200, 400):
                if self.direct == 'd':
                    self.img = e_up[self.e_animation_count // 2]
                    self.e_y -= self.e_speed
                else:
                    self.img = e_down[self.e_animation_count // 2]
                    self.e_y += self.e_speed


class Monster:
    def __init__(self, m_x, m_y, way):
        self.m_x = m_x
        self.m_y = m_y
        self.m_health = 20
        self.m_strength = random.choice((0.4, 0.4, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.7, 0.7))
        self.m_speed = 5
        self.m_animation_count = 0
        self.img = m_left[self.m_animation_count // 2]
        self.way = way

    def draw(self):
        self.m_animation_count += 1
        if self.m_animation_count >= 17:
            self.m_animation_count = 0
        window.blit(self.img, (self.m_x, self.m_y))

        pygame.draw.rect(window, red, (self.m_x + 17, self.m_y + 70, 30, 7))
        pygame.draw.rect(window, (0, 255, 0), (self.m_x + 17, self.m_y + 70, 30 - (3 / 2) * (20 - self.m_health), 7))

        pygame.display.update()
        self.move()

    def move(self):
        if self.way == 'x':
            if self.m_y not in range(y - 64, y + 64):
                if self.m_x not in range(x - 64, x + 64):
                    if self.m_x > x:
                        self.img = m_left[self.m_animation_count // 2]
                        self.m_x -= self.m_speed
                    else:
                        self.img = m_right[self.m_animation_count // 2]
                        self.m_x += self.m_speed
                else:
                    if self.m_y > y + 64:
                        self.img = m_up[self.m_animation_count // 2]
                        self.m_y -= self.m_speed
                    elif self.m_y < y - 64:
                        self.img = m_down[self.m_animation_count // 2]
                        self.m_y += self.m_speed
                    else:
                        self.hit()
            else:
                if self.m_x > x + 64:
                    self.img = m_left[self.m_animation_count // 2]
                    self.m_x -= self.m_speed
                elif self.m_x < x - 64:
                    self.img = m_right[self.m_animation_count // 2]
                    self.m_x += self.m_speed
                else:
                    self.hit()
            # if self.m_x not in range(x - 16, x + 16):
            #     if self.m_y not in range(y - 72, y + 72):
            #         if self.m_x > x:
            #             self.img = m_left[self.m_animation_count // 2]
            #             self.m_x -= self.m_speed
            #         else:
            #             self.img = m_right[self.m_animation_count // 2]
            #             self.m_x += self.m_speed
            #     else:
            #         if self.m_x > x + 72:
            #             self.img = m_left[self.m_animation_count // 2]
            #             self.m_x -= self.m_speed
            #         elif self.m_x < x - 72:
            #             self.img = m_right[self.m_animation_count // 2]
            #             self.m_x += self.m_speed
            # elif self.m_y not in range(y - 72, y + 72):
            #     if self.m_y > y:
            #         self.img = m_up[self.m_animation_count // 2]
            #         self.m_y -= self.m_speed
            #     else:
            #         self.img = m_down[self.m_animation_count // 2]
            #         self.m_y += self.m_speed
            # else:
            #     self.hit()
        else:
            if self.m_x not in range(x - 64, x + 64):
                if self.m_y not in range(y - 64, y + 64):
                    if self.m_y > y:
                        self.img = m_up[self.m_animation_count // 2]
                        self.m_y -= self.m_speed
                    else:
                        self.img = m_down[self.m_animation_count // 2]
                        self.m_y += self.m_speed
                else:
                    if self.m_x > x + 64:
                        self.img = m_left[self.m_animation_count // 2]
                        self.m_x -= self.m_speed
                    elif self.m_x < x - 64:
                        self.img = m_right[self.m_animation_count // 2]
                        self.m_x += self.m_speed
                    else:
                        self.hit()
            else:
                if self.m_y > y + 64:
                    self.img = m_up[self.m_animation_count // 2]
                    self.m_y -= self.m_speed
                elif self.m_y < y - 64:
                    self.img = m_down[self.m_animation_count // 2]
                    self.m_y += self.m_speed
                else:
                    self.hit()
            # if self.m_y not in range(y - 16, y + 16):
            #     if self.m_x not in range(x - 72, x + 72):
            #         if self.m_y > y:
            #             self.img = m_up[self.m_animation_count // 2]
            #             self.m_y -= self.m_speed
            #         else:
            #             self.img = m_down[self.m_animation_count // 2]
            #             self.m_y += self.m_speed
            #     else:
            #         if self.m_y > y + 72:
            #             self.img = m_up[self.m_animation_count // 2]
            #             self.m_y -= self.m_speed
            #         elif self.m_y < y - 72:
            #             self.img = m_down[self.m_animation_count // 2]
            #             self.m_y += self.m_speed
            # elif self.m_x not in range(x - 72, x + 72):
            #     if self.m_x > x:
            #         self.img = m_left[self.m_animation_count // 2]
            #         self.m_x -= self.m_speed
            #     else:
            #         self.img = m_right[self.m_animation_count // 2]
            #         self.m_x += self.m_speed
            # else:
            #     self.hit()

    def hit(self):
        global health
        health -= self.m_strength


class Button:
    def __init__(self, width, height, active_color, inactive_color):
        self.width = width
        self.height = height
        self.active_color = active_color
        self.inactive_color = inactive_color

    def draw(self, cl_x, cl_y, message, action=None, text_color=black, font_size=20, place_text_x=10, place_text_y=10):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if cl_x < mouse[0] < cl_x + self.width and cl_y < mouse[1] < cl_y + self.height:
            pygame.draw.rect(window, self.active_color, (cl_x, cl_y, self.width, self.height))

            if click[0] == 1:
                # sound ?
                if action is not None:
                    action()

        else:
            pygame.draw.rect(window, self.inactive_color, (cl_x, cl_y, self.width, self.height))

        print_text(message=message, button_x=cl_x + place_text_x, button_y=cl_y + place_text_y, color=text_color, font_size=font_size)


class Bullet:
    def __init__(self, b_x, b_y, color, text='', bullet_speed=3, front='r', image=arrow_left):
        self.b_x = b_x
        self.b_y = b_y
        self.color = color
        self.text = text
        self.bullet_speed = bullet_speed
        self.front = front
        self.image = image

    def draw(self):
        if self.text != '':
            lab = game_font.render(self.text, 1, self.color)
            window.blit(lab, (self.b_x, self.b_y))
        else:
            window.blit(self.image, (self.b_x, self.b_y))


'''   FUNCTIONS   '''


def print_text(message, button_x, button_y, color=black, font='joystix monospace.ttf', font_size=20):
    font = pygame.font.Font(font, font_size)
    text = font.render(message, True, color)
    window.blit(text, (button_x, button_y))


def quotes():
    global cooling, last_quote
    monster_quotes = ['Arr..', 'Eat!', 'I\'ll get you!', '...', 'I\'m gonna eat you!']
    if not cooling:
        for every in monsters:
            last_quote = random.choice(monster_quotes)
            print_text(last_quote, 100, 700)
            cooling = 20
    else:
        print_text(last_quote, 100, 700)
        cooling -= 1


def resume():
    global paused
    paused = False


def pause():
    global cooled_menu, paused
    paused = True
    cooled_menu_3 = 5

    pause_menu_bg = pygame.image.load('textures/pause_menu.png')
    resume_button = Button(250, 70, red, blue)
    restart_button = Button(250, 70, red, blue)
    options_button = Button(250, 70, red, blue)
    mm_button = Button(325, 70, red, blue)

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # quit the game
                pygame.quit()
                #quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        if not cooled_menu:
            if keys[pygame.K_ESCAPE]:
                paused = False
                cooled_menu = cooled_menu_3 = 5
        else:
            cooled_menu -= 1


        window.blit(pause_menu_bg, (0, 0))

        resume_button.draw(350, 350, 'Resume', None, white, 40, 25)

        if not cooled_menu_3:
            resume_button.draw(350, 350, 'Resume', resume, white, 40, 25)
            cooled_menu_3 = cooled_menu = 2
        else:
            cooled_menu_3 -= 1

        restart_button.draw(350, 450, 'Restart', start_game, white, 40, 15)
        options_button.draw(350, 550, 'Options', None, white, 40)   # global variable to do
        mm_button.draw(313, 250, 'Main Menu', menu, white, 40, 15)

        pygame.display.update()
        clock.tick(15)


def backpack_menu():
    global backpack_opened, cooled_menu_2
    show_backpack_menu = True
    you_do = True

    print_text('Backpack', 675, 684, white, font_size=38)
    backpack_menu_bg = pygame.image.load('textures/backpack_menu_bg.png')
    backpack_menu_bg = pygame.transform.scale(backpack_menu_bg, (640, 768))

    def use(obj):
        global health, added_strength
        piece = chest_voc[obj]
        cond = str(type(piece)).split('.')[-1][:-2]

        if cond == 'Potion':
            if piece.poison_type == 'hl':
                if health >= 100:
                    if obj in backpack:
                        backpack[obj] += 1
                    else:
                        you_do = False
                        return not you_do
                else:
                    health += piece.value
                    if health > 100:
                        health = 100
            elif piece.poison_type == 'st':
                if piece.name == 'Strength potion':
                    if added_strength == 0:
                        # added_strength += piece.value
                        if piece.value not in fight_number_for_st_potions:
                            fight_number_for_st_potions[piece.value] = 0
                        else:
                            if obj in backpack:
                                backpack[obj] += 1
                            else:
                                you_do = False
                                return not you_do
                    else:
                        if obj in backpack:
                            backpack[obj] += 1
                        else:
                            you_do = False
                            return not you_do
                elif piece.name == 'Strong strength potion':
                    if added_strength <= 1:
                        # added_strength += piece.value
                        if piece.value not in fight_number_for_st_potions:
                            fight_number_for_st_potions[piece.value] = 0
                        else:
                            if obj in backpack:
                                backpack[obj] += 1
                            else:
                                you_do = False
                                return not you_do
                    else:
                        if obj in backpack:
                            backpack[obj] += 1
                        else:
                            you_do = False
                            return not you_do


    while show_backpack_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # quit the game
                pygame.quit()
                #quit()

        stats()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            backpack_opened = False
            cooled_menu_2 = 5
            show_backpack_menu = False

        window.blit(backpack_menu_bg, (0, 4))

        thing_y = 420
        thing_num = 1
        to_del = []

        for thing in backpack.keys():
            if mouse[0] in range(12 + (92 * thing_num), 12 + (92 * thing_num) + 64) and mouse[1] in range(thing_y, thing_y + 64):
                window.blit(backpack_frame, (12 + (92 * thing_num) - 4, thing_y - 4))

                print_text(chest_voc[thing].name, 200, 300, font_size=20)
                print_text(chest_voc[thing].description, 200, 330,  font_size=20)

                for one in pygame.event.get():
                    if one.type == pygame.MOUSEBUTTONDOWN:
                        use(thing)
                        if backpack[thing] == 1:
                            to_del.append(thing)
                        else:
                            if you_do:
                                backpack[thing] -= 1

            window.blit(chest_voc[thing].image, (12 + (92 * thing_num), thing_y))
            print_text('x' + str(backpack[thing]), 48 + (92 * thing_num), thing_y + 48, font_size=16)

            if thing_num == 5:
                thing_y += 92
                thing_num = 0
            thing_num += 1
        thing_num = 0

        for every in to_del:
            backpack.pop(every)
        to_del.clear()

        pygame.display.update()
        clock.tick(60)


def options_menu():
    show_options_menu = True

    options_menu_bg = pygame.image.load('textures/just_menu.png')
    back_button = Button(250, 70, red, blue)

    while show_options_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # quit the game
                pygame.quit()
                #quit()

        window.blit(options_menu_bg, (0, 0))
        back_button.draw(50, 750, 'Back', menu, white, 40, 57)

        pygame.display.update()
        clock.tick(60)


def quity():
    pygame.quit()


def menu():
    show_menu = True
    local_cool = 5

    menu_bg = pygame.image.load('textures/menu_bg.png')
    start_button = Button(250, 70, red, blue)
    options_button = Button(250, 70, red, blue)
    quit_button = Button(250, 70, red, blue)

    while show_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # quit the game
                pygame.quit()
                #quit()

        window.blit(menu_bg, (0, 0))

        start_button.draw(350, 350, 'Start', start_game, white, 40, 45)
        options_button.draw(350, 450, 'Options', options_menu, white, 40)
        quit_button.draw(350, 550, 'Quit', quity, white, 40, 57)
        print_text(version, 870, 750, white, 'Helvetica 400.ttf', 18)

        pygame.display.update()
        clock.tick(60)


def start_game():
    global score, backpack, coors, x, y, health, strength, gold, ruby, field_been, field_been_2, field_been_monster, field_been_elf, added_strength, fight_number_for_st_potions, sum_values_in_fnfsp
    global cooldown, cooling, cooled, cooled_menu, cooled_menu_2

    field_been = [[1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1]]
    field_been_2 = [[0, 0, 1, 1, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [0, 1, 1, 1, 1, 1, 0]]
    field_been_monster = [[0, 0, 1, 1, 1, 1, 0],
                          [1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 0, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1],
                          [0, 1, 1, 1, 1, 1, 0]]
    field_been_elf = [[0, 0, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 0, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1],
                      [0, 1, 1, 1, 1, 1, 0]]
    coors = [0, 1]
    x = 256
    y = 256
    health = 100
    strength = 2
    fight_number_for_st_potions = {}
    sum_values_in_fnfsp = 0
    added_strength = 0
    gold = 10
    ruby = 0
    score = 0
    backpack = {}
    cooldown = 0
    cooling = 0
    cooled = 0
    cooled_menu = 5
    cooled_menu_2 = 0
    notifications.clear()
    barrier.clear()
    bullets.clear()
    monsters.clear()
    elfs.clear()

    game_cycle()


def check_roads():
    global north, west, south, east
    info = field_rooms[coors[0]][coors[1]]
    for every in info.keys():
        if every == 'N':
            north = info[every]
        elif every == 'W':
            west = info[every]
        elif every == 'S':
            south = info[every]
        elif every == 'E':
            east = info[every]


def game_over():
    show_go_menu = True

    menu_go_bg = pygame.image.load('textures/game_over.png')
    click = pygame.mouse.get_pressed()

    while show_go_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # quit the game
                pygame.quit()
                #quit()

        window.blit(menu_go_bg, (0, 0))
        # print_text('Your score is ' + str(score), 300, 500)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or keys[pygame.K_RETURN] or click[0] == 1:
            show_go_menu = False

        pygame.display.update()
        clock.tick(60)


def chest():
    global current_room
    #  Finds possible places
    room_key = field_rooms[coors[0]][coors[1]]
    possible_places = [(128, 0), (192, 0), (256, 0), (320, 0), (384, 0), (448, 0), (512, 0),
                       (0, 128), (0, 192), (0, 256), (0, 320), (0, 384), (0, 448), (0, 512),
                       (128, 576), (192, 576), (256, 576), (320, 576), (384, 576), (448, 576), (512, 576),
                       (576, 128), (576, 192), (576, 256), (576, 320), (576, 384), (576, 448), (576, 512)]
    enters = [(room_key['N'] * 64, 0) if room_key['N'] > 0 else False,
              (0, room_key['W'] * 64) if room_key['W'] > 0 else False,
              (room_key['S'] * 64, 576) if room_key['S'] > 0 else False,
              (576, room_key['E'] * 64) if room_key['E'] > 0 else False]
    for i in enters:
        if i is not False:
            possible_places.remove(i)

    #  Creating a chest

    if field_been_2[coors[0]][coors[1]] == 1:
        if random.choice(probability_chest) == 1:
            chest_coors = random.choice(possible_places)
            field_objects[coors[0]][coors[1]]['C'] = [chest_coors, 'full']
        field_been_2[coors[0]][coors[1]] = 0
    try:
        barrier.append(field_objects[coors[0]][coors[1]]['C'][0])
    except IndexError:
        pass

    current_room = field_objects[coors[0]][coors[1]]
    if len(current_room['C']) > 0:

        if current_room['C'][0][1] == 0:
            if current_room['C'][1] == 'full':
                window.blit(chest_up, (current_room['C'][0][0], current_room['C'][0][1] + 64))
            else:
                window.blit(chest_up_empty, (current_room['C'][0][0], current_room['C'][0][1] + 64))

        if current_room['C'][0][0] == 0:
            if current_room['C'][1] == 'full':
                window.blit(chest_left, (current_room['C'][0][0] + 64, current_room['C'][0][1]))  # chest_left
            else:
                window.blit(chest_left_empty, (current_room['C'][0][0] + 64, current_room['C'][0][1]))  # chest_left

        if current_room['C'][0][1] == 576:
            if current_room['C'][1] == 'full':
                window.blit(chest_down, (current_room['C'][0][0], current_room['C'][0][1] - 64))
            else:
                window.blit(chest_down_empty, (current_room['C'][0][0], current_room['C'][0][1] - 64))

        if current_room['C'][0][0] == 576:
            if current_room['C'][1] == 'full':
                window.blit(chest_right, (current_room['C'][0][0] - 64, current_room['C'][0][1]))  # chest_right
            else:
                window.blit(chest_right_empty, (current_room['C'][0][0] - 64, current_room['C'][0][1]))  # chest_right


def elfes():
    global current_room, elfs
    if field_been_elf[coors[0]][coors[1]] == 1:
        if random.choice(probability_elf) == 1:
            # chest_coors = random.choice(possible_places)  <--- DO SOMETHING LIKE THIS FOR ELF
            field_objects[coors[0]][coors[1]]['E'] = [(random.choice(range(150, 450)), random.choice(range(150, 450))), 'alive']
        field_been_elf[coors[0]][coors[1]] = 0

    current_room = field_objects[coors[0]][coors[1]]
    if len(current_room['E']) > 0 and len(current_room['M']) == 0:
        if current_room['E'][1] == 'alive':
            if elfs == []:
                elfs.append(Elf(random.choice(range(150, 450)), random.choice(range(150, 450)), random.choice(('x', 'y'))))
                # window.blit(chest_up, (current_room['C'][0][0], current_room['C'][0][1] + 64))


def monstre():
    global current_room, monsters

    if field_been_monster[coors[0]][coors[1]] == 1:
        if random.choice(probability_monster) == 1:
            # chest_coors = random.choice(possible_places)  <--- DO SOMETHING LIKE THIS FOR MONSTER
            field_objects[coors[0]][coors[1]]['M'] = [(random.choice(range(150, 450)), random.choice(range(150, 450))), 'alive']
        field_been_monster[coors[0]][coors[1]] = 0

    current_room = field_objects[coors[0]][coors[1]]
    if len(current_room['M']) > 0:
        if current_room['M'][1] == 'alive':
            if monsters == []:
                monsters.append(Monster(random.choice(range(150, 450)), random.choice(range(150, 450)), random.choice(('x', 'y'))))
                # window.blit(chest_up, (current_room['C'][0][0], current_room['C'][0][1] + 64))


def stats():
    window.blit(health_mark, (675, 340))
    pygame.draw.rect(window, red, (730, 348, 200, 20))
    pygame.draw.rect(window, (0, 255, 0), (730, 348, 200 - 2 * (100 - health), 20))
    print_text(str(int(health)) + '/100', 772, 344, font_size=20)

    window.blit(strength_mark, (675, 400))
    local_strength = 0
    if with_weapon == 1:
        local_strength = sword_strength
        print_text(str(sword_strength), 732, 400, black, 'joystix monospace.ttf', 30)
    elif with_weapon == 2:
        local_strength = bow_strength
        print_text(str(bow_strength), 732, 400, black, 'joystix monospace.ttf', 30)
    else:
        local_strength = strength
        print_text(str(strength), 732, 400, black, 'joystix monospace.ttf', 30)

    if added_strength != 0:
        print_text('+' + str(added_strength), 760, 400, (128, 0, 128), 'joystix monospace.ttf', 30)
        print_text('=' + str(local_strength + added_strength), 812, 400, red, 'joystix monospace.ttf', 30)

    window.blit(gold_mark, (675, 464))
    window.blit(ruby_mark, (675, 528))
    print_text(str(gold), 732, 464, black, 'joystix monospace.ttf', 30)
    print_text(str(ruby), 732, 528, black, 'joystix monospace.ttf', 30)

    # Control
    #print_text('x: ' + str(x), 700, 350)
    #print_text('y: ' + str(y), 700, 375)
    # stat_chest = 'chest: ' + str(field_objects[coors[0]][coors[1]]['C'])
    # label_stat_chest = game_font.render(stat_chest, 1, black)
    # if stat_chest != 'chest: []':
    #     window.blit(label_stat_chest, (700, 400))



'''   MAIN   '''


def game_cycle():
    global gold, ruby, x, y, cooldown, cooled, sum_values_in_fnfsp, cooled_menu_2, backpack_opened, with_weapon, added_strength

    '''   Variables   '''
    last_one = 'r'
    last_pressed = 'd'
    # with_weapon = 0
    left = False
    right = True
    down = False
    up = False
    left_yes = False
    right_yes = False
    up_yes = False
    down_yes = False
    animation_count = 0

    run = True

    backpack_button = Button(280, 100, pygame.Color("#f2d833"), pygame.Color("#e8931f"))

    def get_reward(sourse):
        global gold, ruby, last_pressed

        take_it = prize_chest
        if sourse == 'chest':
            take_it = prize_chest
        elif sourse == 'monster':
            take_it = prize_monster

        new_gold = random.choice(take_it['Gold'])
        new_ruby = random.choice(take_it['Ruby'])

        print(random.choice(take_it['Other']))
        add_num = 1
        for new in [random.choice(take_it['Other'])]:
            if new != 'NOTHING':
                if new in backpack:
                    backpack[new] += 1
                else:
                    backpack[new] = 1

                add_y = 224
                if new_ruby == 0:
                    add_y = 192

                notifications.append((Bullet(32, add_y + (32 * add_num), (0, 255, 255), '+ ' + chest_voc[new].name)))
                add_num += 1
        add_num = 0

        gold += new_gold
        ruby += new_ruby

        notifications.append(Bullet(32, 192, (255, 255, 0), '+ ' + str(new_gold) + ' gold'))
        if new_ruby > 0:
            notifications.append(Bullet(32, 224, (255, 0, 255), '+ ' + str(new_ruby) + ' ruby'))

    while run:

        '''   Frames per second (FPS) '''
        clock.tick(18)

        '''     Sets background     '''
        bg_image = 'textures/rooms/room_' + str(coors[0]) + '_' + str(coors[1]) + '.png'
        bg = pygame.image.load(bg_image)

        '''     Checks the possible roads     '''
        check_roads()

        '''     CONTROL     '''
        if health <= 0:
            game_over()
            menu()

        '''     Quits the game     '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # quit the game
                pygame.quit()
                #quit()
                # run = False

        for note in notifications:
            if note.b_y > 0:
                note.b_y -= note.bullet_speed
            else:
                notifications.remove(note)

        for bullet in bullets:
            change = (0, 0)
            if bullet.front == 'l':
                change = (1, 0)
            elif bullet.front == 'r':
                change = (-1, 0)
            elif bullet.front == 'u':
                change = (0, 1)
            elif bullet.front == 'd':
                change = (0, -1)
            else:
                pass

            if 640 > bullet.b_x > 0 and 620 > bullet.b_y > 0:
                bullet.b_x -= bullet.bullet_speed * change[0]
                bullet.b_y -= bullet.bullet_speed * change[1]
            else:
                bullets.remove(bullet)

        '''     Checks the events      '''
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 56:   # go left
            if len(barrier) > 0:
                for bite in barrier:
                    if bite[0] == 0:
                        if x > bite[0] + 104 or y not in range(bite[1] - 56, bite[1] + 64):
                            left_yes = True
                    elif bite[1] == 0:
                        if (x > bite[0] + 48 or x < bite[0]) or y not in range(bite[1] - 64, bite[1] + 120):
                            left_yes = True
                    elif bite[1] == 576:
                        if (x > bite[0] + 48 or x < bite[0]) or y not in range(bite[1] - 120, bite[1] + 128):
                            left_yes = True
                    elif bite[0] == 576:
                        if (x < bite[0] - 64 or x > bite[0]) or y not in range(bite[1] - 48, bite[1] + 48):
                            left_yes = True
            else:
                left_yes = True

            for every in monsters:
                if y in range(every.m_y - 32, every.m_y + 64) and x in range(every.m_x, every.m_x + 48):
                    left_yes = False

            if left_yes:
                x -= speed
                left = True
                right = down = up = False
                last_one = 'l'
                last_pressed = 'a'
                left_yes = False
        elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 520:   # go right
            if len(barrier) > 0:
                for bite in barrier:
                    if bite[0] == 0:
                        if x > bite[0] + 96 or y not in range(bite[1] - 48, bite[1] + 48):
                            right_yes = True
                    elif bite[1] == 0:
                        if (x < bite[0] - 48 or x > bite[0]) or y not in range(bite[1] - 64, bite[1] + 120):
                            right_yes = True
                    elif bite[1] == 576:
                        if x < bite[0] - 48 or x > bite[0] or y not in range(bite[1] - 120, bite[1] + 120):
                            right_yes = True
                    elif bite[0] == 576:
                        if (x < bite[0] - 110 or x > bite[0]) or y not in range(bite[1] - 56, bite[1] + 64):
                            right_yes = True
            else:
                right_yes = True

            for every in monsters:
                if y in range(every.m_y - 32, every.m_y + 64) and x in range(every.m_x - 48, every.m_x):
                    right_yes = False

            if right_yes:
                x += speed
                right = True
                left = down = up = False
                last_one = 'r'
                last_pressed = 'd'
                right_yes = False
        elif (keys[pygame.K_w] or keys[pygame.K_UP]) and y > 69:   # go up
            if len(barrier) > 0:
                for bite in barrier:
                    if bite[0] == 0:
                        if y > bite[1] + 64 or y < bite[1] or x not in range(bite[0] - 104, bite[0] + 104):
                            up_yes = True
                    elif bite[1] == 0:
                        if y > bite[1] + 120 or x not in range(bite[0] - 40, bite[0] + 48):
                            up_yes = True
                    elif bite[1] == 576:
                        if y < bite[1] - 64 or y > bite[1] or x not in range(bite[0] - 48, bite[0] + 48):
                            up_yes = True
                    elif bite[0] == 576:
                        if y > bite[1] + 64 or y < bite[1] or x not in range(bite[0] - 96, bite[0] + 96):
                            up_yes = True
            else:
                up_yes = True

            for every in monsters:
                if y in range(every.m_y, every.m_y + 64) and x in range(every.m_x - 32, every.m_x + 32):
                    up_yes = False

            if up_yes:
                y -= speed
                up = True
                left = right = down = False
                last_one = 'u'
                last_pressed = 'w'
                up_yes = False
        elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and y < 512:   # go down
            if len(barrier) > 0:
                for bite in barrier:
                    if bite[0] == 0:
                        if y < bite[1] - 64 or y > bite[1] or x not in range(bite[0] - 104, bite[0] + 104):
                            down_yes = True
                    elif bite[1] == 0:
                        if y < bite[1] - 64 or y > bite[1] or x not in range(bite[0] - 64, bite[0] + 64):
                            down_yes = True
                    elif bite[1] == 576:
                        if y < bite[1] - 128 or x not in range(bite[0] - 40, bite[0] + 48):
                            down_yes = True
                    elif bite[0] == 576:
                        if y < bite[1] - 64 or y > bite[1] or x not in range(bite[0] - 96, bite[0] + 96):
                            down_yes = True
            else:
                down_yes = True

            for every in monsters:
                if y in range(every.m_y - 64, every.m_y) and x in range(every.m_x - 32, every.m_x + 32):
                    down_yes = False

            if down_yes:
                y += speed
                down = True
                left = right = up = False
                last_one = 'd'
                last_pressed = 's'
                down_yes = False
        else:
            if last_one == 'l:':
                left = True
                right = False
            elif last_one == 'r':
                left = False
                right = True
            elif last_one == 'd':
                down = True
                up = False
            elif last_one == 'u':
                down = False
                up = True

            animation_count = 0

        if keys[pygame.K_q]:   # change the weapon (temporary)
            if cooled == 0:

                if with_weapon == 0:
                    if last_one == 'r':
                        x += 16
                    elif last_one == 'l':
                        x -= 15
                    with_weapon += 1
                elif with_weapon == 1:
                    if last_one == 'r':
                        x -= 8
                    elif last_one == 'l':
                        x += 7
                    with_weapon += 1
                elif with_weapon == 2:
                    if last_one == 'r':
                        x -= 8
                    elif last_one == 'l':
                        x += 8
                    with_weapon = 0

                last_pressed = 'q'
                cooled = 4
            else:
                cooled -= 1

# Press E to get reword from the chest
        if keys[pygame.K_e]:
            try:
                cx = current_room['C'][0][0]
                cy = current_room['C'][0][1]
                if cx == 0:  # left
                    if y in range(cy - 72, cy + 80) and x in range(cx, cx + 136):
                        if len(current_room['C']) > 0:
                            if current_room['C'][1] == 'full':
                                get_reward('chest')
                                current_room['C'][1] = 'empty'

                elif cy == 0:  # up
                    if y in range(cy, cy + 136) and x in range(cx - 64, cx + 72):
                        if len(current_room['C']) > 0:
                            if current_room['C'][1] == 'full':
                                get_reward('chest')
                                current_room['C'][1] = 'empty'

                elif cx == 576:  # right
                    if y in range(cy - 72, cy + 80) and x in range(cx - 136, cx):
                        if len(current_room['C']) > 0:
                            if current_room['C'][1] == 'full':
                                get_reward('chest')
                                current_room['C'][1] = 'empty'

                else:  # down
                    if y in range(cy - 136, cy) and x in range(cx - 64, cx + 72):
                        if len(current_room['C']) > 0:
                            if current_room['C'][1] == 'full':
                                get_reward('chest')
                                current_room['C'][1] = 'empty'

                last_pressed = 'e'

            except IndexError:
                pass

# Press SPACE to hit or shot
        if not cooldown:
            if keys[pygame.K_SPACE]:
                if with_weapon == 0:
                    try:
                        if current_room['M'][1] == 'alive':
                            for monster in monsters:
                                if monster.m_x in range(x - 72, x + 72) and monster.m_y in range(y - 72, y + 72):
                                    monster.m_health -= strength
                    except IndexError:
                        pass
                elif with_weapon == 1:
                    try:
                        if current_room['M'][1] == 'alive':
                            for monster in monsters:
                                if monster.m_x in range(x - 72, x + 72) and monster.m_y in range(y - 72, y + 72):
                                    monster.m_health -= sword_strength
                    except IndexError:
                        pass
                elif with_weapon == 2:
                    if last_one == 'l':
                        bullets.append(Bullet(x + 4, y + 32, red, '', 10, 'l', arrow_left))
                    elif last_one == 'r':
                        bullets.append(Bullet(x + 36, y + 32, red, '', 10, 'r', arrow_right))
                    elif last_one == 'u':
                        bullets.append(Bullet(x + 28, y - 20, red, '', 10, 'u', arrow_up))
                    elif last_one == 'd':
                        bullets.append(Bullet(x + 32, y + 32, red, '', 10, 'd', arrow_down))
                    else:
                        print('last_one ERROR')
                else:
                    print('with_weapon ERROR')
                cooldown = 8
        else:
            cooldown -= 1

        if not cooled_menu_2 and not backpack_opened:
            if keys[pygame.K_ESCAPE]:
                pause()
                cooled_menu_2 = 5
        else:
            cooled_menu_2 -= 1

        if keys[pygame.K_r]:
            backpack_opened = True
            backpack_menu()

        '''     Controls what sprites to image     '''
        walk_with = [left_with_nothing, right_with_nothing, up_with_nothing, down_with_nothing]
        if with_weapon == 0:
            walk_with = [left_with_nothing, right_with_nothing, up_with_nothing, down_with_nothing]
        elif with_weapon == 1:
            walk_with = [left_with_sword, right_with_sword, up_with_sword, down_with_sword]
        elif with_weapon == 2:
            walk_with = [left_with_bow, right_with_bow, up_with_bow, down_with_bow]
        else:
            print('with_weapon is not equal 0, 1, or 2!')

        walkLeft = walk_with[0]
        walkRight = walk_with[1]
        walkUp = walk_with[2]
        walkDown = walk_with[3]

        '''     Checks if player enters the road and navigate him    '''
        if north > 0:
            if x in range(64 * north - 32, 64 * north + 32) and y in range(62, 72) and (keys[pygame.K_w]
                                                                                        or keys[pygame.K_UP]):
                coors[0] += 1
                y += 440
                x = 64 * north

                barrier.clear()
                bullets.clear()
                monsters.clear()
                elfs.clear()

        if west > 0:
            if x == 56 and y in range(64 * west - 32, 64 * west + 32) and (keys[pygame.K_a] or keys[pygame.K_LEFT]):
                coors[1] += 1
                x += 448
                y = 64 * west
                barrier.clear()
                bullets.clear()
                monsters.clear()
                elfs.clear()

        if south > 0:
            if x in range(64 * south - 32, 64 * south + 32) and y == 512 and (keys[pygame.K_s] or keys[pygame.K_DOWN]):
                coors[0] -= 1
                y -= 448
                x = 64 * south
                barrier.clear()
                bullets.clear()
                monsters.clear()
                elfs.clear()

        if east > 0:
            if x == 520 and y in range(64 * east - 32, 64 * east + 32) and (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
                coors[1] -= 1
                x -= 448
                y = 64 * east
                barrier.clear()
                bullets.clear()
                monsters.clear()
                elfs.clear()

        '''     Saves the information about what room player visited     '''
        if field_been[coors[0]][coors[1]] == 1:
            field_been[coors[0]][coors[1]] = 0

        '''     Calls function that images everything above     '''
        window.fill((0, 0, 0))
        window.blit(bg, (0, 0))
        window.blit(bar, (640, 0))
        window.blit(scroll, (0, 640))
        stats()
        chest()
        monstre()
        elfes()
        quotes()

        # for key in fight_number_for_st_potions.keys():
        #     if sum_values_in_fnfsp < key:
        #         sum_values_in_fnfsp = key

        max_var = 0
        for key in fight_number_for_st_potions.keys():
            if max_var < key:
                max_var = key

        sum_values_in_fnfsp = max_var

        added_strength = sum_values_in_fnfsp
        strength = 2 + added_strength
        sword_strength = 4 + added_strength
        bow_strength = 5 + added_strength


        for every in range(7):
            for one in range(7):
                if not field_been[every][one]:

                    if [every, one] == [0, 1]:
                        been_mark = pygame.image.load('textures/mini-map/blue_start_location_mark.png')
                    elif [every, one] == [3, 3]:
                        been_mark = pygame.image.load('textures/mini-map/blue_dragon_location_mark.png')
                    else:
                        been_mark = pygame.image.load('textures/mini-map/blue_location_mark.png')
                    window.blit(been_mark, (880 - (32 * one), 240 - (32 * every)))

                    if coors == [0, 1]:
                        mark_image = pygame.image.load('textures/mini-map/red_start_location_mark.png')
                    elif coors == [3, 3]:
                        mark_image = pygame.image.load('textures/mini-map/red_dragon_location_mark.png')
                    else:
                        mark_image = pygame.image.load('textures/mini-map/red_location_mark.png')
                    window.blit(mark_image, (880 - (32 * coors[1]), 240 - (32 * coors[0])))

        if animation_count + 1 >= 18:
            animation_count = 0

        if last_pressed in 'wasd':
            if left:
                window.blit(walkLeft[animation_count // 3], (x, y))
                animation_count += 1
            elif right:
                window.blit(walkRight[animation_count // 3], (x, y))
                animation_count += 1
            elif down:
                window.blit(walkDown[animation_count // 3], (x, y))
                animation_count += 1
            elif up:
                window.blit(walkUp[animation_count // 3], (x, y))
                animation_count += 1
        else:
            if last_one == 'l':
                if with_weapon == 1:
                    window.blit(just_left_sword, (x, y))
                elif with_weapon == 2:
                    window.blit(just_left_bow, (x, y))
                else:
                    window.blit(just_left, (x, y))
            elif last_one == 'r':
                if with_weapon == 1:
                    window.blit(just_right_sword, (x, y))
                elif with_weapon == 2:
                    window.blit(just_right_bow, (x, y))
                else:
                    window.blit(just_right, (x, y))
            elif last_one == 'u':
                if with_weapon == 1:
                    window.blit(just_up_sword, (x, y))
                elif with_weapon == 2:
                    window.blit(just_up_bow, (x, y))
                else:
                    window.blit(just_up, (x, y))
            elif last_one == 'd':
                if with_weapon == 1:
                    window.blit(just_down_sword, (x, y))
                elif with_weapon == 2:
                    window.blit(just_down_bow, (x, y))
                else:
                    window.blit(just_down, (x, y))

        for note in notifications:
            note.draw()

        for bullet in bullets:
            bullet.draw()

        for bullet in bullets:
            for monster in monsters:
                if bullet.b_x in range(monster.m_x, monster.m_x + 64) and bullet.b_y in range(monster.m_y, monster.m_y + 64):
                    monster.m_health -= bow_strength
                    bullets.remove(bullet)

        for elfe in elfs:
            elfe.draw()

        for monster in monsters:
            if monster.m_health > 0:
                monster.draw()
            else:
                notifications.append(Bullet(32, 160, (255, 165, 0), 'Fight Victory!'))
                get_reward('monster')
                current_room['M'][1] = 'done'

                to_del_potion = []
                for potion in fight_number_for_st_potions:
                    if fight_number_for_st_potions[potion] < 2:
                        fight_number_for_st_potions[potion] += 1
                    else:
                        to_del_potion.append(potion)

                for potion in to_del_potion:
                    fight_number_for_st_potions.pop(potion)
                to_del_potion.clear()

                monsters.remove(monster)

        backpack_button.draw(660, 656, 'Backpack', backpack_menu, white, 38, 15, 28)
        pygame.display.update()


menu()
#game_cycle()

#   ? |
#     v
input('Press Enter')
pygame.display.flip()
