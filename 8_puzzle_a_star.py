"""
author: underscoreanuj
"""

from heapq import heappush, heappop, heapify
from random import shuffle 



class State():
    def __init__(self, values, moves=0, parent=None):
        self.values = values
        self.moves = moves
        self.parent = parent
        self.goal = range(1, 9)

    def possible_moves(self, moves):
        i = self.values.index(0)
        if i in [3,4,5,6,7,8]:
            new_board = self.values[:]
            new_board[i], new_board[i-3] = new_board[i-3], new_board[i]
            yield State(new_board, moves, self)
        if i in [0,1,2,3,4,5]:
            new_board = self.values[:]
            new_board[i], new_board[i+3] = new_board[i+3], new_board[i]
            yield State(new_board, moves, self)
        if i in [0,1,3,4,6,7]:
            new_board = self.values[:]
            new_board[i], new_board[i+1] = new_board[i+1], new_board[i]
            yield State(new_board, moves, self)
        if i in [1,2,4,5,7,8]:
            new_board = self.values[:]
            new_board[i], new_board[i-1] = new_board[i-1], new_board[i]
            yield State(new_board, moves, self)

    def _h(self):
        return sum([1 if self.values[i] != self.goal[i] else 0 for i in range(8)])

    def _g(self):
        return self.moves

    def score(self):
        return self._h() + self._g()

    def __cmp__(self, other):
        return self.values == other.values

    def __hash__(self):
        return hash(str(self.values))

    def __lt__(self, other):
        return self.score() < other.score()

    def __str__(self):
        return """
        {}
        {}
        {}
        """.format(
            self.values[0:3], self.values[3:6],self.values[6:9]
        ).replace('[', '').replace(']', '').replace('0', 'x').replace(',', '\t')


class PriorityQueue():
    def __init__(self):
        self.pq = []

    def add(self, item):
        heappush(self.pq, item)
    
    def poll(self):
        return heappop(self.pq)

    def peek(self):
        return self.pq[0]

    def remove(self, item):
        value = self.pq.remove(item)
        heapify(self.pq)
        return value is not None

    def empty(self):
        return len(self.pq) <= 0

    def __len__(self):
        return len(self.pq)


class Solver():
    def __init__(self, initial_state=None):
        self.initial_state = State(initial_state)
        self.goal = range(1, 9)

    def rebuildPath(self, end):
        path = [end]
        state = end.parent
        while state is not None:
            path.append(state)
            state = state.parent
        
        return path

    def solve(self):
        openset = PriorityQueue()
        openset.add(self.initial_state)
        closed = set()
        moves = 0
        print(self.initial_state)
        print('\nSolution:\n')
        while not openset.empty():
            current = openset.poll()
            flag = all([True if current.values[i] == self.goal[i] else False for i in range(8)])
            if flag:
                path = self.rebuildPath(current)
                for state in reversed(path):
                    print(state)
                return
            moves += 1
            for state in current.possible_moves(moves):
                if state not in closed:
                    openset.add(state)
            closed.add(current)
        else:
            print("no solution found!!!")



puzzle = [
    4, 1, 3,
    0, 2, 5,
    7, 8, 6
]
# shuffle(puzzle)
print(puzzle)
problem = Solver(puzzle)
problem.solve()
