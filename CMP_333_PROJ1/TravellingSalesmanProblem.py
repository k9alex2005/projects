# Kevin Koshy 
# b00098368
# Jerusha Paul
# g00100797
# Aly Mahmoud 
# b00101376
# Farah Jayas 
# g00100715

from AI_problem import SearchProblem
from AI_heuristics import AI_heuristics

class TravellingSalesmanProblem (SearchProblem):
    #! this class implements the CLASSIC TSP, in which every vertex must be visited exactly once
    #! we store the graph as an adjacency list
    #! each entry in the list is an array of tuples (adjVertexIndex, distance)
    #! we also store the current position (index) of the salesman
    def __init__(self, graph, startIndex):
        self.adjList = list(graph)
        self.vertexCount = len(self.adjList)
        self.startIndex = startIndex
        #! for heuristic purpose, we store the average weight
        count = 0
        self.avgWeight = 0
        for i in graph:
            for j in i:
                self.avgWeight += j[1]
                count += 1
        self.avgWeight /= count

    #! a state is the index of the current position, an ordered list of all visited vertices, and the current walk cost
    #! example (3, [0, 3, 1, 2, 1, 3], 9)
    def getStartState(self):
        return (self.startIndex, [self.startIndex], 0)
    
    def isGoalState(self, state):
        #! check if each node has been visited
        for i in range(self.vertexCount):
            try:
                state[1].index(i)
            except ValueError:
                return False #! in this case, at least one vertex was not visited
        #! getting here means that all vertices have been visited AT LEAST one time
        #! because of the logic in getSuccessors, no vertex will ever be visited > one time, except the starting one
        #! confirm that the walk is a cycle
        if state[0] == self.startIndex:
            return True
        else:
            return False

    
    def getSuccessors(self, state):
        successors = []

        currentPos = state[0]

        visitedArrayCopy = list(state[1])
        #! in this case, no successors
        if visitedArrayCopy[-1] == visitedArrayCopy[0] and len(visitedArrayCopy) != 1:
            return []

        for edge in self.adjList[currentPos]:
            adjVertex, edgeCost = edge
            visitedArrayCopy = list(state[1])

            addNode = False
            try:
                indx = visitedArrayCopy.index(adjVertex)
                #! if this succeeds, then the value is already visited, so we ignore it
                #! of course, we create an exception for the initial node
                if indx == 0:
                    addNode = True
            except ValueError:
                #! if the exception is thrown, then the value was not visited, and we may add it
                addNode = True

            if addNode == True:
                newPos = adjVertex
                newVisitedArray = visitedArrayCopy.append(adjVertex)
                newWalkCost = state[2] + edgeCost
                successors.append((newPos, visitedArrayCopy, newWalkCost))

        return successors
    
    def getHeuristics(self):
        #! this heuristic simply returns the distance of the current vertex from the previous one
        #! in this way, greedy best first would visit the nearest neighbour every time
        #! in theory, this is not a very good heuristic
        def nearestNeighbor(state):
            current, visited, cost = state
            if len(visited) < 2:
                return 0
            else:
                prev = visited[-2] #! the second to last node
            
            prevAdjList = self.adjList[prev]
            #! find the edge cost, return it
            for i in prevAdjList:
                if i[0] == current:
                    return i[1]
            #! error case
            return float('inf')

        #! this is not useful, all nodes at the same depth will have the same value
        def remainingDistanceApproximate(state):
            visited = list(state[1])
            n = len(self.adjList)
            #! solution will have n+1 vertices
            return ((n+1) - len(visited)) * self.avgWeight


        return [remainingDistanceApproximate,nearestNeighbor]
