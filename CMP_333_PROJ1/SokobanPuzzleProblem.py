from AI_problem import SearchProblem

class SokobanPuzzleProblem(SearchProblem):

    def __init__(self, board):
        # this is constructor, it runs when we create a SokobanPuzzleProblem(board) object
        # board is the list of strings

        self.board = board  # saves the board for later use
        self.goals = set()  # stores all . storage positions
        self.start_boxes = set()  # stores all the $ box positions
        self.start_player = None  # to save the @ player position
        self.walls = set()  # stores all # wall positions

        # we iterate through every row and column of the board
        for r in range(len(board)):
            for c in range(len(board[r])):
                index_value = board[r][c]

                # if we find the player, save position
                if index_value == '@':
                    self.start_player = (r, c)

                # if we find a box
                if index_value == '$':
                    self.start_boxes.add((r, c))

                # goal position
                if index_value == '.':
                    self.goals.add((r, c))

                # wall position
                if index_value == '#':
                    self.walls.add((r, c))

                # box already on goal
                if index_value == '*':
                    self.start_boxes.add((r, c))
                    self.goals.add((r, c))

                # player on goal
                if index_value == '+':
                    self.start_player = (r, c)
                    self.goals.add((r, c))

        # converting to frozenset so they don't change
        self.goals = frozenset(self.goals)
        self.start_boxes = frozenset(self.start_boxes)
        self.walls = frozenset(self.walls)

        # checking corner positions in advance to prevent boxes from being pushed into them

        # this set will store positions that are empty corners meaning if a box is pushed there, it will get stuck forever
        self.corners = set()

        for r in range(len(board)):
            for c in range(len(board[r])):

                pos = (r, c)

                # only check spaces that are not walls and not goals because goals are allowed places for boxes
                if pos not in self.walls and pos not in self.goals:

                    # check if walls exist around this cell
                    wall_up = (r - 1, c) in self.walls
                    wall_down = (r + 1, c) in self.walls
                    wall_left = (r, c - 1) in self.walls
                    wall_right = (r, c + 1) in self.walls

                    # if there is a wall vertically AND horizontally,
                    # this means the position is a corner
                    # if a box goes into X, it gets stuck forever
                    if (wall_up or wall_down) and (wall_left or wall_right):
                        self.corners.add(pos)


    #returns what we saved in init, where the player starts, where the boxes start, and the path
    def getStartState(self):
        return (self.start_player, self.start_boxes, [])


    def isGoalState(self, state):

        player, boxes, path = state

        for box in boxes:
            if box not in self.goals:
                return False

        return True


    # generate possible moves
    def getSuccessors(self, state):

        player, boxes, path = state
        moves_list = []

        #  all 4 directions
        direction_name = ['U', 'D', 'L', 'R']
        direction_row = [-1, 1, 0, 0]
        direction_cols = [0, 0, -1, 1]

        for i in range(4):

            move_name = direction_name[i]
            dr = direction_row[i]
            dc = direction_cols[i]

            new_row = player[0] + dr
            new_col = player[1] + dc

            # cannot move into wall
            if (new_row, new_col) in self.walls:
                continue

            new_boxes = set(boxes)

            # if player hits a box
            if (new_row, new_col) in boxes:

                box_r = new_row + dr
                box_c = new_col + dc

                # cannot push into wall
                if (box_r, box_c) in self.walls:
                    continue

                # cannot push into another box
                if (box_r, box_c) in boxes:
                    continue

                # if box is pushed into a corner that is NOT goal,
                # we skip this move because it will fail later
                if (box_r, box_c) in self.corners:
                    continue

                new_boxes.remove((new_row, new_col))
                new_boxes.add((box_r, box_c))

            moves_list.append(
                (
                    (new_row, new_col),
                    frozenset(new_boxes),
                    path + [move_name]
                )
            )

        return moves_list


    # each move costs 1
    def getCostOfAction(self, state, action):
        return 1


    def getHeuristics(self):

        def optimalMatchingPlayerDist(state):

            player, boxes, path = state

            if not boxes:
                return 0

            # OPTIMAL MATCHING
            # We pair each box with a unique goal to avoid double-counting goals

            total_box_dist = 0
            unmatched_goals = list(self.goals)

            # to Sort boxes by distance to any goal to process constrained boxes first
            sorted_boxes = sorted(
                list(boxes),
                key=lambda b: min(
                    abs(b[0] - g[0]) +
                    abs(b[1] - g[1])
                    for g in self.goals
                )
            )

            for box in sorted_boxes:

                if not unmatched_goals:
                    break

                # Finds the closest goal among those not yet taken by another box
                dist, best_goal = min(
                    (
                        abs(box[0] - g[0]) +
                        abs(box[1] - g[1]),
                        g
                    )
                    for g in unmatched_goals
                )

                total_box_dist += dist
                unmatched_goals.remove(best_goal)

            # PLAYER DISTANCE
            # Finds the distance from the player to the nearest box

            player_to_box_dist = min(
                abs(player[0] - b[0]) +
                abs(player[1] - b[1])
                for b in boxes
            )
            # We subtract 1 because the player stands next to the box to push it

            return total_box_dist + (player_to_box_dist - 1)

        return [optimalMatchingPlayerDist]
    
        #  Manhattan to Nearest Goal
        
        # def manhattanToNearestGoal(state):
        #
        #     player, boxes, path = state
        #
        #     total = 0
        #
        #     # for each box, find nearest goal
        #     for box in boxes:
        #
        #         # if box already on goal, skip it
        #         if box in self.goals:
        #             continue
        #
        #         # find closest goal using Manhattan distance
        #         nearest = min(
        #             abs(box[0] - g[0]) +
        #             abs(box[1] - g[1])
        #             for g in self.goals
        #         )
        #
        #         total += nearest
        #
        #     return total
        #
        # return [manhattanToNearestGoal]

        # Manhattan + Player Distance
       
        # def manhattanPlusPlayer(state):
        #
        #     player, boxes, path = state
        #
        #     if not boxes:
        #         return 0
        #
        #     total_box_dist = 0
        #
        #     # distance from each box to nearest goal
        #     for box in boxes:
        #
        #         nearest = min(
        #             abs(box[0] - g[0]) +
        #             abs(box[1] - g[1])
        #             for g in self.goals
        #         )
        #
        #         total_box_dist += nearest
        #
        #     # distance from player to nearest box
        #     player_to_box_dist = min(
        #         abs(player[0] - b[0]) +
        #         abs(player[1] - b[1])
        #         for b in boxes
        #     )
        #
        #     return total_box_dist + (player_to_box_dist - 1)
        #
        # return [manhattanPlusPlayer]