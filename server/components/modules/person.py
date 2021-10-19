from enum import Enum


class Status(Enum):
    Works = 1
    Dines = 2
    Resting = 3
    At_the_meeting = 4
    Game = 5


class Pos:
    PosX = 0
    PosY = 0

    def __init__(self, X=0, Y=0):
        self.PosX = X
        self.PosY = Y

    def getPosX(self):
        return self.PosX

    def getPosY(self):
        return self.PosY

    def SetPosX(self, X):
        self.PosX = X

    def SetPosY(self, Y):
        self.PosY = Y

    def SetPos(self, X, Y):
        self.PosX = X
        self.PosY = Y


class Person:

    def __init__(self, id, position = Pos()):
        self.id = id
        self.stat = Status.Works
        self.position = position

    def GetId(self):
        return self.id

    def GetStatus(self):
        return self.stat

    def GetPos(self):
        return self.position

    def GetPosX(self):
        return self.position.getPosX()

    def GetPosY(self):
        return self.position.getPosY()

    def SetId(self, id):
        self.id = id

    def SetStatus(self, stat):
        self.stat = stat

    def SetPos(self, position):
        self.position = position

    def SetPos(self, X, Y):
        self.position.SetPosX(X)
        self.position.SetPosY(Y)

    def SetPosX(self, X):
        self.position.SetPosX(X)

    def SetPosY(self, Y):
        self.position.SetPosY(Y)

    def SetStatAndPos(self, stat, position):
        self.stat = stat
        self.position = position

    def toString(self):
        print("The id employee: ", self.id)
        print("Status: ", self.stat)
        print("Located in: ", str(self.GetPosX()), " ", self.GetPosY())
