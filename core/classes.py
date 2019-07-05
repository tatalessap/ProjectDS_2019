import math


class Node:
    def __init__(self, id,x,y,visited):
        self.id=id
        self.x=x
        self.y=y
        self.visited=visited


class Arc:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        self.cost=math.sqrt((i.x-j.x)**2+(i.y-j.y)**2)

    def getCost(self):
        print(self.cost)


class Route:
    pass