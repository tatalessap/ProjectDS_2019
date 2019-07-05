from classes import *
nodo1 = Node(4,2,2,'false')
nodo2 = Node(5,1,1,'false')
deposit = Node(0,0,0,'false')
arco = Arc(nodo1,nodo2,deposit)
print(arco.getSaving())
