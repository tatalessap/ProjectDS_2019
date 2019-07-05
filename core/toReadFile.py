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

    deposit = Node(0, float(mysplit[0]), float(mysplit[1]),)

    vehiclesCapacity = mysplit[3]

    "per i clienti"
    for i in range(nCustomers):
        mystring = in_file.readline()
        mysplit = clearSplit(mystring)

        if int(mysplit[2]) != 0:

        else:


    return nCustomers, nVehicles, capacity


def clearSplit(l):
    splitl = re.findall(r"[-+]?\d*\.\d+|\d+", l)
    return splitl
