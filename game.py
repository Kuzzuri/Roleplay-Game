import random
import time
#Character creation classes
class Character():
    def __init__(self, name, nickname, health = 100):
        self.name = name
        self.nickname = nickname
        self.health = health
    
    def sword(self):
        print(f"{self.name} hits with sword 🗡️")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (sword_damage * 2)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (sword_damage * 2)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (sword_damage * 2)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - sword_damage
            elif enemy == "sleet":
                Sleet.health = Sleet.health - sword_damage
            elif enemy == "valerus":
                Valerus.health = Valerus.health - sword_damage



class Enemy():
    def __init__(self, name, nickname, health = 100):
        self.name = name
        self.nickname = nickname
        self.health = health
    def attack(self):
        if self.name == "mordu":
            print(f"{self.name} ATTACKS 💥")
            kobe.health -= 20
        elif self.name == "sleet":
            print(f"Sleet ATTACKS 💥")
            kobe.health -= 30
        elif self.name == "valerus":
            print(f"Valerus ATTACKS 💥")
            kobe.health -= 40

#Powers and abiltiy classes
class Fire(Character):
    def heavy(self):
        print(f"{self.name} hits with fire storm 🌪️")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 3.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 2.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 2.5)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 2)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 2)
    def light(self):
        print(f"{self.name} hits with fire breath 🔥")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 1.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 1.5)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 1)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 1)

class Lightning(Character):
    def heavy(self):
        print(f"{self.name} hits with lighting strike ⚡️")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 3.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 2.5)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 2.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 2)
    def light(self):
        print(f"{self.name} hits with venom punch 🌩️")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 1.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 1.5)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 1)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 1)

class Air(Character):
    def heavy(self):
        print(f"{self.name}  hits with air blast 🌀")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 2.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 3.5)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 2)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 2)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 2.5)
    def light(self):
        print(f"{self.name} hits with air push 💨")
        hit = randomizer()
        if hit == 5:
            print("CRITICKAL HIT 🩸")
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1.5)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 1.5)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 1.5)
        else:
            if enemy == "mordu":
                mordu.health = mordu.health - (power_damage * 1)
            elif enemy == "sleet":
                Sleet.health = Sleet.health - (power_damage * 1)
            elif enemy == "valerus":
                Valerus.health = Valerus.health - (power_damage * 1)

def randomizer():
    return random.randint(1, 10)
def vertam_attack():
    if randomizer() == 1:
        Vertam.light
    elif randomizer() == 2:
        Vertam.heavy
    else:
        Vertam.sword()
sdamage = 10
pdamage = 20
#Boss fights
mordu = Enemy("mordu", "the Beast")
Baron =  Enemy("Lord Baron", "the Great")
Sleet =  Enemy("Sleet", "the Brutel")
Valerus =  Enemy("Valerus", "the Cruel")
Vertam = Air("vertam", "the brave")



#start game
input("Press any key to start the game ")

#Character creation
print("Create your character")
print(" ")
Character_name = input("enter your characters name: ")
Character_nickname = input("enter your characters nickname: ")
Character_class = input("enter your characters class(F for Firebender, L for Lightningbender, A for Airbender): ")
print(" ")

while True:
    if Character_class == "f" or Character_class == "F":
        kobe = Fire(Character_name, Character_nickname)
        break
    if Character_class == "l" or Character_class == "L":
        kobe = Lightning(Character_name, Character_nickname)
        break
    if Character_class == "a" or Character_class == "A":
        kobe = Air(Character_name, Character_nickname)
        break
    else:
        Character_class = input("enter your characters class(F for Firebender, L for Lightning, A for Air bender): ")
time.sleep(2)

#monologue
print("----------------------------------------------------------------------------------------------------------------------------")
print("Since the end of the great war the evil forces have been ruling over the world, following their leader King Gaesric")
time.sleep(3)
print("With few lands and kingdoms left unconquered, the worlds hands depend on hunters. ")
time.sleep(3)
print("An organization formed by gifted people who call themselves 'HUNTERS'")
time.sleep(3)
print("These hunters bare abilities above human capeabilities, abilties that can overcome evil")
time.sleep(3)
print(f"You were selected as a gifted yourselve by god {kobe.name} the {kobe.nickname}.")
time.sleep(3)
print("So good luck soldier, hunt he evil and save your people!")
print("----------------------------------------------------------------------------------------------------------------------------")
time.sleep(4)

print("You wake up in a forest with blood dripping down your head")
time.sleep(3)
print("Last thing you remember is you and your master, Vertam were hunting down a warlord called Valerus")
time.sleep(3)
print(" ")

while True:
    print("🧿 Vertam: 'Are you going to sleep this one out or help me out?'")
    print(" ")
    print("1.Sleeping sounds good 2.Can't do it alone huh? 3.What do you mean help me out")
    response = input("Select your response(Type the number): ")
    if response == "1" or response == "2" or response == "3":
        break

print("You turn your face to see a giant bear charging to your direction")
time.sleep(3)
print("Then your remember you were chasing down a pawn of Valerus and once you caught him")
time.sleep(3)
print("He turned into a bear and slammed you into a tree ")
while True:
    print(" ")
    print("🧿")
    print("1.Fight the bear 2.Let Vertam handle the monster")
    response = input("Select your response(Type the number): ")
    if response == "1":
        break
    elif response == "2":
        print("'I think you can handle this Vertam'")
        time.sleep(3)
        print("Vertam gets knocked out by the bear so you have to face him")
        break





potion_counter = 0
enemy = "mordu"
flask_amount = 1
flask = flask_amount
sword_damage = sdamage
power_damage = pdamage
light_counter = False
heavy_counter = False


print("---------------------------------------------------------------")
print("Tutorial: You have two options your sword and special abilities")
time.sleep(3)
print("Your sword deals less damage but does not have a cooldown")
time.sleep(3)
print("Your light attack has a cooldown of one round and your heavy attack has a cooldown of two rounds")
time.sleep(3)
print("Your potions boost your sword damage for one battle")
time.sleep(3)
print("Your flasks heal you but they are limited")
time.sleep(3)
print("You can level up and upgrade your stats")
print("---------------------------------------------------------------")
time.sleep(3)
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
            if heavy_number % 3 == 0:
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
                potion_counter += 1
                sword_damage += 5
            elif selection == "5":
                if flask > 0:
                    flask -= 1
                    kobe.health += 50
                    time.sleep(1)
                else:
                    print("out of flask")
                    time.sleep(1)
time.sleep(2)
print(" ")
sword_damage -= (potion_counter * 5)
while True:
        response = input("What do you want to level up? 1.Flask +1 2.Sword Damage +10 3.Ability Damage +2: ")
        if response == "1":
            flask_amount = flask_amount + 1
            break
        elif response == "2":
            sdamage = sdamage + 10
            break
        elif response == "3":
            pdamage = pdamage + 2
            break
time.sleep(2)
print("")
print("---------------------------------------------------------------------------------------------------")
print("You watch as Mordu slowly falls to the ground as he gives his last breath turning back into a human")
print("---------------------------------------------------------------------------------------------------")
print(" ")
time.sleep(2)
while True:
    print("🧿 1.That was easy 2.Does bear meat taste good?")
    response = input("Select your response(Type the number): ")
    if response == "1":
        print("Vertam chuckles")
        time.sleep(2)
        break
    elif response == "2":
        print("Vertam:'And i thought i was the crazy one'")
        time.sleep(2)
        break
print("---------------------------------------------------------------------------------------------------")
print("You and Vertam enter into a pub close by to have a breather")
time.sleep(3)
print("You feel peoples stare as you enter the pub, their stare is contagius")
time.sleep(3)
print("You can feel their resentment towards hunters like you")
time.sleep(3)
print("A ginger haired bearded man is notciable among them")
time.sleep(3)
print("He may be the biggest human you seen")
print("---------------------------------------------------------------------------------------------------")
time.sleep(3)
print(" ")
print("🧿 Vertam: 'Not so much for hospitality 'ey?'")
print(" ")
while True:
    print("1.Stay Silent 2.Show your anger")
    response = input("Select your response(Type the number): ")
    if response == "1":
        print("You stayed silent")
        time.sleep(2)
        break
    elif response == "2":
        print("'Stupid humans'")
        time.sleep(1)
        print("Vertam noticed your anger")
        time.sleep(1)
        break
print("------------------------------------------------------------")
print("A man with dirty clothes approach you")
print("------------------------------------------------------------")
time.sleep(3)
print("🧿 Man: 'We don't like hunters here")
print(" ")
time.sleep(3)
while True:
    print("1.Make a joke 2.Stay silent")
    response = input("Select your response(Type the number): ")
    if response == "1":
        print("'You are free to leave'")
        time.sleep(3)
        print("Your joke insulted the man")
        time.sleep(3)
        print("Man: 'Who the hell do you think you are dog?")
        time.sleep(2)
        break
    elif response == "2":
        print("You stayed silent")
        time.sleep(3)
        print("Man: 'Thats what i tought coward")
        time.sleep(2)
        break
time.sleep(3)
print("🧿 Vertam: 'Easy now friend")
print(" ")
time.sleep(3)
while True:
    print("1.Hurt the man 2.Kill the man 3.Do nothing")
    response = input("Select your response(Type the number): ")
    if response == "1":
        print("You stood up and knocked the man out with a single punch")
        time.sleep(3)
        print("The other man watching got angry but are too afraid to do anyhting")
        time.sleep(3)
        print("You and Vertam leave the pub to continue chasing Valerus")
        time.sleep(3)
        print("Ginger haired man from the pub comes up behind you")
        time.sleep(3)
        print("Ginger haired man: 'Not a nice thing you did huh hunter?'")
        time.sleep(3)
        print(" ")
        print("Vertam: 'I think he deserved it")
        time.sleep(3)
        print(" ")
        print("Ginger haired man: 'Hunters, I am lord Baron the great'")
        time.sleep(3)
        print(" ")
        print("Lord Baron: 'I heard you are after Valerus, please let me help you'")
        time.sleep(3)
        print(" ")
        print("Lord Baron: 'I have a personal vendetta against him'")
        time.sleep(3)
        baron_choice = True
        break
    elif response == "2":
        print("You unsheet and swing your sword as the head of the man seperates his body")
        time.sleep(3)
        print("Vertam gets angry and pulls you out of the pub")
        time.sleep(3)
        print(f"Vertam: '{kobe.name} get hold of yourself!'")
         
        time.sleep(3)
        print(" ")
         
        print("Ginger haired man: You dare come to my lands and hurt my PEOPLE!")
         
        time.sleep(3)
        print(" ")
         
        print("Lord Baron: 'I am Lord Baron the Great, lord of these land'")
         
        time.sleep(3)
        print(" ")
         
        print("Lord Baron: 'I am here to hunt down Valerus to avenge my people'")
         
        time.sleep(3)
        print(" ")
         
        print("Lord Baron: 'If you dare stand in my way i shall crush you'")
         
        print("Baron leaves into the forest")
        time.sleep(3)
        baron_choice = False
        break
    elif response == "3":
        print("You stayed silent")
        time.sleep(3)
        print("The ginger haired man pulls away the man from his back and warn the other man to 'Fuck off'")
        time.sleep(3)
        print(" ")
         
        print("Ginger haired man: Hunters, I am lord Baron the great")
         
        time.sleep(3)
        print(" ")
         
        print("Lord Baron: 'I heard you are after Valerus, please let me help you'")
         
        time.sleep(3)
        print(" ")
         
        print("Lord Baron: 'He slaughterd my people let me have my vengeance'")
         
        time.sleep(3)
        baron_choice = True
        break
print(" ")
print("---------------------------------------------------------------------------------------------------")
print("Baron was a big man, no doubt he was strong")
time.sleep(3)
print("He was carrying a huge hammer even bigger than him")
time.sleep(3)
print("But not enought to make a hunter afraid")
time.sleep(3)
print("---------------------------------------------------------------------------------------------------")
print(" ")
if baron_choice == True:
     
    print("Vertam: 'A helping hand wouldnt be so bad ey'")
     
    time.sleep(3)
elif baron_choice == False:
     
    print("Vertam: 'Stupid humans")
     
    time.sleep(3)
print(" ")
print("---------------------------------------------------------------------------------------------------")
print("You walkd down the forest in search of Valerus")
print("---------------------------------------------------------------------------------------------------")
time.sleep(2)
print("🧿")
print(" ")
while True:
    print("1.What was the bear about? 2.Valerus, is he dangerous?")
    response = input("Select your response(Type the number): ")
    if response == "1":
        print("Vertam: 'He was a shapeshifter. One of man that serve Valerus'")
        time.sleep(2)
        break
    elif response == "2":
        print("Vertam:'I encountered him once, nearly cost me my life'")
        time.sleep(2)
        break
print("Vertam: 'Valerus was one of the leading officers of King Gaseric'")
time.sleep(2)
print("Vertam: 'Just before Valerus became power hungry and tried to take Gaeseric's place'")
time.sleep(2)
print("Vertam: 'But he wasn't strong enough to take down Gaeseric'")
time.sleep(2)
print("Vertam: 'Since then Valerus has been hiding from Gaeseric hoping he doesnt find him'")
time.sleep(2)
print("Vertam: 'Until we got the lead on him telling us he has been hiding in this forest with his brother'")
time.sleep(2)
print("------------------------------------------------------------")
print("You stumble on a old ruin in the forest")
time.sleep(2)
print("A figure appears behind you, a man with pale face holding a long blade in his hand")
time.sleep(2)
print("Another figure appears in front of you")
time.sleep(2)
print("This one is far taller than the other one, has spikes in his head and holds a long spear")
time.sleep(2)
print("No doubt this is Valerus")
print("------------------------------------------------------------")
if baron_choice == True:
    print("Vertam: 'Me and Barron got Valerus, you handle his brother'")
    time.sleep(2)
elif baron_choice == False:
    print("You see lifeless body of Baron in front of you")
    time.sleep(2)
    print("Tried to avenge his people just to fail")
    time.sleep(2)
    print("Vertam: 'I deal with Valerus, you handle his brother")
    time.sleep(2)


input("Do you want to fight Sleet?: ")

potion_counter = 0
enemy = "sleet"
flask = flask_amount
sword_damage = sdamage / 1.5
power_damage = pdamage / 1.5
light_counter = False
heavy_counter = False
kobe.health = 100

while True:
    if Sleet.health <= 0:
        print("**************")
        print("ENEMY FELLED".center(13))
        print("**************")
        break
    else:
        print(f"sleet health: %{int(Sleet.health)}")
        mordu.attack()
        if light_counter == True:
            light_number += 1
            if light_number % 2 == 0:
                light_counter = False
        if heavy_counter == True:
            heavy_number += 1
            if heavy_number % 3 == 0:
                heavy_counter = False
        if kobe.health == 0:
            print("You lost")
            time.sleep(3)
            Sleet.health = 100
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
                potion_counter += 1
                power_damage += 5
            elif selection == "5":
                if flask > 0:
                    flask -= 1
                    kobe.health += 50
                    time.sleep(1)
                else:
                    print("out of flask")
                    time.sleep(1)
sword_damage -= (potion_counter * 5)
time.sleep(1)
while True:
        response = input("What do you want to level up? 1.Flask +1 2.Sword Damage +10 3.Ability Damage +2: ")
        if response == "1":
            flask_amount = flask_amount + 1
            break
        elif response == "2":
            sdamage = sdamage + 10
            break
        elif response == "3":
            pdamage = pdamage + 2
            break
time.sleep(1)
if baron_choice == True:
    print("You here the screams of Baron as you see him get impaled by spear of Valerus")
    time.sleep(2)
    print("You went out to help Vertam")
    time.sleep(2)
elif baron_choice == False:
    print("You look at Vertam to see what he is doing")
    time.sleep(2)
    print("Just to see his lifeless body lying in front of you")
    time.sleep(2)
    print("Rage fills you up as the hatred fuels your body")
    time.sleep(2)

potion_counter = 0
enemy = "valerus"
flask = flask_amount
sword_damage = sdamage / 2
power_damage = pdamage / 2
light_counter = False
heavy_counter = False
kobe.health = 100

input("Fight Velarus?")
if baron_choice == True:
    while True:
        if Valerus.health <= 0:
            print("********************")
            print("GREAT ENEMY FELLED".center(15))
            print("********************")
            break
        else:
            print(f"valerus health: %{int(Valerus.health)}")
            mordu.attack()
            vertam_attack()
            if light_counter == True:
                light_number += 1
                if light_number % 2 == 0:
                    light_counter = False
            if heavy_counter == True:
                heavy_number += 1
                if heavy_number % 3 == 0:
                    heavy_counter = False
            if kobe.health == 0:
                print("You lost")
                time.sleep(3)
                Valerus.health = 100
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
                    potion_counter += 1
                    power_damage += 5
                elif selection == "5":
                    if flask > 0:
                        flask -= 1
                        kobe.health += 50
                        time.sleep(1)
                    else:
                        print("out of flask")
                        time.sleep(1)
elif baron_choice == False:
        while True:
            if Valerus.health <= 0:
                print("********************")
                print("GREAT ENEMY FELLED".center(15))
                print("********************")
                break
            else:
                print(f"valerus health: %{int(Valerus.health)}")
                mordu.attack()
                if light_counter == True:
                    light_number += 1
                    if light_number % 2 == 0:
                        light_counter = False
                if heavy_counter == True:
                    heavy_number += 1
                    if heavy_number % 3 == 0:
                        heavy_counter = False
                if kobe.health == 0:
                    print("You lost")
                    time.sleep(3)
                    Valerus.health = 100
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
if baron_choice == True:
    print("------------------------------------------------------------")
    print("You bring end to the evil warlord that took innocent lives")
    print("Who knows how many lives you saved, but at what cost?")
    print("A lord who just wanted to avenge his peoples lifes")
    print("One thing you know, you and Vertam wont stop until there is no more evil left")
    print("THE END")
    print("------------------------------------------------------------")  
elif baron_choice == False:
    print("------------------------------------------------------------")
    print("You bring end to the evil warlord that took innocent lives")
    print("Who knows how many lives you saved, but at what cost?")
    print("A teacher, a master, a father figure")
    print("One thing you know, you wont stop until there is no more evil left")
    print("THE END")
    print("------------------------------------------------------------")  





