from search import SearchAlgorithm
from pq import PriorityQueue
import math

def h_euclidean(x, endState):
    return math.dist(x, endState)

class AStarSearch(SearchAlgorithm):
    def __init__(self, problem):

        #This is the heuristic election
        self.heuristic = lambda x : h_euclidean(x, problem.endState())

        super().__init__(problem)
        self.frontier = PriorityQueue()
        self.backrefs = {}
        self.frontier.update(self.startState, 0.0)
        self.finished = False
        self.gScores = {self.startState : 0.0}
        self.fScores = {}
        self.fScores[self.startState] = self.heuristic(self.startState) 

    def stateCost(self, state):
        return self.fScores.get(state, None)

    def path(self, state):
        path = []
        while state != self.problem.startState():
            _, prevState = self.backrefs[state]
            path.append(state)
            state = prevState
        path.reverse()
        return path

    def step(self):
        problem = self.problem
        startState = self.startState
        frontier = self.frontier
        backrefs = self.backrefs
        gScores = self.gScores
        fScores = self.fScores

        if self.finished:
            return self.path(problem.endState())

        state, fScore = frontier.removeMin()
        if state is None and fScore is None:
            return []

        self.fScores[state] = fScore
        self.numStatesExplored += 1
        path = self.path(state)

        if problem.isEnd(state):
            self.pathCost = fScore
            self.finished = True
            return path

        for action, newState, cost in problem.successorsAndCosts(state):
            tentativeGScore = gScores[state] + cost 
            if gScores.get(newState, float('+inf'))  > tentativeGScore:
                backrefs[newState] = (action, state)
                gScores[newState] = tentativeGScore
                fScores[newState] = tentativeGScore + self.heuristic(newState)
                frontier.update(newState, fScores[newState])

        return path


