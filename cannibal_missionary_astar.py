"""
author: underscoreanuj
"""

from heapq import heappop, heappush, heapify
from random import shuffle



class State():
    def __init__(self, ml, cl, b, mr, cr, moves=0, parent=None):
        self.ml = ml
        self.cl = cl
        self.mr = mr
        self.cr = cr
        self.b = b
        moves = moves
        self.parent = parent

    def is_goal(self):
        return self.ml == 0 and self.cl == 0

    def is_valid(self):
        return (
            self.ml >= 0 and
            self.cl >= 0 and
            self.mr >= 0 and
            self.cr >= 0 and
            (self.ml == 0 or self.ml >= self.cl) and
            (self.mr == 0 or self.mr >= self.cr)
        )

    def possible_moves(self, moves):
        if self.b == 'l':
            obj = State(self.ml-2, self.cl, 'r', self.mr+2, self.cr, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml, self.cl-2, 'r', self.mr, self.cr+2, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml-1, self.cl-1, 'r', self.mr+1, self.cr+1, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml-1, self.cl, 'r', self.mr+1, self.cr, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml, self.cl-1, 'r', self.mr, self.cr+1, moves, self)
            if obj.is_valid():
                yield obj
        else:
            obj = State(self.ml+2, self.cl, 'l', self.mr-2, self.cr, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml, self.cl+2, 'l', self.mr, self.cr-2, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml+1, self.cl+1, 'l', self.mr-1, self.cr-1, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml+1, self.cl, 'l', self.mr-1, self.cr, moves, self)
            if obj.is_valid():
                yield obj
            obj = State(self.ml, self.cl+1, 'l', self.mr, self.cr-1, moves, self)
            if obj.is_valid():
                yield obj


    def score(self):
        return self.ml + self.cl
    
    def __cmp__(self, other):
        return (
            self.ml == other.ml and 
            self.cl == other.cl and 
            self.b == other.b and 
            self.mr == other.mr and 
            self.cr == other.cr
        )

    def __lt__(self, other):
        return self.score() < other.score()

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        return """
        {}\t{}\t{}\t{}\t{}
        """.format(self.ml, self.cl, self.b, self.mr, self.cr)


class PriorityQueue():
    def __init__(self):
        self.pq = []

    def add(self, item):
        heappush(self.pq, item)

    def poll(self):
        return heappop(self.pq)

    def seek(self):
        return self.pq[0]

    def remove(self, item):
        value = self.pq.remove(item)
        heapify(self.pq)
        
        return value is not None

    def empty(self):
        return self.__len__() <= 0

    def __len__(self):
        return len(self.pq)


class Solver():
    def __init__(self, ml, cl, b, mr, cr):
        self.initial_state = State(ml, cl, b, mr, cr)

    def rebuildPath(self, end):
        path = [end]
        state = end.parent
        while state:
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
            if current.is_goal():
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
            print("No solution found")


problem = Solver(3,3,'l',0,0)
problem.solve()
