##############################################################################
###
###   CMP 333 PROJECT 1 -- SEARCH
###
###   SOLVE FUNCTION used to solve various AI search problems
###
###   Michel Pasquier 2019, to be adapted/expanded as necessary
###

# Kevin Koshy 
# b00098368
# Jerusha Paul
# g00100797
# Aly Mahmoud 
# b00101376
# Farah Jayas 
# g00100715


from AI_search import generalSearch, breadthFirstSearch, depthFirstSearch, \
    iterativeDeepeningSearch, uniformCostSearch, greedySearch,astarSearch, \
    Stack, Queue, PriorityQueue
from EightPuzzleProblem import EightPuzzleProblem
from PacmanProblem import PacmanProblem
from TravellingSalesmanProblem import TravellingSalesmanProblem
from SokobanPuzzleProblem import SokobanPuzzleProblem  
#!#! added imports for tsp and sokoban problems








def solve(problem, search_algorithms):
    

    def print_info(solution):
       
       
        if not solution:
            print("No solution!")
            return
        state, num_nodes_exp, num_nodes_gen = solution
        if isinstance(problem, EightPuzzleProblem):
            
            
            finalstate,_,steps = state
            cost = len(steps)
            
        
        elif isinstance(problem, TravellingSalesmanProblem):
            finalstate, steps, cost = state
        elif isinstance(problem, SokobanPuzzleProblem):  #! added Sokoban case
            finalstate, boxes, steps = state 
        else:
            finalstate, steps = state
            cost = len(steps)
        
        print(f"Final state: {finalstate}")
        
        
            
            
            
       
        
        

        print(f"Solution: {steps}")
        
        print(f"Cost: {cost}")
        print(f"Number of nodes expanded: {num_nodes_exp}")
        print(f"Number of nodes generated: {num_nodes_gen}")
        print("="*80+"\n")

    print(problem.__class__.__name__)

    for algo in search_algorithms:
        if algo.__name__ in ["greedySearch", "astarSearch"]: # heuristic search
            for heuristic in problem.getHeuristics():
              print(f"Algorithm used: {algo.__name__}")
              print(f"Heuristic used: {heuristic.__name__}")
              solution = algo(problem, heuristic)
              print_info(solution)
        else:
            print(f"Algorithm used: {algo.__name__}")
            solution = algo(problem)
            print_info(solution)


#!#!Commented out sample 8 puzzle and pac-man problems

# puzzle = [1,8,0,
#           4,3,2,
#           5,7,6]
# solve(EightPuzzleProblem(puzzle), [breadthFirstSearch, uniformCostSearch, astarSearch])

#  pacmap = ["P---------",
#           "%%-%%-%-%%",
#           "---%--%---",
#           "-%%%-%%%-%",
#           "---%%%-.-%",
#           "-%------%%"]

# solve(PacmanProblem(pacmap, (0,0), (4,7)), [breadthFirstSearch,greedySearch,astarSearch])



###