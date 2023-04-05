from search import SearchAlgorithm

class DepthFirstIdSearch(SearchAlgorithm):
    def __init__(self, problem, depth = 1):
        super().__init__(problem)
        self.frontier = []
        self.backrefs = {}
        self.frontier.append((self.startState, 0))
        self.current_depth = depth;
    
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
        backrefs = self.backrefs

        if self.actions:
            return self.path(problem.endState())
        elif len(frontier) == 0:
            
            self.__init__(problem, self.current_depth + 1)
        #    self.current_depth += 1
        #    print('depth: ', self.current_depth)
        #    frontier.append((problem.startState(), 0))
        #    state = self.startState
        #    self.backrefs = {}
        #    self.pastCosts = {}
        #    self.numStatesExplored = 0
        #    pastCost = 0

        if len(frontier) > 0:
            state, pastCost = frontier.pop()
        else:
            return []
        
        self.pastCosts[state] = pastCost
        self.numStatesExplored += 1
        path = self.path(state)

        if problem.isEnd(state):
            self.actions = []
            while state != startState:
                action, prevState = backrefs[state]
                self.actions.append(action)
                state = prevState
            self.actions.reverse()
            self.pathCost = pastCost
            return path

        for action, newState, cost in problem.successorsAndCosts(state):
            if len(path) < self.current_depth and newState not in self.pastCosts:
                self.frontier.append((newState, cost))
                self.pastCosts[newState] = self.pastCosts[state] + cost
                backrefs[newState] = (action, state)
        return path
