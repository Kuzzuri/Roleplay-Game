import random
import time
#Character creation classes
class Character():
    def __init__(self, name, nickname, gender, health = 100):
        self.name = name
        self.nickname = nickname
        self.gender = gender
        self.health = health
    
    def sword(self):
        print(f"{self.name} hits with sword")
        hit = randomizer()
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (sword_damage * 2)
            elif enemy == "darth":
                mordu.health = mordu.health - (sword_damage * 2)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - sword_damage
            elif enemy == "darth":
                mordu.health = mordu.health - sword_damage



class Enemy():
    def __init__(self, name, nickname, health = 100):
        self.name = name
        self.nickname = nickname
        self.health = health
    def attack(self):
        kobe.health -= 20

#Powers and abiltiy classes
class Fire(Character):
    def heavy(self):
        print(f"{self.name} hits with fire breath")
        hit = randomizer()
        print(hit)
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 3)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
    def light(self):
        print(f"{self.name} hits with fire storm")
        hit = randomizer()
        print(hit)
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1.5)

class Lightning(Character):
    def heavy(self):
        print(f"{self.name} hits with lighting strike")
        hit = randomizer()
        print(hit)
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 3)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
    def light(self):
        print(f"{self.name} hits with venom punch")
        hit = randomizer()
        print(hit)
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1.5)


class Air(Character):
    def heavy(self):
        print(f"{self.name} hits with air push")
        hit = randomizer()
        print(hit)
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 3)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
    def light(self):
        print(f"{self.name} hits with air blast")
        hit = randomizer()
        print(hit)
        if hit == 5:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1.5)

def randomizer():
    return random.randint(1, 10)

#Boss fights
mordu = Enemy("mordu", "the Beast")
Baron =  Enemy("Lord Baron", "the Great")
Sleet =  Enemy("Sleet", "the Brutel")
Valerus =  Enemy("Valerus", "the Cruel")



#start game
input("Press any key to start the game ")
#monologue
print("-----------------------------------------------------------------------------------------------------------------------------")
print("Since the end of the great war the evil forces have been ruling over the world, following their leader King Gaesric")
time.sleep(2)
print("With few lands and kingdoms left unconquered, the worlds hands depend on hunters. ")
time.sleep(2)
print("An organization formed by gifted people who call themselves 'HUNTERS'")
time.sleep(2)
print("These hunters bare abilities above human capeabilities, abilties that can overcome evil")
time.sleep(2)
print("You were selected as a gifted yourselve by god.")
time.sleep(2)
print("So good luck soldier, hunt he evil and save your people!")
print("-----------------------------------------------------------------------------------------------------------------------------")
time.sleep(2)

#Character creation
Character_name = input("enter your characters name: ")
Character_nickname = input("enter your characters nickname: ")
Character_sex = input("enter your characters sex: ")
Character_class = input("enter your characters class(F for Firebender, L for Lightningbender, A for Airbender): ")

while True:
    if Character_class == "f" or Character_class == "F":
        kobe = Fire(Character_name, Character_nickname, Character_sex)
        break
    if Character_class == "l" or Character_class == "L":
        kobe = Lightning(Character_name, Character_nickname, Character_sex)
        break
    if Character_class == "a" or Character_class == "A":
        kobe = Air(Character_name, Character_nickname, Character_sex)
        break
    else:
        Character_class = input("enter your characters class(F for Firebender, L for Lightning, A for Air bender): ")
time.sleep(2)

print("You wake up in a forest with blood dripping down your head")
time.sleep(2)
print("Last thing you remember is you and your master, Vertam were hunting down a warlord called Valerus")
time.sleep(2)

while True:
    print("---------------------------------------------------------------")
    print("Vertam: 'Are you going to sleep this one out or help me out?'")
    print("1.Sleeping sounds good 2.Can't do it alone huh? 3.What do you mean help me out")
    print("---------------------------------------------------------------")
    response = input("Select your response(Type the number): ")
    if response == "1" or response == "2" or response == "3":
        break
print("---------------------------------------------------------------")
print("You turn your face to see a bear charging to your direction")
time.sleep(2)
print("Then your remember you were chasing down a pawn of Vertam and once you caught him")
time.sleep(2)
print("He turned into a bear and slammed you into a tree ")
print("---------------------------------------------------------------")
while True:
    print("---------------------------------------------------------------")
    print("1.Fight the bear 2.Let Vertam handle the monster")
    response = input("Select your response(Type the number): ")
    if response == "1":
        break
    elif response == "2":
        print("'I think you can handle this Vertam'")
        time.sleep(2)
        print("Vertam gets knocked out by the bear so you have to face him")
        print("---------------------------------------------------------------")
        break






enemy = "mordu"
flask = 1
sword_damage = 10
power_damage = 20
light_counter = False
heavy_counter = False


print("---------------------------------------------------------------")
print("Tutorial: You have two options your sword and special abilities")
time.sleep(2)
print("Your sword deals less damage but does not have a cooldown")
time.sleep(2)
print("Your light attack has a cooldown of one round and your heavy attack has a cooldown of two rounds")
time.sleep(2)
print("Your potions boost your damage")
time.sleep(2)
print("Your flasks heal you but they are limited")
time.sleep(2)
print("You can level up and upgrade your stats")
print("---------------------------------------------------------------")
time.sleep(2)
input("Do you want to fight Mordu?: ")

while True:
    if mordu.health <= 0:
        print("**************")
        print("ENEMY FELLED".center(13))
        print("**************")
        break
    else:
        print(f"mordu health: %{int(mordu.health)}")
        mordu.attack()
        if light_counter == True:
            light_number += 1
            if light_number % 2 == 0:
                light_counter = False
        if heavy_counter == True:
            heavy_number += 1
            if heavy_number % 2 == 0:
                heavy_counter = False
        if kobe.health == 0:
            print("You lost")
            time.sleep(3)
            mordu.health = 100
            kobe.health = 100
        else:
            print(f"{enemy} attacked {kobe.name} health: {kobe.health}")
            selection = input("Select your attack: 1.Sword 2.Light 3.Heavy 4.Potion Up 5.FLask: ")
            if selection == "1":
                kobe.sword()
                time.sleep(1)
            elif selection == "2":
                if light_counter == False:
                    kobe.light()
                    light_counter = True
                    light_number = 0
                    time.sleep(1)
                else:
                    print("Ability on cooldown")
                    time.sleep(1)
            elif selection == "3":
                if heavy_counter == False:
                    kobe.heavy()
                    heavy_counter = True
                    heavy_number = 0
                    time.sleep(1)
                else:
                    print("Ability on cooldown")
                    time.sleep(1)
            elif selection == "4":
                power_damage += 5
            elif selection == "5":
                if flask > 0:
                    flask -= 1
                    kobe.health += 50
                    time.sleep(1)
                else:
                    print("out of flask")
                    time.sleep(1)

print("You watch as Mordu slowly falls to the ground as he gives his last breath turning back into a human")
time.sleep(2)
while True:
    print("1.That was easy 2.Does bear meat taste good?")
    response = input("Select your response(Type the number): ")
    if response == "1":
        print("Vertam chuckles")
        time.sleep(2)
        break
    elif response == "2":
        print("Vertam:'And i thought i was the crazy one'")
        time.sleep(2)
        break


        
    








