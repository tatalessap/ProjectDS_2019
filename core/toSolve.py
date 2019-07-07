from core.classes import *


def solved(arcs, routes, nVehicles, vehiclesCapacity):
    """
    The function takes the necessary parameters as input to create a route to L or B. (which will be merged next.)
    :param arcs:
    :param routes:
    :param nVehicles:
    :param vehiclesCapacity:
    :return:
    """

    # phase 1
    # initialization of routes, insertion of the first arc.
    i: int = 0
    start: int = 0
    keep: bool = True
    while i < nVehicles and keep:
        found = False
        while not found:
            found, arc, start = searchArcNotVisited(start, arcs)
            if found:
                routes.append(Route(i, vehiclesCapacity))
                found = routes[i].firstAdd(arc)
            else:
                found = True
                keep = False
        i = i + 1

    #  phase 2
    #  Each route has a Boolean associated with it.
    #  This Boolean indicates if the route still has load available to be able to insert available arcs.
    tupleRouteCheck = []

    for r in range(len(routes)):
        tupleRouteCheck.append([routes[r], True])

    checkAllRoute: bool = True  # if this check is False, not more arcs to visited

    while checkAllRoute:
        tupleRouteCheck.sort(key=lambda item: item[0].load)  # sort by most capacity left
        # Continue to add Arcs until the routes are saturated
        for r in range(len(routes)):
            if tupleRouteCheck[r][1]:
                reStart: int = 0
                found: bool = False
                while not found:
                    arc, indexPosition, typeHT, reStart = searchArcOneNotVisited(reStart, arcs,
                                                                                 tupleRouteCheck[r][0].indexHead,
                                                                                 tupleRouteCheck[r][0].indexTale)
                    if reStart < len(arcs):  # if there are other arc to check
                        found = tupleRouteCheck[r][0].add(arc, indexPosition, typeHT)
                    else:
                        found = True  # there are no more arcs available for that route
                        tupleRouteCheck[r][1] = False
        checkAllRoute = False  # reset for the check
        for r in range(len(routes)):
            checkAllRoute = checkAllRoute or tupleRouteCheck[r][1]  # there are more arcs to add (check = true ) or not

    return routes


def searchArcNotVisited(start, arcs):
    """
    For the initialization of Routes, it renders an arc only if both nodes are not visited
    :param arcs:
    :param start: where to start the search
    :return: True if there are arc e the arc.
    """
    for i in range(start, len(arcs)):
        if not arcs[i].nodes[0].visited and not arcs[i].nodes[1].visited:
            return True, arcs[i], i+1
    return False, None, -1


def searchArcOneNotVisited(start, arcs, indexHead, indexTale):
    """
    To add valid nodes to the route
    :param start: where to start the search
    :param arcs:
    :param indexHead: head of the route
    :param indexTale: tale of the route
    :return:
    """
    for i in range(start, len(arcs), 1):
        if arcs[i].nodes[0].visited ^ arcs[i].nodes[1].visited:  # use of xor
            if arcs[i].nodes[0].index == indexHead:
                return arcs[i], 1, "h", i + 1

            if arcs[i].nodes[1].index == indexHead:
                return arcs[i], 0, "h", i + 1

            if arcs[i].nodes[0].index == indexTale:
                return arcs[i], 1, "t", i + 1

            if arcs[i].nodes[1].index == indexTale:
                return arcs[i], 0, "t", i + 1

    return None, -1, 'None', len(arcs)


def mergeRoutes(routesL, routesB, deposit):
    """
    This function merges  Linehaul routes with a BackHaul routes, and add deposit at start and finish
    :param routesL: List of LineHaul routes
    :param routesB: List of BackHaul routes
    :param deposit: Deposit node
    :return: List of merged routes
    """
    arcs = []  # List of arcs between Linehaul and BackHaul routes
    capacity = routesL[0].capacity  # Capacity of LineHaul routes
    routes = [] # Routes list to return

    # For all routes append arcs between all heads and all tales saving in the tuple routes indexes and head or tale
    for i in range(len(routesL)):
        for j in range(len(routesB)):
            arcs.append((Arc(routesL[i].destinations[0], routesB[j].destinations[0], deposit), i, j, "t", "t"))
            arcs.append(
                (Arc(routesL[i].destinations[0], routesB[j].destinations[len(routesB[j].destinations) - 1], deposit), i, j, "t", "h"))
            arcs.append(
                (Arc(routesL[i].destinations[len(routesL[i].destinations) - 1], routesB[j].destinations[0], deposit), i, j, "h", "t"))
            arcs.append(
                (Arc(routesL[i].destinations[len(routesL[i].destinations) - 1], routesB[j].destinations[len(routesB[j].destinations) - 1], deposit)
                 , i, j, "h", "h"))
    # Sort arcs in term of saving
    arcs.sort(key=lambda item: item[0].saving, reverse=True)

    i=0
    for p in range(len(routesB)):   # Every loop is a merge of a BackHaul route
        isRouteAdded = False
        while not isRouteAdded:  # Until the route is added we check arcs[i]
            if not routesL[arcs[i][1]].merged and not routesB[arcs[i][2]].merged:   # If the arc can be used
                routesL[arcs[i][1]].merged = True   # Mark routes of the arc as merged
                routesB[arcs[i][2]].merged = True
                routes.append(Route(p, capacity))   # Create new empty route with LineHaul capacity
                # Cost of the L-B route, still no deposit
                routes[p].totalCost = routesL[arcs[i][1]].totalCost + routesB[arcs[i][2]].totalCost + arcs[i][0].cost
                routes[p].destinations = routesL[arcs[i][1]].destinations  # The LineHaul route is added
                if arcs[i][3] == "t":
                    routes[p].destinations.reverse()   # If necessary, the route is reversed
                if arcs[i][4] == "h":
                    routesB[arcs[i][2]].destinations.reverse() #If necessary, the BackHaul route is also reversed
                routes[p].destinations = routes[p].destinations + routesB[arcs[i][2]].destinations   # BackHaul route added

                # Add deposit
                addDeposit(routes[p],deposit)
                isRouteAdded = True
            i=i+1

    for i in range(len(routesL)):   # There may be LineHaul routes left
        if not routesL[i].merged:   # If the route hasn't been merged
            p = len(routes)
            routesL[i].merged = True
            routes.append(routesL[i])   # Add route of pure Linehaul
            # Add deposit
            addDeposit(routes[p],deposit)

    return routes


def addDeposit(route, deposit):
    """
    This function adds a deposit node at the start and at the end of a route, updating the total cost of the route
    :param route: Route to update
    :param deposit: Deposit to add
    :return:
    """
    route.totalCost = route.totalCost + Node.distance(deposit, route.destinations[0]) + \
                          Node.distance(deposit, route.destinations[len(route.destinations) - 1])
    route.destinations.append(deposit)
    route.destinations.insert(0, deposit)
    route.indexHead = 0
    route.indexTale = 0