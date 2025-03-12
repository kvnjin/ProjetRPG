from characterClass import getClassStats
from inventory import verifyInventory


class Character:   
    def __init__(self, name, attack, defense, hp, mana, intelligence, mr, agility, chance, stamina, spirit, characterClass, inventory):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.mana = mana
        self.intelligence = intelligence
        self.mr = mr
        self.agility = agility
        self.chance = chance
        self.stamina = stamina
        self.spirit = spirit
        self.characterClass = characterClass
        self.inventory = inventory
        
    def createAPlayer(self):
        print("Enter the name of your player: ")
        name = input()
        while len(name) >= 3 and len(name) <= 10:
            self.name = name
            return self.name
        else:
            return "Name must be between 3 and 10 characters"
    
    def selectClass(self):
        print("Select a class: Warrior, Mage, Rogue")
        selectedClass = input()
        if selectedClass == "Warrior" or selectedClass == "Mage" or selectedClass == "Rogue":
            self.characterClass = selectedClass
            return self.characterClass
        else:
            return "Invalid class"

    def __str__(self):
        if self.createAPlayer() == "Name must be between 3 and 10 characters":
            return "Name must be between 3 and 10 characters"
        if self.selectClass() == "Invalid class":
            return "Invalid class"
        getClassStats(self)

        return f"Hello {self.name}, here is your character as a {self.characterClass} \nName: {self.name}, Attack: {self.attack}, Defense: {self.defense}, HP: {self.hp}, Mana: {self.mana},Intelligence: {self.intelligence}, Magic Resistance:{self.mr}, Agility:{self.agility}, Chance: {self.chance}, Stamina: {self.stamina}, Spirit:{self.spirit} Class: {self.characterClass}, Inventory: {self.inventory}"

