from core.classes import *
from core.toReadFile import *
from core.toSolve import *

#node1 = Node(1, 1, 1, False, "L", 3)
#node2 = Node(2, 2, 2, False, "L", 3)
#deposit = Node(0,0,0, False, "D", 0)
#arc = Arc(node1, node2, deposit)

nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = readIstance("istances/A1.txt")

routesL=[]
routesB=[]
solved(arcsL, routesL, nVehicles, vehiclesCapacity)
solved(arcsB, routesB, nVehicles, vehiclesCapacity)

print("len(nodesL) = " + str(len(nodesL)))

for i in range(len(nodesL)):
    if not(nodesL[i].visited):
        print(str(i)+" is not visited")

for i in range(len(nodesB)):
    if not(nodesB[i].visited):
        print(str(i)+" is not visited")




