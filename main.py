import examples
from nfa import NFA

if __name__ == '__main__':
  
  states, alphabet, transitionFunctions, initialState, finalStates = examples.sample7()

  nfae = NFA(states, alphabet, transitionFunctions, initialState, finalStates)

  nfae.convertToNFA()

  print(nfae.transitionFunctions)

  print(nfae.regognition('00000'))
