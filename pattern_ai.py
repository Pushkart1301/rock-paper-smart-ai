from collections import defaultdict
import random

class PatternAI:
    def __init__(self):
        self.transition = defaultdict(lambda: defaultdict(int))
        self.last_move = None

    def update(self, current_move):
        if self.last_move is not None:
            self.transition[self.last_move][current_move] += 1
        self.last_move = current_move

    def predict(self):
        if self.last_move is None:
            return random.choice(['rock', 'paper', 'scissors'])

        next_moves = self.transition[self.last_move]
        if not next_moves:
            return random.choice(['rock', 'paper', 'scissors'])

        return max(next_moves, key=next_moves.get)
