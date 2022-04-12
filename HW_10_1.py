class Enemy:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor

    def be_attacked(self):
        pass


class Archer(Enemy):
    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)


class Wizard(Enemy):
    def __init__(self, name, health, armor):
        super().__init__(name, health, armor)
