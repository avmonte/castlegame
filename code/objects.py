from list_textures import *


class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Potion(Object):
    def __init__(self, name, description, poison_type, value, image):
        Object.__init__(self, name, description)
        self.poison_type = poison_type
        self.value = value
        self.image = image


sh_potion = Potion('Strong health potion', 'Regenerate health up to 100.', 'hl', 100, potion_health_hard)
h_potion = Potion('Health potion', 'Regenerate 50 health points.', 'hl', 50, potion_health)
lh_potion = Potion('Light health potion', 'Regenerate 25 health points.', 'hl', 25, potion_health_light)
s_potion = Potion('Strength potion', 'Adds 1 point to strength within next 3 battles.', 'st', 1, potion_strength)
ss_potion = Potion('Strong strength potion', 'Adds 2 point to strength within next 3 battles.', 'st', 2, potion_strength_hard)


class Nothing:
    pass


nothing = Nothing()