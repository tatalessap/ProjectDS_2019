'''
Created on 21 mag 2019

@author: ronco
'''
from old import mylib
from old.mylib import ReadIstance, buildMetric
from _ctypes import sizeof
if __name__ == '__main__':
    nCustomers, nVehicles, vectorX, vectorY, listQuery, listForniture, listL, listB, capacity=ReadIstance("Istanze\A1.txt")
    "distanze calcolate tra posizione i-esima e posizione j-esima M[i][j]"
    M=buildMetric(vectorX,vectorY) 