from nfa import NFA

if __name__ == '__main__':
  states = ['q1', 'q2', 'q3', 'q4']
  alphabet = ['0', '1']
  transitionFunctions = {
    ('q1', '0'): {'q1'},
    ('q1', '1'): {'q1', 'q2'},
    ('q2', '0'): {'q3'},
    ('q2', '1'): {'q3'},
    ('q3', '0'): {'q4'},
    ('q3', '1'): {'q4'},
  }
  initialState = 'q1'
  finalStates = {'q4'}

  nfa = NFA(states, alphabet, transitionFunctions, initialState, finalStates)

  print(nfa.regognition('10101'))