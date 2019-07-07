from core.classes import *
from core.toReadFile import *
from core.toSolve import *

nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = readIstance("istances/J3.txt")

routesL=[]
routesB=[]
solved(arcsL, routesL, nVehicles, vehiclesCapacity)
solved(arcsB, routesB, nVehicles, vehiclesCapacity)

routes = mergeRoutes(routesL, routesB, deposit)

for i in range(len(nodesL)):
    if not nodesL[i].visited:
        print(str(i)+" (L) is not visited")

for i in range(len(nodesB)):
    if not nodesB[i].visited :
        print(str(i)+" (B) is not visited")

for i in range(len(routes)):
    print("Route: "+str(i)+"\n")
    for j in range(len(routes[i].route)):
        print(str(routes[i].route[j].index)+" ")
    print("\n\n")

totalAllCost = 0

for i in range(len(routes)):
    totalAllCost = totalAllCost+routes[i].totalCost

print(str(totalAllCost))


