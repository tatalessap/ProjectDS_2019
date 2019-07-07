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
    arcs = []
    capacity=routesL[0].capacity
    for i in range(len(routesL)):
        for j in range(len(routesB)):
            arcs.append((Arc(routesL[i].route[0], routesB[j].route[0], deposit), i, j, "t", "t"))
            arcs.append((Arc(routesL[i].route[0], routesB[j].route[len(routesB[j].route)-1], deposit), i, j, "t", "h"))
            arcs.append((Arc(routesL[i].route[len(routesL[i].route)-1], routesB[j].route[0], deposit), i, j, "h", "t"))
            arcs.append((Arc(routesL[i].route[len(routesL[i].route)-1], routesB[j].route[len(routesB[j].route)-1], deposit)
                         , i, j, "h", "h"))
    arcs.sort(key=lambda item: item[0].cost)

    routes = []

    for p in range(len(routesB)):
        for i in range(len(arcs)):
            if(not(routesL[arcs[i][1]].merged) and not(routesB[arcs[i][2]].merged)):
                routesL[arcs[i][1]].merged = True
                routesB[arcs[i][2]].merged = True
                routes.append(Route(p,capacity))
                routes[p].totalCost = routesL[arcs[i][1]].totalCost + routesB[arcs[i][2]].totalCost + arcs[i][0].cost
                routes[p].route =  routesL[arcs[i][1]].route
                if(arcs[i][3]=="t"):
                    routes[p].route.reverse()
                if(arcs[i][4]=="h"):
                    routes[p].route=routes[p].route+routesB[arcs[i][2]].route.reverse()
                else:
                    routes[p].route=routes[p].route+routesB[arcs[i][2]].route
                routes[p].totalCost = routes[p].totalCost + Node.distance(deposit, routes[p].route[0]) + \
                                      Node.distance(deposit, routes[p].route[len(routes[p].route)-1])
                routes[p].route.append(deposit)
                routes[p].route.insert(0, deposit)
                routes[p].indexHead = 0
                routes[p].indexTale = 0
                break


    for i in range(len(routesL)):
        if (not (routesL[i].merged)):
            p = len(routes)
            routesL[i].merged = True
            routes.append(routesL[i])
            routes[p].totalCost = routes[p].totalCost + Node.distance(deposit, routes[p].route[0]) + \
                                  Node.distance(deposit, routes[p].route[len(routes[p].route) - 1])
            routes[p].route.append(deposit)
            routes[p].route.insert(0, deposit)
            routes[p].indexHead = 0
            routes[p].indexTale = 0

    return routes

