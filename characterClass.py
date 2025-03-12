def getClassStats(character):
    if character.characterClass == "Warrior":
        character.pv = 150
        character.mana = 50
        character.attack = 15
        character.intelligence = 5
        character.defense = 12
        character.mr = 6
        character.agility = 8
        character.chance = 5
        character.stamina = 10
        character.spirit = 4
    elif character.characterClass == "Mage":
        character.pv = 90
        character.mana = 150
        character.attack = 4
        character.intelligence = 15
        character.defense = 5
        character.mr = 12
        character.agility = 7
        character.chance = 6
        character.stamina = 5
        character.spirit = 10
    elif character.characterClass == "Rogue":
        character.pv = 110
        character.mana = 70
        character.attack = 10
        character.intelligence = 7
        character.defense = 8
        character.mr = 7
        character.agility = 15
        character.chance = 12
        character.stamina = 7
        character.spirit = 6
    else:
        return "This class does not have boost actually"
