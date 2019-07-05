from classes import *
from toReadFile import *

node1 = Node(1, 1, 1, False, "L", 3)
node2 = Node(2, 2, 2, False, "L", 3)
deposit = Node(0,0,0, False, "D", 0)
arc = Arc (node1, node2, deposit)

nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = ReadIstance("istances\A1.txt")

#for i in range(len(arcsL)):
   # print("\n"+str(i)+"    "+str(arcsL[i].saving))

