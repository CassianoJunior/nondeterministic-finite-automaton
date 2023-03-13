class NFA:
  def __init__(self, statesSet, alphabet, transitionFunctions, initialState, finalStates):
    self.statesSet = statesSet
    self.alphabet = alphabet
    self.transitionFunctions = transitionFunctions
    self.initialState = initialState
    self.finalStates = finalStates

    if not self._assert():
      self.statesSet = []
      self.alphabet = []
      self.transitionFunctions = []
      self.initialState = None
      self.finalStates = []
      raise Exception('Invalid AFNe')
    
  
  def _assert(self) -> bool:
    haveStates = len(self.statesSet) > 0
    haveAlphabet = len(self.alphabet) > 0
    haveTransitionFunctions = len(self.transitionFunctions) > 0
    haveInitialState = self.initialState in self.statesSet and self.initialState != None
    haveFinalStates = len(self.finalStates) > 0 and len(self.finalStates.intersection(self.statesSet)) > 0

    return haveStates and haveAlphabet and haveTransitionFunctions and haveInitialState and haveFinalStates
  
  def programFunction(self, states, transitionFunction):
    S = set(states)
    unexplored = list(states)
    while len(unexplored) > 0:
      q = unexplored.pop()
      if (q, 'epsilon') in transitionFunction:
        newStates = transitionFunction[(q, 'epsilon')].difference(S)
        S = S.update(newStates)
        unexplored = unexplored.extend(newStates)
    
    return S

  def regognition(self, word):
    activeStates = self.programFunction([self.initialState], self.transitionFunctions)
    for symbol in word:
      newActiveStates = set()
      for state in activeStates:
        if (state, symbol) in self.transitionFunctions:
          newActiveStates.update(self.programFunction(self.transitionFunctions[(state, symbol)], self.transitionFunctions))

      activeStates = newActiveStates
    
    return len(activeStates.intersection(self.finalStates)) > 0