# Kevin Koshy 
# b00098368
# Jerusha Paul
# g00100797
# Aly Mahmoud 
# b00101376
# Farah Jayas 
# g00100715

from AI_solve import *
from AI_search import generalSearch, greedySearch, astarSearch, PriorityQueue
from SokobanPuzzleProblem import SokobanPuzzleProblem




easy_board = [
    "#######",
    "# .   #",
    "# # # #",
    "# # # #",
    "# $@  #",
    "#     #",
    "#######",
] # 12




moderate_board = [
    "  ####",
    "###  #",
    "#@ .$##",
    "#   $ #",
    "# #.  #",
    "#     #",
    "#######",
]  # 22
hard_board = [
    "     #####",
    "     #   ###",
    "  ####     ##",
    "###   #.##  ##",
    "#  $ $ $ $$@ #",
    "#  # ##.##   #",
    "## # # . #####",
    "#  # ...*.   #",
    "# $###   #   #",
    "# $   ###  ###",
    "#   #     ##",
    "###########",
]      # 32

algorithms = [greedySearch, astarSearch]
algo_names = ['greedySearch', 'astarSearch']

for board, name in [(easy_board,'#12 (Easy)'), (moderate_board,'#22 (Moderate)'), (hard_board,'#32 (Hard)')]:
    problem = SokobanPuzzleProblem(board)
    print("\nSokoban Puzzle")
    print(f"Puzzle: {name}")
    print("\nBoard:")
    print('\n'.join(board))



    #!#! call generalSearch directly so we control pruning type
    #!#! reuses solve()'s print_info by passing results manually

    def print_final_board(problem, state):
        player, boxes = state[0], state[1]
        # We use the walls and goals stored in the problem object
        for r in range(len(problem.board)):
            row_str = ""
            for c in range(len(problem.board[r])):
                pos = (r, c)
                if pos in problem.walls:
                    row_str += "#"
                elif pos == player:
                    row_str += "+" if pos in problem.goals else "@"
                elif pos in boxes:
                    row_str += "*" if pos in problem.goals else "$"
                elif pos in problem.goals:
                    row_str += "."
                else:
                    row_str += " "
            print(row_str)


    for i in range(len(algorithms)):
            for j in range(len(problem.getHeuristics())):
                heuristic = problem.getHeuristics()[j]
                print(f"\nAlgorithm: {algo_names[i]} ,  Heuristic: {heuristic.__name__}")
                solution = algorithms[i](problem, heuristic)
            if not solution:
                print("No solution found!")
            else:
                state, exp, gen = solution
                player, boxes, steps = state
                print(f"Solution path: {steps}")
                print(f"Cost: {len(steps)}")
                print(f"Nodes expanded: {exp}")
                print(f"Nodes generated: {gen}")
                print("\nFinal State Board:")
                print_final_board(problem, state)
            print("="*80)