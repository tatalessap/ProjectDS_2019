import math


class Node:
    """
    This class represent nodes
    """
    def __init__(self, index, x, y, visited, demand):
        """
        Node constructor
        :param index: Node index
        :param x: X coordinate
        :param y: Y coordinate
        :param visited: Boolean
        :param demand:  Root quantity to give or take
        """
        self.index = index
        self.x = x
        self.y = y
        self.visited = visited
        self.demand = demand

    @staticmethod
    def distance(node1, node2):
        """
        Static method that returns the distance between two nodes
        :param node1:
        :param node2:
        :return:
        """
        return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


class Arc:
    """
    This class represent arcs and their savings for a given deposit.
    """
    def __init__(self, node1, node2, deposit):
        """
        Arc constructor
        :param node1: First Node of the arc
        :param node2: Second Node of the arc
        :param deposit: Deposit to consider for the saving computation
        """
        self.nodes = [node1, node2]
        self.cost = Node.distance(node1,node2)
        self.saving = Node.distance(node1,deposit) + Node.distance(node2,deposit) - self.cost


class Route:
    """
    This class represent arcs and their savings for a given deposit.
    """
    def __init__(self, index, capacity):
        """
        Route constructor
        :param index: Route index
        :param capacity: Vehicle capacity
        """
        self.index = index
        self.totalCost = 0  # Cost of the route
        self.capacity = capacity
        self.load = 0  #Current load of the route
        self.route = [] # List of route's nodes
        self.indexTale = 0  # Index of the first visited node
        self.indexHead = 0  # Index of the last visited node
        self.merged = False  #Boolean attribute for the merging process

    def firstAdd(self, arc):
        """
        This function adds two nodes in the route, given by an arc
        :param arc: Arc to add
        :return: Boolean indicating if the adding process is completed
        """
        if arc.nodes[0].demand + arc.nodes[1].demand > self.capacity:   # If capacity isn't enough
            return False
        self.route.append(arc.nodes[0])  # Both nodes of the arc are added
        self.route.append(arc.nodes[1])
        arc.nodes[0].visited = True  # Nodes marking
        arc.nodes[1].visited = True
        self.indexTale = arc.nodes[0].index  # Tale and head index upgrade
        self.indexHead = arc.nodes[1].index
        arc.nodes[0].visited = True  # Nodes marking
        arc.nodes[1].visited = True
        self.totalCost = arc.cost  # Cost update
        self.load = arc.nodes[0].demand + arc.nodes[1].demand  # Load update
        return True

    def add(self, arc, chosen, position):
        """
        This function adds on node in the route, given by an arc and his position in the arc, in the correct position.
        :param arc: Arc to consider
        :param chosen: Node of the arc chosen (0 or 1)
        :param position: Head or Tale
        :return: Boolean indicating if the adding process is completed
        """

        if arc is None:  #If the arc is empty
            return False
        if self.load + arc.nodes[chosen].demand > self.capacity:   # If capacity isn't enough
            return False
        if position == "h":  #Head adding
            self.route.append(arc.nodes[chosen])
            self.indexHead = arc.nodes[chosen].index
        if position == "t":  #Tale adding
            self.route.insert(0, arc.nodes[chosen])
            self.indexTale = arc.nodes[chosen].index
        arc.nodes[chosen].visited = True  #Node marking
        self.totalCost = self.totalCost + arc.cost  #Cost update
        self.load = self.load + arc.nodes[chosen].demand  #Load update
        return True
