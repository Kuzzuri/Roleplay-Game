#Character Yaratmak
class Character():
    def __init__(self, name, nickname, gender, health = 100):
        self.name = name
        self.nickname = nickname
        self.gender = gender
        self.health = health
    
    def sword(self, enemyname):
        print(f"{self.name} hits with sword")
        if enemy == mordu:
            mordu.health = mordu.health - 10
        else:
            print("hey")


class Enemy():
    def __init__(self, name, nickname, health = 100):
        self.name = name
        self.nickname = nickname
        self.health = health

mordu = Enemy("mordu", "the beast")

#Powers and abiltiy classes
class Fire(Character):
    def attack(self):
        print("attacked")

class Lightning(Character):
    def attack(self):
        print("defended")


class Air(Character):
    def __init__(self):
        pass

kobe = Fire("umut", "tengo", "m")
mordu = Enemy("mordu", "the beast")