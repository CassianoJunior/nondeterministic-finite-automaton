class NFA:
  def __init__(self, statesSet, alphabet, transitionFunctions, initialState, finalStates):
    self.statesSet = statesSet
    self.alphabet = alphabet
    self.transitionFunctions = transitionFunctions
    self.initialState = initialState
    self.finalStates = finalStates
    self.hasEpsilonTransition = self.isNFAe()

    if not self._assert():
      self.statesSet = []
      self.alphabet = []
      self.transitionFunctions = {}
      self.initialState = None
      self.finalStates = []
      raise Exception('Invalid AFNe')
  
  def __str__(self):
    return f"""
      States: {self.statesSet}
      Alphabet: {self.alphabet}
      Transition Functions: {self.transitionFunctions}
      Initial State: {self.initialState}
      Final States: {self.finalStates}
      Has Epsilon Transition: {self.hasEpsilonTransition}
    """
  
  def isNFAe(self):
    for transitionFunction in self.transitionFunctions:
      if transitionFunction[1] == 'epsilon':
        return True
    
    return False
    

  def _assert(self) -> bool:
    statesIsNotEmpty = len(self.statesSet) > 0
    alphabetIsNotEmpty = len(self.alphabet) > 0
    transitionFunctionsWasDefined = len(self.transitionFunctions) > 0
    initialStateIsDefined = self.initialState != None
    initialStateBelongsToStates = self.initialState in self.statesSet
    finalStatesIsDefined = len(self.finalStates) > 0 
    finalStatesBelongsToStates = len(self.finalStates.intersection(self.statesSet)) > 0

    return (
      statesIsNotEmpty and 
      alphabetIsNotEmpty and 
      transitionFunctionsWasDefined and 
      initialStateIsDefined and 
      initialStateBelongsToStates and 
      finalStatesIsDefined and 
      finalStatesBelongsToStates
    )
  
  def programFunction(self, states):
    statesSet = set(states)
    unexploredStates = list(states)
    while len(unexploredStates) > 0:
      unexploredStates.pop()
      # state = unexploredStates.pop()
      # if (state, 'epsilon') in self.transitionFunctions:
      #   newStates = self.transitionFunctions[(state, 'epsilon')].difference(statesSet)
      #   statesSet.update(newStates)
      #   unexploredStates.extend(newStates)
    
    return statesSet
  
  def _assertWord(self, word) -> bool:
    for symbol in word:
      if symbol not in self.alphabet and symbol != 'epsilon':
        return False
    
    return True
  
  def convertToNFA(self):
    self.hasEpsilonTransition = False

    for state in self.statesSet:
      if (state, 'epsilon') in self.transitionFunctions:
        activeStatesFromEpsilon = self.transitionFunctions[(state, 'epsilon')]

        transitionsThatReachState = list(filter(lambda transition: state in transition[1], self.transitionFunctions.items()))
          
        for transition in transitionsThatReachState:
          self.transitionFunctions[(transition[0][0], transition[0][1])] = transition[1].union(activeStatesFromEpsilon)

        for activeState in activeStatesFromEpsilon:
          transitionsThatLeaveActiveState = list(filter(lambda transition: activeState in transition[0], self.transitionFunctions.items()))
          for transition in transitionsThatLeaveActiveState:
            if (state, transition[0][1]) in self.transitionFunctions: 
              self.transitionFunctions[(state, transition[0][1])].update(transition[1])
            else:
              self.transitionFunctions[(state, transition[0][1])] = transition[1]

        self.transitionFunctions.pop((state, 'epsilon'))
    

  def regognition(self, word):
    if not self._assertWord(word): raise Exception('Word has invalid symbols for NFA alphabet')

    if self.hasEpsilonTransition: self.convertToNFA()
    
    activeStates = self.programFunction([self.initialState])
    for symbol in word:
      # print(f"D")
      newActiveStates = set()
      for state in activeStates:
        if (state, symbol) in self.transitionFunctions:
          newActiveStates.update(self.programFunction(self.transitionFunctions[(state, symbol)]))

      activeStates = newActiveStates
    
    return len(activeStates.intersection(self.finalStates)) > 0