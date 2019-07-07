'''
Created on 29 mag 2019

@author: ronco
'''
import re
import math
def ReadIstance(namefile):
    vectorX=[] #coordinata X
    vectorY=[] #coordinata Y
    listQuery=[] #domande dei clienti
    listForniture=[] #forniture dei fornitori
    listL=[] #lista degli indici dei clienti [a chi consegno]
    listB=[] #lista degli indici dei fornitori 
    
    in_file=open(namefile,"r")
    nCustomers=int(in_file.readline())      #Numero clienti
    in_file.readline()
    nVehicles=int(in_file.readline())        #Numero veicoli
    
    "per il deposito"
    mystring=in_file.readline() #Deposito 
    mysplit=clearSplit(mystring)
    vectorX.append(int(mysplit[0]))
    vectorY.append(int(mysplit[1]))
    capacity=mysplit[3]
    
    "per i clienti"
    for i in range(nCustomers):
        mystring=in_file.readline() 
        mysplit=clearSplit(mystring)
        vectorX.append(int(mysplit[0]))
        vectorY.append(int(mysplit[1]))
        if int(mysplit[2])!=0:
            listL.append(i+1)
            listQuery.append(int(mysplit[2]))
        else:
            listB.append(i+1)
            listForniture.append(int(mysplit[3]))
    
    return nCustomers, nVehicles, vectorX, vectorY, listQuery, listForniture, listL, listB, capacity
            

    
def clearSplit(l):
    splitl = re.findall(r"[-+]?\d*\.\d+|\d+", l)
    return splitl

def buildMetric(vectorX,vectorY):
    M=[]
    for i in range(len(vectorX)):
        p=[]
        for j in range(len(vectorX)):
            p.append(math.sqrt((vectorX[i]-vectorX[j])**2+(vectorY[i]-vectorY[j])**2))
        M.append(p)
    return M
