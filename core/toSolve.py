from core.classes import *

def solved(arcs, routes, nVehicles, vehiclesCapacity):


    #phase 1
    for i in range(nVehicles):
        flagSolved = False
        while(not(flagSolved)):
            found, arc=searchArcNotVisited(arcs)
            if(found):
                routes.append(Route(i, vehiclesCapacity))
                flagSolved = routes[i].firstAdd(arc)
            else:
                flagSolved=True
                i=nVehicles



    #phase 2
    for i in range(len(routes)):
        j = 0
        flagSolved = False
        while(not(flagSolved)):
            arc, indexPosition, typeHT, j = searchArcOneNotVisited(j, arcs, routes[i].indexHead, routes[i].indexTale)
            if (j < len(arcs)):
                flagSolved = routes[i].add(arc, indexPosition, typeHT)
            else:
                flagSolved = True
    return routes



def searchArcNotVisited(arcs):
    for i in range(len(arcs)):
        if((not(arcs[i].nodes[0].visited))and(not(arcs[i].nodes[1].visited))):
            return True, arcs[i]
    return False, None


def searchArcOneNotVisited(start, arcs, indexHead, indexTale):

    for i in range(start, len(arcs), 1):

        if ((arcs[i].nodes[0].visited) ^ (arcs[i].nodes[1].visited)):

            if(arcs[i].nodes[0].index == indexHead):
                return arcs[i], 1, "h", i+1

            if (arcs[i].nodes[1].index == indexHead):
                return arcs[i], 0, "h", i+1

            if (arcs[i].nodes[0].index == indexTale):
                return arcs[i], 1, "t", i+1

            if (arcs[i].nodes[1].index == indexTale):
                return arcs[i], 0, "t", i+1

    return None, -1, 'None', len(arcs)

def mergeRoutes(routesL, routesB, deposit):
    arcs=[]
    for i in range(len(routesL)):
        for j in range(len(routesB)):
            arcs.append(Arc(routesL[i].route[0], routesB[j].route[0], deposit))
            arcs.append(Arc(routesL[i].route[0], routesB[j].route[len(routesB[j].route)-1], deposit))
            arcs.append(Arc(routesL[i].route[len(routesL[i].route)-1], routesB[j].route[0], deposit))
            arcs.append(Arc(routesL[i].route[len(routesL[i].route)-1], routesB[j].route[len(routesB[j].route)-1], deposit))

    arcs.sort(key=lambda Arc: Arc.saving, reverse=True)
    print("done")