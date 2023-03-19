from heapq import *
from Node import *
import numpy as np


# Used to determine solvability of a puzzle
def count_inversions(state):
    array = state.flatten()
    invers_am = 0
    for i, num in enumerate(array[:-1]):
        if num != 1 and num != 0:
            for j in array[i + 1:]:
                if j != 0 and num > j:
                    invers_am += 1
    return invers_am


class Solver:
    def __init__(self, goal_state, rows_am, cols_am):
        self.goal_state = goal_state
        self.rows_am = rows_am
        self.cols_am = cols_am
        self.goal_coord = {}

    # Uses a set of conditions to determine whether the puzzle is solvable
    def is_solvable(self, start_state):
        if self.cols_am & 1:
            if (count_inversions(start_state) & 1) == (count_inversions(self.goal_state) & 1):
                return True
        else:
            mover_y = find_mover(start_state)[0]
            star_mover = (self.rows_am - mover_y) & 1
            mover_y = find_mover(self.goal_state)[0]
            goal_mover = (self.rows_am - mover_y) & 1
            if (((count_inversions(start_state) & 1) == star_mover) ==
                    ((count_inversions(self.goal_state) & 1) == goal_mover)):
                return True
        return False

    # Creates a dictionary of numbers in the goal state and their coordinates
    # to be used by the second heuristic function to calculate the distances
    def set_goal_cord(self):
        for y, row in enumerate(self.goal_state):
            for x, num in enumerate(row):
                if num != 0:
                    self.goal_coord[num] = (y, x)

    # First heuristic function, returns amount of misplaced numbers
    def get_hvalue1(self, node_state):
        hvalue = 0
        for i, row in enumerate(node_state):
            for j, num in enumerate(row):
                if num != 0 and num != self.goal_state[i][j]:
                    hvalue += 1
        return hvalue

    # Second heuristic function, returns the sum of distances of number positions from their goal positions.
    def get_hvalue2(self, node_state):
        hvalue = 0
        for i, row_node in enumerate(node_state):
            for j, num in enumerate(row_node):
                if num != 0:
                    hvalue += abs(i - self.goal_coord[num][0]) + abs(j - self.goal_coord[num][1])
        return hvalue

    # Main algorithm for going through nodes
    # Every state is saved as to not create duplicate states - for this we use a set
    # and the arrays that represent states have to be converted to strings to be hashable
    def a_star(self, start_state, h_function):
        heap = []
        generated_count = 0
        opened_count = 0
        max_depth = 0
        start_node = Node(start_state, None, None)
        start_node.value = h_function(start_state)
        generated_states = {start_node.state.copy().tostring()}
        heappush(heap, start_node)
        while not np.array_equal(heap[0].state, self.goal_state):
            opened_count += 1
            new_children = heappop(heap).make_children(self.rows_am, self.cols_am)
            for child in new_children:
                if child.state.copy().tostring() not in generated_states:
                    generated_states.add(child.state.copy().tostring())
                    child.value = h_function(child.state) + child.depth
                    generated_count += 1
                    max_depth = max(max_depth, child.depth)
                    heappush(heap, child)
        print(' '.join(["Depth:", str(max_depth), "Generated nodes:",
                        str(generated_count), "Opened nodes:", str(opened_count)]))
        return heappop(heap)

    # If the puzzle is solvable, returns path from start to goal with operators and states along the way
    # returns a tuple (state, operator)
    def solve(self, start_state, h_function=2):
        if not self.is_solvable(start_state):
            print("Solution doesn't exist")
            return False
        if h_function == 1:
            hf = self.get_hvalue1
        else:
            self.set_goal_cord()
            hf = self.get_hvalue2
        last_node = self.a_star(start_state, hf)
        path = []
        while last_node is not None:
            path.append((last_node.state, last_node.op))
            last_node = last_node.parent
        path.reverse()
        return path
