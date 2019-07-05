import math


class Node:
    def __init__(self, index, x, y, visited, type, quantity):
        self.index = index
        self.x = x
        self.y = y
        self.visited = visited
        self.type = type
        self.quantity = quantity;


class Arc:
    def __init__(self, node1, node2, deposit):
        self.node1 = node1
        self.node2 = node2
        self.cost = math.sqrt((node1.x-node2.x)**2 + (node1.y-node2.y)**2)
        self.saving = math.sqrt((node1.x - deposit.x)**2+(node1.y-deposit.y)**2) + math.sqrt((deposit.x - node2.x)**2 + (deposit.y - node2.y)**2) - self.cost
        self.arcType = node1.type + node2.type


    def getCost(self):
        print(self.cost)

    def getSaving(self):
        return self.saving

    def getArcType(self):
        return self.arcType


class Route:
    pass
