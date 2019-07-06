from core.classes import *
from core.toReadFile import *
from core.toSolve import *

nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = readIstance("istances/A1.txt")

routesL=[]
routesB=[]
solved(arcsL, routesL, nVehicles, vehiclesCapacity)
solved(arcsB, routesB, nVehicles, vehiclesCapacity)

print("len(nodesL) = " + str(len(nodesL)))

print("len(route) = " + str(len(routesB)))

for i in range(len(nodesL)):
    if not(nodesL[i].visited):
        print(str(i)+" is not visited")

for i in range(len(nodesB)):
    if not(nodesB[i].visited):
        print(str(i)+" is not visited")




