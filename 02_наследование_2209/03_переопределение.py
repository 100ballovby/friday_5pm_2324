class Weapon:  # базовый класс оружия со всеми необходимыми мне параметрами.
    def __init__(self, bullets, skin, chance_get):
        self.capacity = bullets
        self.skin = skin
        self.stikers_list = []
        self.chance_get = chance_get

    def fire(self):
        return 'ratatatata'

    def aim(self):
        return 'vizhu'

    def reload(self):
        return 'chik-chik'


class AK47(Weapon):
    def grenade_fire(self):
        return 'babah'

    # хочу полностью переписать метод стрельбы
    def fire(self, fire_sound):
        return f'ratata + {fire_sound}'