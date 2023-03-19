from Solver import Solver
from timeit import default_timer as timer
import numpy as np
from Generator import Generator
import random as rn


# Take input for one puzzle from the console
def load_input():
    m, n = input("Input size of the puzzle (#rows #columns):\n").split(" ", 1)
    m = int(m)
    n = int(n)
    start_state = np.arange(m * n, dtype=np.uint8).reshape(m, n)
    goal_state = np.arange(m * n, dtype=np.uint8).reshape(m, n)
    print("Input start state (seperate with spaces, one row = one line):")
    for i in range(0, int(m)):
        for j, num in enumerate(input().split(" ")):
            start_state[i, j] = int(num)
    print("Input goal state (seperate with spaces, one row = one line):")
    for i in range(0, int(m)):
        for j, num in enumerate(input().split(" ")):
            goal_state[i, j] = int(num)
    return m, n, start_state, goal_state


# Load puzzle from prepared file, loads the puzzle with the given index number
def from_file(index):
    with open("puzzle_examples.txt", 'r') as f:
        if index == 'r':
            amount = int(f.readline().split()[0])
            rn.seed()
            index = rn.randint(1, amount)
        else:
            index = int(index)
        for line in f:
            for word in line.split():
                if word == str(index) + '.':
                    m, n = f.readline().split(" ", 1)
                    m = int(m)
                    n = int(n)
                    start_state = np.arange(m * n, dtype=np.uint8).reshape(m, n)
                    goal_state = np.arange(m * n, dtype=np.uint8).reshape(m, n)
                    f.readline()
                    for i in range(0, int(m)):
                        for j, num in enumerate(f.readline().split(" ")):
                            start_state[i, j] = int(num)
                    f.readline()
                    for i in range(0, int(m)):
                        for j, num in enumerate(f.readline().split(" ")):
                            goal_state[i, j] = int(num)
                    return m, n, start_state, goal_state


# Instead of moving the blank we move the tiles
def translate_operator(op):
    if op == 'r':
        return 'LEFT'
    elif op == 'l':
        return 'RIGHT'
    elif op == 'u':
        return 'DOWN'
    elif op == 'd':
        return 'UP'


def output_state(state):
    for row in state:
        print(' '.join(str(i) for i in row))


# Print path from start to finish with operators and states
def output_path(path):
    for step in path:
        if step[1] is not None:
            print(translate_operator(step[1]))
        else:
            print("START")
        output_state(step[0])


# Solve given puzzle, using given heuristic option (1 or 2) and output the outcome
def solve_puzzle(rows_am, cols_am, start_state, goal_state, hf=2):
    print("\nSTART STATE:")
    output_state(start_state)
    print("\nGOAL STATE:")
    output_state(goal_state)
    start = timer()
    solver = Solver(goal_state, rows_am, cols_am)
    path = solver.solve(start_state, hf)
    end = timer()
    if path:
        print("Duration: " + str(end - start) + " seconds")
        output_path(path)


# Asks the user to specify puzzle characteristics and input type
def create_puzzle():
    try:
        while 1:
            choice = input("Choose how to create a puzzle (a - to input states, g - to generate randomly, "
                           "f - load from file) or put in 'q' to quit:\n")
            if choice == 'a':
                rows_am, cols_am, start_state, goal_state = load_input()
                hf = int(input("Which heuristic should be used (1 - first, 2 - second):\n"))
                solve_puzzle(rows_am, cols_am, start_state, goal_state, hf)
            elif choice == 'g':
                rows_am, cols_am = input("Input size of the puzzle (#rows #columns):\n").split(" ", 1)
                rows_am = int(rows_am)
                cols_am = int(cols_am)
                gen = Generator(rows_am, cols_am)
                puzzle_am = int(input("How many puzzles should be generated:\n"))
                hf = int(input("Which heuristic should be used (1 - first, 2 - second):\n"))
                for i in range(0, puzzle_am):
                    start_state, goal_state = gen.generate_puzzle()
                    solve_puzzle(rows_am, cols_am, start_state, goal_state, hf)
            elif choice == 'f':
                index = input("Which puzzle do you want to load (input index number or 'r' for random):\n")
                rows_am, cols_am, start_state, goal_state = from_file(index)
                hf = int(input("Which heuristic should be used (1 - first, 2 - second):\n"))
                solve_puzzle(rows_am, cols_am, start_state, goal_state, hf)
            elif choice == 'q':
                return
            else:
                print("Please input 'a' or 'g' or 'f' or 'q'!\n")
    except ValueError:
        print("Wrong input!")


create_puzzle()
