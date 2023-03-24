def sample0():
  """
    Recognized language: Language where antepenultimate symbol is 1 | RE: (0+1)*1(0+1)(0+1)
    params: nothing;
    return: 
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """
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

  return states, alphabet, transitionFunctions, initialState, finalStates


def sample1():
  """
    Recognized language: Words starts with 0 and ends with 1 | RE: 0(0+1)*1
    params: nothing;
    return: 
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """
  states = ['q1', 'q2', 'q3']
  alphabet = ['0', '1']
  transitionFunctions = {
    ('q1', '0'): {'q2'},
    ('q2', '0'): {'q2'},
    ('q2', '1'): {'q2', 'q3'},
    ('q3', '1'): {'q3'}
  }
  initialState = 'q1'
  finalStates = {'q3'}

  return states, alphabet, transitionFunctions, initialState, finalStates

def sample2():
  """
    Recognized language: Words starts with 001 | RE: 001(0+1)*
    params: nothing;
    return: 
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """
  states = ['q1', 'q2', 'q3', 'q4']
  alphabet = ['0', '1']
  transitionFunctions = {
    ('q1', '0'): {'q2'},
    ('q2', '0'): {'q3'},
    ('q3', '1'): {'q4'},
    ('q4', '0'): {'q4'},
    ('q4', '1'): {'q4'},
  }
  initialState = 'q1'
  finalStates = {'q4'}

  return states, alphabet, transitionFunctions, initialState, finalStates

def sample3():
  """
    Recognized language: Words witch contains 110 as substring | RE: (0+1)*110(0+1)*
    params: nothing;
    return: 
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """
  states = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']
  alphabet = ['0', '1']
  transitionFunctions = {
    ('q1', '0'): {'q1'},
    ('q1', '1'): {'q1', 'q2'},
    ('q2', '1'): {'q3'},
    ('q3', '0'): {'q4'},
    ('q4', '0'): {'q4'},
    ('q4', '1'): {'q4'},
  }
  initialState = 'q1'
  finalStates = {'q4'}

  return states, alphabet, transitionFunctions, initialState, finalStates

def sample4():
  """
    Recognized language: Words that start and end with the same symbol | RE: 0(0+1)*0 | 1(0+1)*1 | 0 | 1
    params: nothing;
    return: 
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """

  states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7']
  alphabet = ['0', '1']
  transitionFunctions = {
    ('q0', 'epsilon'): {'q1', 'q4'},
    ('q0', '0'): {'q7'},
    ('q0', '1'): {'q7'},
    ('q1', '0'): {'q2'},
    ('q2', '0'): {'q2', 'q3'},
    ('q2', '1'): {'q2'},
    ('q3', 'epsilon'): {'q7'},
    ('q4', '1'): {'q5'},
    ('q5', '0'): {'q5'},
    ('q5', '1'): {'q5', 'q6'},
    ('q6', 'epsilon'): {'q7'},
  }
  initialState = 'q0'
  finalStates = {'q7'}

  return states, alphabet, transitionFunctions, initialState, finalStates

def sample5():
  """
    Recognized language: Words that contain a or bb or ccc as a suffix | RE: (a+b+c)*a | (a+b+c)*bb | (a+b+c)*ccc
    params: nothing;
    return: 
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """
  states = ['q0', 'q1','q2','q3','q4','q5','q6', 'q7']
  alphabet = ['a', 'b', 'c']
  transitionFunctions = {
    ('q0', 'epsilon'): {'q1', 'q2', 'q4'},
    ('q0', 'a'): {'q0'},
    ('q0', 'b'): {'q0'},
    ('q0', 'c'): {'q0'},
    ('q1', 'a'): {'q7'},
    ('q2', 'b'): {'q3'},
    ('q3', 'b'): {'q7'},
    ('q4', 'c'): {'q5'},
    ('q5', 'c'): {'q6'},
    ('q6', 'c'): {'q7'},
  }
  initialState = 'q0'
  finalStates = {'q7'}

  return states, alphabet, transitionFunctions, initialState, finalStates

def sample6():
  """
    Recognized language: Only accepts aa or bb | RE: aa | bb 
    params: nothing;
    return:
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """

  states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9']
  alphabet = ['a', 'b']
  transitionFunctions = {
    ('q0', 'epsilon'): {'q1', 'q5'},
    ('q1', 'a'): {'q2'},
    ('q2', 'epsilon'): {'q3'},
    ('q3', 'a'): {'q4'},
    ('q4', 'epsilon'): {'q9'},
    ('q5', 'b'): {'q6'},
    ('q6', 'epsilon'): {'q7'},
    ('q7', 'b'): {'q8'},
    ('q8', 'epsilon'): {'q9'},
  }
  initialState = 'q0'
  finalStates = {'q9'}

  return states, alphabet, transitionFunctions, initialState, finalStates

# def sample7():
#   """
#     Recognized language: Words that contain only 0's and amount of 0 is multiple of 2 or 3 | RE: (0+1)*0(0+1)*0(0+1)* | (0+1)*0(0+1)*0(0+1)*0(0+1)*
#     params: nothing;
#     return:
#       states -> list of states;
#       alphabet -> list of symbols;
#       transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
#       initialState -> initial state;
#       finalStates -> set of final states in form: {state1, state2, ...};
#   """

#   states = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']
#   alphabet = ['0']
#   transitionFunctions = {
#     ('q1', 'epsilon'): {'q4', 'q3'},
#     ('q4', '0'): {'q2'},
#     ('q2', '0'): {'q4'},
#     ('q3', '0'): {'q5'},
#     ('q5', '0'): {'q6'},
#     ('q6', '0'): {'q3'},
#   }

#   initialState = 'q1'
#   finalStates = {'q4', 'q3'}

#   return states, alphabet, transitionFunctions, initialState, finalStates

def sample8():
  """
    Recognized language: Words where b and c only appear after the occurrence of a | RE: a(b+c)* | e
    params: nothing;
    return:
      states -> list of states;
      alphabet -> list of symbols;
      transitionFunctions -> dictionary of transition functions in form: key: (state, symbol), value: set of states in form: {state1, state2, ...};
      initialState -> initial state;
      finalStates -> set of final states in form: {state1, state2, ...};
  """

  states = ['q0', 'q1', 'q2']
  alphabet = ['a', 'b', 'c']
  transitionFunctions = {
    ('q0', 'a'): {'q1'},
    ('q1', 'epsilon'): {'q0'},
    ('q1', 'b'): {'q2'},
    ('q1', 'c'): {'q2'},
    ('q2', 'epsilon'): {'q0'},
  }
  initialState = 'q0'
  finalStates = {'q0'}

  return states, alphabet, transitionFunctions, initialState, finalStates

def sample9():
  """
    Recognized language: Words that contain a as suffix or ba as prefix | RE: (a+b)*a | ba(a+b)* 
  """

  states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
  alphabet = ['a', 'b']
  transitionFunctions = {
    ('q0', 'epsilon'): {'q1', 'q3'},
    ('q1', 'a'): {'q1', 'q2'},
    ('q1', 'b'): {'q1'},
    ('q3', 'b'): {'q4'},
    ('q4', 'a'): {'q5'},
    ('q5', 'b'): {'q5'},
    ('q5', 'a'): {'q5'},
  }
  initialState = 'q0'
  finalStates = {'q2', 'q5'}

  return states, alphabet, transitionFunctions, initialState, finalStates