# Kevin Koshy 
# b00098368
# Jerusha Paul
# g00100797
# Aly Mahmoud 
# b00101376
# Farah Jayas 
# g00100715

from AI_solve import *
from TravellingSalesmanProblem import *

#! this is the example from the HW
graph1 = [
    [(1, 20), (2, 42), (3, 35)],
    [(0, 20), (2, 30), (3, 34)],
    [(0, 42), (1, 30), (3, 12)],
    [(0, 35), (1, 34), (2, 12)]
]
tsp1 = TravellingSalesmanProblem(graph1, 0)

#! these examples are complete graphs of order 10, with random weights for the edges (generated via c++ script)
#! the weights were generated using the rand() function in cstdlib using the default seed
graph2 = [
    [(1, 41), (2, 67), (3, 34), (4, 0), (5, 69), (6, 24), (7, 78), (8, 58), (9, 62)],
    [(0, 64), (2, 5), (3, 45), (4, 81), (5, 27), (6, 61), (7, 91), (8, 95), (9, 42)],
    [(0, 27), (1, 36), (3, 91), (4, 4), (5, 2), (6, 53), (7, 92), (8, 82), (9, 21)],
    [(0, 16), (1, 18), (2, 95), (4, 47), (5, 26), (6, 71), (7, 38), (8, 69), (9, 12)],
    [(0, 67), (1, 99), (2, 35), (3, 94), (5, 3), (6, 11), (7, 22), (8, 33), (9, 73)],
    [(0, 64), (1, 41), (2, 11), (3, 53), (4, 68), (6, 47), (7, 44), (8, 62), (9, 57)],
    [(0, 37), (1, 59), (2, 23), (3, 41), (4, 29), (5, 78), (7, 16), (8, 35), (9, 90)],
    [(0, 42), (1, 88), (2, 6), (3, 40), (4, 42), (5, 64), (6, 48), (8, 46), (9, 5)],
    [(0, 90), (1, 29), (2, 70), (3, 50), (4, 6), (5, 1), (6, 93), (7, 48), (9, 29)],
    [(0, 23), (1, 84), (2, 54), (3, 56), (4, 40), (5, 66), (6, 76), (7, 31), (8, 8)]
]
graph3 = [
    [(1, 44), (2, 39), (3, 26), (4, 23), (5, 37), (6, 38), (7, 18), (8, 82), (9, 29)],
    [(0, 41), (2, 33), (3, 15), (4, 39), (5, 58), (6, 4), (7, 30), (8, 77), (9, 6)],
    [(0, 73), (1, 86), (3, 21), (4, 45), (5, 24), (6, 72), (7, 70), (8, 29), (9, 77)],
    [(0, 73), (1, 97), (2, 12), (4, 86), (5, 90), (6, 61), (7, 36), (8, 55), (9, 67)],
    [(0, 55), (1, 74), (2, 31), (3, 52), (5, 50), (6, 50), (7, 41), (8, 24), (9, 66)],
    [(0, 30), (1, 7), (2, 91), (3, 7), (4, 37), (6, 57), (7, 87), (8, 53), (9, 83)],
    [(0, 45), (1, 9), (2, 9), (3, 58), (4, 21), (5, 88), (7, 22), (8, 46), (9, 6)],
    [(0, 30), (1, 13), (2, 68), (3, 0), (4, 91), (5, 62), (6, 55), (8, 10), (9, 59)],
    [(0, 24), (1, 37), (2, 48), (3, 83), (4, 95), (5, 41), (6, 2), (7, 50), (9, 91)],
    [(0, 36), (1, 74), (2, 20), (3, 96), (4, 21), (5, 48), (6, 99), (7, 68), (8, 84)]
]
graph4 = [
    [(1, 81), (2, 34), (3, 53), (4, 99), (5, 18), (6, 38), (7, 0), (8, 88), (9, 27)],
    [(0, 67), (2, 28), (3, 93), (4, 48), (5, 83), (6, 7), (7, 21), (8, 10), (9, 17)],
    [(0, 13), (1, 14), (3, 9), (4, 16), (5, 35), (6, 51), (7, 0), (8, 49), (9, 19)],
    [(0, 56), (1, 98), (2, 3), (4, 24), (5, 8), (6, 44), (7, 9), (8, 89), (9, 2)],
    [(0, 95), (1, 85), (2, 93), (3, 43), (5, 23), (6, 87), (7, 14), (8, 3), (9, 48)],
    [(0, 0), (1, 58), (2, 18), (3, 80), (4, 96), (6, 98), (7, 81), (8, 89), (9, 98)],
    [(0, 9), (1, 57), (2, 72), (3, 22), (4, 38), (5, 92), (7, 38), (8, 79), (9, 90)],
    [(0, 57), (1, 58), (2, 91), (3, 15), (4, 88), (5, 56), (6, 11), (8, 2), (9, 34)],
    [(0, 72), (1, 55), (2, 28), (3, 46), (4, 62), (5, 86), (6, 75), (7, 33), (9, 69)],
    [(0, 42), (1, 44), (2, 16), (3, 81), (4, 98), (5, 22), (6, 51), (7, 21), (8, 99)]
]

tsp2 = TravellingSalesmanProblem(graph2, 0)
tsp3 = TravellingSalesmanProblem(graph3, 0)
tsp4 = TravellingSalesmanProblem(graph4, 0)

solve(tsp1, [depthFirstSearch, breadthFirstSearch, iterativeDeepeningSearch, uniformCostSearch, greedySearch, astarSearch])
print("\n\n\nSolving big example 1:")
solve(tsp2, [depthFirstSearch, breadthFirstSearch, iterativeDeepeningSearch, uniformCostSearch, greedySearch, astarSearch])
print("\n\n\nSolving big example 2:")
solve(tsp3, [depthFirstSearch, breadthFirstSearch, iterativeDeepeningSearch, uniformCostSearch, greedySearch, astarSearch])
print("\n\n\nSolving big example 3:")
solve(tsp4, [depthFirstSearch, breadthFirstSearch, iterativeDeepeningSearch, uniformCostSearch, greedySearch, astarSearch])

#solve(tsp2, [astarSearch])