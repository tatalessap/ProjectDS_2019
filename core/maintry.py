from core.classes import *
from core.toReadFile import *
from core.toSolve import *
import os

directory = 'istances'
error = 0

filename = ("D1.txt")

nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = readIstance("istances/" + filename)

solution = readSolution("RPA_Solutions/Detailed_Solution_" + filename)

routesL = []

routesB = []

solved(arcsL, routesL, nVehicles, vehiclesCapacity, nodesL, deposit)

solved(arcsB, routesB, nVehicles, vehiclesCapacity, nodesB, deposit)

routes = mergeRoutes(routesL, routesB, deposit)

print("\n" + filename)

for i in range(len(nodesL)):
    if not nodesL[i].visited:
        print(str(i) + " (L) is not visited with capacity "+str(nodesL[i].demand)+". Vehicle capacity is "+str(vehiclesCapacity))

for i in range(len(nodesB)):
    if not nodesB[i].visited:
        print(str(i) + " (B) is not visited")

totalAllCost = 0

for i in range(len(routes)):
    totalAllCost = totalAllCost + routes[i].totalCost

print(str("\t Our solution:         " + str(totalAllCost)))

print("\t Optimal solution:     " + solution)

print("\t Absolute error:       " + str(abs(totalAllCost - float(solution))/float(solution)))

error = error + (abs(totalAllCost - float(solution))/float(solution))








