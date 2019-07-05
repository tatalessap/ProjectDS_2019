import math


class Node:
    def __init__(self, index, x, y, visited, nodetype, quantity):
        self.index = index
        self.x = x
        self.y = y
        self.visited = visited
        self.type = nodetype
        self.quantity = quantity


class Arc:
    def __init__(self, node1, node2, deposit):
        self.nodes = [node1, node2]
        self.cost = math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
        self.saving = math.sqrt((node1.x - deposit.x) ** 2 + (node1.y - deposit.y) ** 2) + math.sqrt((deposit.x - node2.x) ** 2 + (deposit.y - node2.y) ** 2) - self.cost
        self.arcType = node1.type + node2.type


class Route:
    def __init__(self, index, capacity):
        self.index = index
        self.totalCost = 0
        self.capacity = capacity
        self.load = 0
        self.route = []
        self.indexTale = 0
        self.indexHead = 0

    def firstAdd(self, arc):
        if arc.nodes[0].quantity + arc.nodes[1].quantity > self.capacity:
            return False

        self.route.append(arc.nodes[0])
        self.indexTale = arc.nodes[0].index
        self.route.append(arc.nodes[1])
        self.indexHead = arc.nodes[1].index

        arc.nodes[0].visited = True
        arc.nodes[1].visited = True

        self.totalCost = arc.cost
        self.load = arc.nodes[0].quantity + arc.nodes[1].quantity

        return True

    def add(self, arc, n, position):
        if self.load + arc.nodes[n].quantity > self.capacity:
            return False

        if position == "h":
            self.route.append(arc.nodes[n])
            self.indexHead = arc.nodes[n].index
        if position == "t":
            self.route.insert(0, arc.nodes[n])
            self.indexTale = arc.nodes[n].index

        arc.nodes[n].visited = True
        self.totalCost = self.totalCost + arc.cost
        self.load = self.load + arc.nodes[n].quantity

        return True
