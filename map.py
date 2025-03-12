from room import roomInfo
import random

class Map:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.room = []
        self.roomInfo(self)

    def room(self):
        empty = 0
        treasure = 1
        monster = 2

        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(random.choice([empty, treasure, monster]))
            self.room.append(row)
    
    def createRoom(self):
        for row in self.room:
            print(row)

        


