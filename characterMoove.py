class CharacterMoove:
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.map = map

    def move(self, direction):
        print("Veuillez rentrée une commande de deplacement:\n N: Nord\n S: Sud\n E: Est\n O: Ouest")
        direction = input()
        if direction == "N":
            self.y -= 1
            return self.y
        if direction == "S":
            self.y += 1
            return self.y
        if direction == "E":
            self.x += 1
            return self.x
        if direction == "O":
            self.x -= 1
            return self.x
        else:
            return "Direction invalide"