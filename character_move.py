class CharacterMove:
    def __init__(self, startX, startY, gameMap, character):
        self.startX = startX
        self.startY = startY
        self.gameMap = gameMap
        self.character = character

    def move(self, direction):
        print("Enter an input for mooving:\n N: North\n S: South\n E: East\n W: West")
        direction = input()
        if direction == "N":
            self.startY - 1
            return self.startY
        if direction == "S":
            self.startY + 1
            return self.startY
        if direction == "E":
            self.startX + 1
            return self.startX
        if direction == "W":
            self.startX - 1
            return self.startX
        else:
            return "Invalid input"