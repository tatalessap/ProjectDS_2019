from core.classes import *
from core.toReadFile import *
from core.toSolve import *
import os

directory = '/home/tatalessap/PycharmProjects/ProjectDS_2019/core/istances'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):

        nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles = readIstance("istances/"+filename)

        routesL = []

        routesB = []

        solved(arcsL, routesL, nVehicles, vehiclesCapacity)

        solved(arcsB, routesB, nVehicles, vehiclesCapacity)

        routes = mergeRoutes(routesL, routesB, deposit)

        print("\n" + filename)

        for i in range(len(nodesL)):
            if not nodesL[i].visited:
                print(str(i) + " (L) is not visited")

        for i in range(len(nodesB)):
            if not nodesB[i].visited:
                print(str(i) + " (B) is not visited")

        totalAllCost = 0

        for i in range(len(routes)):
            totalAllCost = totalAllCost + routes[i].totalCost

        print(str(totalAllCost))







