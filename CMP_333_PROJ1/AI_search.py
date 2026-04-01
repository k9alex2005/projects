##############################################################################
###
###   CMP 333 PROJECT 1 -- SEARCH
###
###   AI SEARCH ALGORITHMS AND SUPPORTING DATA STRUCTURES for the frontier
###   General Search and BFS, DFS, IDA, UFS, A*, and Greedy search;
###   Stack, Queue, and Priority Queue.
###
###   Michel Pasquier 2019, adapted from the code @
###   https://kartikkukreja.wordpress.com/2015/06/14/heuristics-in-ai-search/
###


# Kevin Koshy 
# b00098368
# Jerusha Paul
# g00100797
# Aly Mahmoud 
# b00101376
# Farah Jayas 
# g00100715

from TravellingSalesmanProblem import TravellingSalesmanProblem
from SokobanPuzzleProblem import SokobanPuzzleProblem


class Stack:
    def __init__(self): self.items = []

    def push(self, item): self.items.append(item)

    def pop(self): return self.items.pop()

    def empty(self): return not self.items

from collections import deque
class Queue:
    def __init__(self): self.items = deque()

    def push(self, item): self.items.append(item)

    def pop(self): return self.items.popleft()

    def empty(self): return not self.items

import heapq
class PriorityQueue:
    def __init__(self, priorityFunction):
        self.priorityFunction = priorityFunction
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, (self.priorityFunction(item), item))

    def pop(self):
        (_, item) = heapq.heappop(self.heap)
        return item

    def empty(self): return not self.heap


#!#! modifying the general search to include pruning for 8 puzzle
def generalSearch(problem, strategy, pruning='None'):
    
    #!#! for the travelling salesman problem, due to states being unique, pruning not 
    #!#! applicable
   
    
    if (isinstance(problem,TravellingSalesmanProblem)):
        pruning = "None"
    else:
        print("Select pruning method (None, Parent, Ancestor, Full): ")
        pruning = input().strip().capitalize()
    
        


    
    num_nodes_exp = 0
    num_nodes_gen = 1
    strategy.push(problem.getStartState())
    
    
    #!#! pruning implementation different based on problem
    #!#! generalsearch for sokoban
    if (isinstance(problem,SokobanPuzzleProblem)):
        
        visited = set() # For Full Pruning


    # Ancestor puning - we track the states leader to the current state 
    # using a disctionary to store: {child state: parent state} this lets us climb ip the family tree to check ancestors

        parents = {} 

        while not strategy.empty():
            node = strategy.pop()
            # node[0] is player (r,c), node[1] is boxes frozenset
            state_key = (node[0], node[1]) 

            if problem.isGoalState(node):
                return (node, num_nodes_exp, num_nodes_gen)

            num_nodes_exp += 1

            for move in problem.getSuccessors(node):
                successor_key = (move[0], move[1])
                skip_node = False # We assume we want the move unless pruning says no

                # --- PRUNING LOGIC ---
                if pruning == 'Parent':
                    # Check if this move leads back to the state that generated 'node'
                    if state_key in parents and successor_key == parents[state_key]:
                        skip_node = True
                
                elif pruning == 'Ancestor':
                    # Climb the family tree
                    check_parent = state_key
                    while check_parent in parents:
                        if successor_key == check_parent:
                            skip_node = True
                            break
                        check_parent = parents[check_parent]
                    
                elif pruning == 'Full':
                    if successor_key in visited:
                        skip_node = True
                    else:
                        visited.add(successor_key)

                # --- THE CRITICAL PART ---
                if not skip_node:
                    # Record parentage for Parent and Ancestor tracking
                    if successor_key not in parents: 
                        parents[successor_key] = state_key
                    
                    strategy.push(move)
                    num_nodes_gen += 1

        return None
           
       
    
    #!#! for the 8 puzzle and tsp
    else:
    
        #!#! global list to contain visited states for full pruning    
        best_g = {}  
        #!#! function to check if a generated node is an ancestor
        def isAncestor(node, move_grid):
            pos0 = node[1]
            node_grid = node[0].copy()
            for action in node[-1][::-1]:
                if (action == 'D'):
                    node_grid[pos0], node_grid[pos0 - 3] = node_grid[pos0 - 3], node_grid[pos0]
                    pos0 -= 3
                    if (node_grid == move_grid):
                        return True
                elif (action == 'U'):
                    node_grid[pos0], node_grid[pos0 + 3] = node_grid[pos0 + 3], node_grid[pos0]
                    pos0 += 3
                    if (node_grid == move_grid):
                        return True
                elif (action == 'L'):
                    node_grid[pos0], node_grid[pos0 + 1] = node_grid[pos0 + 1], node_grid[pos0]
                    pos0 += 1
                    if (node_grid == move_grid):
                        return True
                    
                elif (action == 'R'):
                    node_grid[pos0], node_grid[pos0 - 1] = node_grid[pos0 - 1], node_grid[pos0]
                    pos0 -=1
                    if (node_grid == move_grid):
                        return True
            return False
        
         
        
    
        while not strategy.empty():
        
            num_nodes_exp += 1
            #> uncomment below to print the priority queue at each iteration
            #print(strategy.heap)
            node = strategy.pop()
            
            #> uncomment below to print the node being expanded
            #print(node)
            
            
            if problem.isGoalState(node):
                return (node, num_nodes_exp, num_nodes_gen)


            #!#! for parent pruning prevent generation of states we just came from
            if (pruning == 'Parent'):
                #!#! determine parent of the current node
                #!#! generate children of current node
                #!#! ignore pushing child states that are equal to parent states
                # parent_node_grid = getParent(node)
                for move in problem.getSuccessors(node):
                    
                #!#! Parent pruning: prevent generating child states that correspond
                #!#! to immediately reversing the last action (i.e., avoid
                #!#! returning to the parent state).
        
                    if (node == problem.getStartState()):
                        strategy.push(move)
                        num_nodes_gen += 1
                        continue
                    last_action = node[-1][-1]
                    if (last_action == 'D'):
                        if move[-1][-1] != 'U':
                            strategy.push(move)
                            num_nodes_gen += 1
                    elif (last_action == 'L'):
                        if move[-1][-1] != 'R':
                            strategy.push(move)
                            num_nodes_gen += 1
                    elif (last_action == 'R'):
                        if move[-1][-1] != 'L':
                            strategy.push(move)
                            num_nodes_gen += 1
                    elif (last_action == 'U'):
                        if move[-1][-1] != 'D':
                            strategy.push(move)
                            num_nodes_gen += 1
                    
                    
                    
                    
                    
            elif (pruning == 'Ancestor'):
                  
            
                    #!#! for ancestor pruning, when we generate a node
                    #!#! we attempt to generate ancestor nodes by applying complement of actions
                    #!#! starting from the last action. If any grid that we generate matches 
                    #!#! with an ancestor grid we avoid expanding that node.
                    
                    #!#! here we are also assuming we are allowed to only modify general 
                    #!#! search
                    
                    for move in problem.getSuccessors(node):
                        if (node == problem.getStartState()):
                            strategy.push(move)
                            num_nodes_gen += 1
                            continue
                    
                        if (isAncestor(node,move[0])):
                            continue
                        strategy.push(move)
                        num_nodes_gen += 1
            
        
        

        
                    
            elif (pruning == "Full"):
                #!#! full pruning
                #!#! before pushing a node, we check if state is visited and 
                #!#! cost to reach state is more than previous paths then 
                #!#! we prune it
                    for move in problem.getSuccessors(node):

                        grid = tuple(move[0])
                        g_cost = len(move[-1])  # steps from start
                        if grid not in best_g or g_cost < best_g[grid]:
                            best_g[grid] = g_cost
                            strategy.push(move)
                            num_nodes_gen += 1
            else:
                for move in problem.getSuccessors(node):
                    strategy.push(move)
                    num_nodes_gen += 1
                #> uncomment to print num of nodes generated after each node expansion
                #print(num_nodes_gen)
        return None

def breadthFirstSearch(problem): return generalSearch(problem, Queue())

def depthFirstSearch(problem): return generalSearch(problem, Stack())

def iterativeDeepeningSearch(problem):
    num_nodes_exp = 0
    num_nodes_gen = 1
   
    def depthLimitedDFS(problem, state, depth):
        nonlocal num_nodes_gen, num_nodes_exp
        num_nodes_exp += 1
        if problem.isGoalState(state): return state
        if depth <= 0: return None
        for move in problem.getSuccessors(state):
            num_nodes_gen += 1
            solution = depthLimitedDFS(problem, move, depth-1)
            if solution is not None: return solution
        return None

    depth = 1
    while True:
        
        solution = depthLimitedDFS(problem, problem.getStartState(), depth)
        
        if solution is not None:
            return (solution, num_nodes_exp, num_nodes_gen)
        depth += 1

def uniformCostSearch(problem):
    #! added this if statement since the cost is stored explicitly for the TSP
    if isinstance(problem, TravellingSalesmanProblem):
        return generalSearch(problem, PriorityQueue(lambda state: state[2]))
   
    else:
        return generalSearch(problem, PriorityQueue(lambda state: (sum(state[3]) if len(state) > 3 else len(state[-1]))))

def greedySearch(problem, heuristic):
    return generalSearch(problem, PriorityQueue(heuristic))

def astarSearch(problem, heuristic):
    # the given function uses the number of steps as g-cost (uniform cost)
    # the number of elements in a state changes for different problems, hence
    # the following checks
    
    #! added this if statement since the cost is stored explicitly for the TSP
    if isinstance(problem, TravellingSalesmanProblem):
        totalCost = lambda state: state[2] + heuristic(state, problem.adjList)
        return generalSearch(problem, PriorityQueue(lambda state: state[2]))
    
    else:
        totalCost = lambda state: (sum(state[3]) if len(state) > 3 else len(state[-1])) + heuristic(state)
        return generalSearch(problem, PriorityQueue(totalCost))


###