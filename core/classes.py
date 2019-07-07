import math


class Node:
    def __init__(self, index, x, y, visited, nodetype, quantity):
        self.index = index
        self.x = x
        self.y = y
        self.visited = visited
        self.type = nodetype
        self.quantity = quantity

    @staticmethod
    def distance(node1, node2):
        return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


class Arc:
    def __init__(self, node1, node2, deposit):
        self.nodes = [node1, node2]
        self.cost = Node.distance(node1,node2)
        self.saving = Node.distance(node1,deposit) + Node.distance(node2,deposit) - self.cost
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
        self.merged = False

    def firstAdd(self, arc):
        if arc.nodes[0].quantity + arc.nodes[1].quantity > self.capacity:
            print(str(a)+" > "+str(self.capacity))
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

    def add(self, arc, position, typeHT):
        if arc is None:
            return False
        if self.load + arc.nodes[position].quantity > self.capacity:
            return False
        if typeHT == "h":
            self.route.append(arc.nodes[position])
            self.indexHead = arc.nodes[position].index
        if typeHT == "t":
            self.route.insert(0, arc.nodes[position])
            self.indexTale = arc.nodes[position].index
        arc.nodes[position].visited = True
        self.totalCost = self.totalCost + arc.cost
        self.load = self.load + arc.nodes[position].quantity
        return True
