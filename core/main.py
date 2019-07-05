from core.classes import *
from core.toReadFile import *
from core.toSolve import *

node1 = Node(1, 1, 1, False, "L", 3)
node2 = Node(2, 2, 2, False, "L", 3)
deposit = Node(0,0,0, False, "D", 0)
arc = Arc(node1, node2, deposit)

nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = readIstance("istances/A1.txt")

routes=[nVehicles]

solved(arcsL, routes)


