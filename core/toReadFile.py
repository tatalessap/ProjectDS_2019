import re
from core.classes import *


def readIstance(namefile):
    """
    This function reads a given .txt file representing an istance of the CVRP problem with LineHaul and Backhaul nodes.
    It returns proper data structures for the resolution.
    :param namefile:
    :return:
    """

    # Lists inizialization
    nodesL = []
    nodesB = []
    arcsL = []
    arcsB = []
    in_file = open(namefile, "r")
    nCustomers = int(in_file.readline())  # number of costumers
    in_file.readline()
    nVehicles = int(in_file.readline())  # number of vehicles
    mystring = in_file.readline()  # Deposit line
    mysplit = clearSplit(mystring)  # Undesired characters removal
    deposit = Node(0, float(mysplit[0]), float(mysplit[1]), False, 0)  # Deposit creation
    vehiclesCapacity = int(mysplit[3])  # Vehicles Capacity

    for i in range(nCustomers):  # Node lists creation
        mystring = in_file.readline()
        mysplit = clearSplit(mystring)
        if int(mysplit[2]) != 0:
            nodesL.append(Node(i+1, float(mysplit[0]), float(mysplit[1]), False, int(mysplit[2])))
        else:
            nodesB.append(Node(i+1, float(mysplit[0]), float(mysplit[1]), False, int(mysplit[3])))

    for i in range(len(nodesL)):  # LineHaul arcs creation and sorting
        for j in range(i+1, len(nodesL), 1):
            arcsL.append(Arc(nodesL[i], nodesL[j], deposit))
    arcsL.sort(key=lambda item: item.saving, reverse=True)

    for i in range(len(nodesB)):  # BackHaul arcs creation and sorting
        for j in range(i+1, len(nodesB), 1):
            arcsB.append(Arc(nodesB[i], nodesB[j], deposit))
    arcsB.sort(key=lambda item: item.saving, reverse=True)

    return nodesL, nodesB, arcsL, arcsB, nCustomers, deposit, vehiclesCapacity, nVehicles


def clearSplit(l):
    """
    This function removes undesired ASCII characters from a string.
    :param l:
    :return:
    """
    return re.findall(r"[-+]?\d*\.\d+|\d+", l)
