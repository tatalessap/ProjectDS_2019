from classes import *


def solved(arcs, routes):
    flagSolved=True
    i=0

    #phase 1
    for i in range(len(routes)):
        while(not(flagSolved)):
            arc=searchArcNotVisited(arcs)
            flagSolved=routes[i].firstAdd(arc)

    #phase 2
    j=0
    flagSolved=True

    for i in range(len(routes)):
        while(not(flagSolved)):
            arc, indexPosition, typeHT, j = searchArcOneNotVisited(arcs, j, routes[i].indexHead, routes[i].indexTale)
            flagSolved=routes[i].add(arc, indexPosition, typeHT)

    return routes



def searchArcNotVisited(arcs):
    for i in range(len(arcs)):
        if((not(arcs[i].nodes[0].visited))and(not(arcs[i].nodes[1].visited))):
            return arcs[i]
    return None


def searchArcOneNotVisited(start, arcs, indexHead, indexTale):

    for i in range(start, len(arcs), 1):

        if((not (arcs[i].nodes[0].visited)) ^ (not (arcs[i].nodes[1].visited))):

            if(arcs[i].nodes[0].index == indexHead):
                return arcs[i], 0, "h", i

            if (arcs[i].nodes[1].index == indexHead):
                return arcs[i], 1, "h", i

            if (arcs[i].nodes[0].index == indexTale):
                return arcs[i], 0, "t", i

            if (arcs[i].nodes[1].index == indexTale):
                return arcs[i], 1, "t", i

    return None, -1, 'None'