"""
author: underscoreanuj
"""

import random


class TspProblem():
    def __init__(self, cityDistances):
        self.cityDistances = cityDistances
        self.numCities = len(cityDistances)
        self.tour = [x for x in range(self.numCities)]

    def getCost(self, tour):
        cost = 0
        for i in range(len(tour)-1):
            cost += self.cityDistances[tour[i]][tour[i+1]]
        cost += self.cityDistances[tour[-1]][tour[0]]

        return cost

    def randomizeTour(self, tour):
        tt = tour[1:]
        random.shuffle(tt)
        return [tour[0]] + tt

    def randomizeTourBySwap(self, tour):
        x = random.randint(1, len(tour)-1)
        y = random.randint(1, len(tour)-1)

        while x == y or y == min(x, y):
            x = random.randint(1, len(tour)-1)
            y = random.randint(1, len(tour)-1)

        tour = tour[0:x+1] + tour[y:x:-1] + tour[y+1:]

        return tour
    
    def HillClimb(self, max_evaluations=100, limit_range=None):
        best_sol = self.randomizeTour(self.tour)
        best_score = self.getCost(best_sol)

        num_evaluations = 0

        if limit_range is None:
            limit_range = len(self.tour)//2

        while num_evaluations < max_evaluations:
            move_made = False
            sols = []
            for i in range(limit_range):
                sols.append(self.randomizeTourBySwap(best_sol))
            
            for sol in sols:
                if num_evaluations >= max_evaluations:
                    break

                score = self.getCost(sol)
                num_evaluations += 1

                if score < best_score:
                    best_score = score
                    best_sol = sol
                    move_made = True
                    break

            if not move_made:
                break

        return num_evaluations, best_sol, best_score


cityDists = [[random.randint(1, 200) for _ in range(100)] for _ in range(100)]
problem = TspProblem(cityDists)

print(problem.HillClimb(2000))
                 