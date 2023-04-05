from search import SearchAlgorithm;

NegativeCostExists = False

class Backtracking(SearchAlgorithm):
    def __init__(self, problem):
        super().__init__(problem)
        self.frontier = []
        self.frontier.append((self.startState, 0, []))
        self.best_cost = float('+inf')
        self.best_path = None
        self.current_path = []
        self.pastCosts = {}

    def stateCost(self, state):
        return self.pastCosts.get(state, None)
    
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

        if len(frontier) == 0:
            return self.best_path

        if frontier: 
            state, currentStateCost, path = frontier.pop() 
        else:
            return []
        
        self.numStatesExplored += 1
        self.pastCosts[state] = currentStateCost
        path.append(state)


        if problem.isEnd(state):
            if currentStateCost < self.best_cost:
                self.best_cost = currentStateCost
                self.best_path = path

            return path

        next_state = []
        for action, newState, cost in problem.successorsAndCosts(state):
            if newState not in self.pastCosts \
                or self.pastCosts[newState] > currentStateCost + cost:
                if currentStateCost + cost < self.best_cost or \
                    NegativeCostExists:
                    next_state.append((newState, 
                        currentStateCost + cost, path.copy()))

        next_state.reverse()
        frontier.extend(next_state)
        return path
