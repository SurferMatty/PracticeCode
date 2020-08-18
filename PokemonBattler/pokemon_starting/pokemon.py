class Pokemon():
    def __init__(self, name, eType, level = 10):
        self.name = name
        self.level = level
        self.eType = eType
        self.maxHp = level*6
        self.currHp = level*6
        self.kout = False

    def lose_health(self, val):
        self.currHp -= val
        self.knock_out()
        print(self.name + " now has " + str(self.currHp) + "hp!")
    
    def gain_health(self, val):
        if(self.currHp <= 0):
            print(self.name + "is being revived!")
            self.kout = False
        self.currHp += val
        if(self.currHp > self.maxHp):
            currHp = self.maxHp
        print(name + " now has " + str(self.currHp) + "hp!")

    def knock_out(self):
        if(self.currHp <= 0):
            self.currHp = 0
            self.kout = True
            print(self.name + " has been knocked out!")
    
    def attack(self, target):
        if(self.currHp == 0):
            print(self.name + " is knocked out, they can not attack!")
        if(target.type == "water" and self.type == "fire" or target.type == "fire" and self.type == "grass" or target.type == "grass" and self.type == "water"):
            target.lose_health(self.level/2)
            print("{name} has attacked {target} for {damage} points of damage!".format(name = self.name, target = target.name, damage = round(self.level/2)))
            print("It's not very effective.")
        if(target.type == "water" and self.type == "grass" or target.type == "fire" and self.type == "water" or target.type == "grass" and self.type == "fire"):
            target.lost_health(self.level*2)
            print("{name} has attacked {target} for {damage} points of damage!".format(name = self.name, target = target.name, damage = self.level*2))
            print("It's very effective!")
        else:
            target.lose_health(self.level)
            print("{name} has attacked {target} for {damage} points of damage!".format(name = self.name, target = target.name, damage = self.level))

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "water", 10)

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "grass", 10)

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "fire", 10)


class Trainer:
    def __init__(self, heldPokemon, potions, name):
        self.heldPokemon = heldPokemon
        self.potions = potions
        self.name = name
        self.outPokemon = 0
    
    def use_potion(self):
        if self.potions <= 0:
            print("You have no potions!")
        else:
            print("You use a potion on " + self.heldPokemons[self.outPokemon].name + ".")
            self.heldPokemons[self.outPokemon].gain_health(20)
            self.potions -=1
    
    def battle(self, target_trainer):
        self.heldPokemon[self.outPokemon].attack(target_trainer.heldPokemon[target_trainer.outPokemon])

    def switch_pokemon(self, new_pokemon):
        if(new_pokemon > len(self.heldPokemon) or new_pokemon < 0):
            print("You do not have a pokemon in that slot!")
        elif(self.heldPokemon[new_pokemon].kout == true):
            print("You can not use a pokemon that has been knocked out!")
        elif(self.heldPokemon[new_pokemon] == self.heldPokemon[outPokemon]):
            print("That pokemon is already out!")
        else:
            self.outPokemon = new_pokemon
            print("Go " + self.heldPokemon[new_pokemon].name + " you're up!")
    