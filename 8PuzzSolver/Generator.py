import random as rn
import numpy as np


# Generates start and goal states for puzzle of given size, they can be unsolvable
class Generator:
    def __init__(self, rows_am=3, cols_am=3):
        self.rows_am = rows_am
        self.cols_am = cols_am

    def generate_puzzle(self):
        rn.seed()
        start_state = np.arange(self.rows_am * self.cols_am).reshape(self.rows_am, self.cols_am)
        goal_state = np.arange(self.rows_am * self.cols_am).reshape(self.rows_am, self.cols_am)
        seq = rn.sample(range(0, self.rows_am * self.cols_am), self.rows_am * self.cols_am)
        for i in range(0, self.rows_am):
            for j in range(0, self.cols_am):
                start_state[i, j] = int(seq[i * self.cols_am + j])
        seq = rn.sample(seq, len(seq))
        for i in range(0, self.rows_am):
            for j in range(0, self.cols_am):
                goal_state[i, j] = int(seq[i * self.cols_am + j])
        return start_state, goal_state
