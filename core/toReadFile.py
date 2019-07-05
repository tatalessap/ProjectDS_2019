import re
import math
from classes import *

def ReadIstance(namefile):
    nodesL = [];
    nodesB = [];
    arcsL = [];
    arcsB = [];

    in_file = open(namefile, "r")

    nCustomers = int(in_file.readline())  #number of costumers

    in_file.readline()

    nVehicles = int(in_file.readline())  #number of vehicles

    mystring = in_file.readline()  # Deposit

    mysplit = clearSplit(mystring)

    deposit = Node(0, float(mysplit[0]), float(mysplit[1]), False, "D", 0)

    vehiclesCapacity = mysplit[3]

    "per i clienti"
    for i in range(nCustomers):
        mystring = in_file.readline()
        mysplit = clearSplit(mystring)

        if int(mysplit[2]) != 0:
            nodesL.append(Node(i+1, mysplit[0]), mysplit[1], False, "L", mysplit[2]) #index, X, Y, visited, type and quantity

        else:
            nodesB.append(Node(i+1, mysplit[0]), mysplit[1], False, "B", mysplit[3])  # index, X, Y, visited, type and quantity


    for i in range(len(nodesL)):
        for j in range(i+1, len(nodesL), 1):
            arcsL.append(Arc(nodesL[i]), nodesL[j], deposit)

    arcsL.sort(key=getSaving(), reverse=True)

    for i in range(len(nodesB)):
        for j in range(i+1, len(nodesB), 1):
            arcsL.append(Arc(nodesB[i]), nodesB[j], deposit)

    arcsL.sort(key=getSaving(), reverse=True)

    return nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles


def clearSplit(l):
    splitl = re.findall(r"[-+]?\d*\.\d+|\d+", l)
    return splitl
