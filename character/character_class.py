from character.classes.mage import Mage
from character.classes.warrior import Warrior
from character.classes.rogue import Rogue

def get_class_choice(class_name):
    class_choice = {
        "Warrior": Warrior(),
        "Mage": Mage(),
        "Rogue": Rogue()
    }
    return class_choice.get(class_name)
