from character.character_class import get_class_choice
from character.inventory import verify_inventory

class Character:   
    def __init__(self, name, attack, defense, hp, mana, intelligence, mr, agility, chance, stamina, spirit, character_class, inventory):
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
        self.character_class = character_class
        self.inventory = inventory
        
    def create_player(self):
        print("Enter the name of your player: ")
        name = input()
        if not (3 <= len(name) <= 10):
            return "Name must be between 3 and 10 characters"
        self.name = name
        return name
    
    def select_class(self):
        print("Select a class: Warrior, Mage, Rogue")
        class_name = input()
        class_instance = get_class_choice(class_name)
        if class_instance is None:
            return "Invalid class"
        self.character_class = class_name
        class_instance.stats(self)
        return class_name

    def __str__(self):
        name = self.create_player()
        if name == "Name must be between 3 and 10 characters":
            return name

        classes = self.select_class()
        if classes == "Invalid class":
            return classes

        return f"Hello {self.name}, here is your character as a {self.character_class} \nName: {self.name}, Attack: {self.attack}, Defense: {self.defense}, HP: {self.hp}, Mana: {self.mana},Intelligence: {self.intelligence}, Magic Resistance:{self.mr}, Agility:{self.agility}, Chance: {self.chance}, Stamina: {self.stamina}, Spirit:{self.spirit} Class: {self.character_class}, Inventory: {self.inventory}"

