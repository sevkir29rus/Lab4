class Rune:
    def __init__(self):
        self.mainstat = 0
        self.level = 1
        self.hp = 100
        self.defence = 40
        self.attack = 100
        self.speed = 20
        self.shield = 0
    def grade(self):
        if self.level == 16:
            pass
        else:
            self.level += 1
            self.mainstat += self.mainstat//10
            self.hp += 10
            self.defence += 2
            self.attack += 10
            self.speed += 1
        return self.level
class Energy(Rune):
    def __init__(self):
        super().__init__()
        self.name = 'Мощь'
        self.mainstat = 30
        self.hp += self.mainstat
class Fatall(Rune):
    def __init__(self):
        super().__init__()
        self.name = 'Натиск'
        self.mainstat = 30
        self.attack += self.mainstat
class Swift(Rune):
    def __init__(self):
        super().__init__()
        self.name = 'Прыть'
        self.mainstat = 10
        self.speed += self.mainstat
class Guard(Rune):
    def __init__(self):
        super().__init__()
        self.name = 'Страж'
        self.mainstat = 20
        self.defence += self.mainstat
class Angel(Energy):
    def __init__(self):
        super().__init__()
        self.name = 'Ангел'
        self.shield = 200

class Beast(Fatall):
    def __init__(self):
        super().__init__()
        self.name = 'Зверь'
        self.speed += 10
        self.attack += 50

