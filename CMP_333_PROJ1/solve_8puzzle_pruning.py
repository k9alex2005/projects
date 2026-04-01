# Kevin Koshy 
# b00098368
# Jerusha Paul
# g00100797
# Aly Mahmoud 
# b00101376
# Farah Jayas 
# g00100715



from AI_solve import *

#2 8-puzzle problems

puzzle1 = [1,3,8,
          4,0,2,
          5,7,6]

puzzle2 = [1,5,8,
           7,2,0,
           3,4,6]




grid = [[[1,2,3],[3,4,4],[1,2,3]],[[3,4,5],[2,1,2],[1,2,1]]]
for row in range(3):
    for grids in grid:
        print()

print("------Solving puzzle 1----")
for i in range(9):
    if (i % 3 == 2):
        print(puzzle1[i])
    else:
        print(puzzle1[i], end=" ")
solve(EightPuzzleProblem(puzzle1), [astarSearch,breadthFirstSearch,greedySearch,uniformCostSearch])

print("------Solving puzzle 2----")
for i in range(9):
    if (i % 3 == 2):
        print(puzzle2[i])
    else:
        print(puzzle2[i], end=" ")
solve(EightPuzzleProblem(puzzle2), [astarSearch,breadthFirstSearch,greedySearch,uniformCostSearch])




