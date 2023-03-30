import examples
from nfa import NFA, generateNFAFromFile, highlightSymbolInWord

if __name__ == '__main__':
  
  # states, alphabet, transitionFunctions, initialState, finalStates = examples.sample7()

  # nfae = NFA(states, alphabet, transitionFunctions, initialState, finalStates)

  # nfae.convertToNFA()

  while True:
    print('''
1 - Load NFA from file
2 - Try existing examples
0 - Exit
    ''')
    response = input('> ')
    if response == '0': break
    elif response == '1':
      fileName = input('File name: ')
      nfaFromFile = generateNFAFromFile(fileName)
      print('Loaded NFA:\n', nfaFromFile)
      while True:
        word = input('Word to test: ')
        print(nfaFromFile.regognition(word))
        res = input('Do you want to test another word? (1-yes | 0-not) > ')
        if res == '0': break
    
    elif response == '2':
      print('''
1 - Words whose third-to-last symbol is 1 | RE: (0+1)*1(0+1)(0+1)
2 - Words that starts with 0 and ends with 1 | RE: 0(0+1)*1
3 - Words that starts with 001 | RE: 001(0+1)*
4 - Words witch contains 110 as substring | RE: (0+1)*110(0+1)*
5 - Words that start and end with the same symbol | RE: 0(0+1)*0 | 1(0+1)*1 | 0 | 1
6 - Words that contain a or bb or ccc as a suffix | RE: (a+b+c)*a | (a+b+c)*bb | (a+b+c)*ccc
7 - Only accepts aa or bb | RE: aa | bb
8 - Words where b and c only appear after the occurrence of a | RE: (a(b+c)*)* | e
9 - Words that contain a as suffix or ba as prefix | RE: (a+b)*a | ba(a+b)*
        ''')
      response = input('> ')
      sampleChoosen = None
      if response == '1': sampleChoosen = examples.sample0
      elif response == '2': sampleChoosen = examples.sample1
      elif response == '3': sampleChoosen = examples.sample2
      elif response == '4': sampleChoosen = examples.sample3
      elif response == '5': sampleChoosen = examples.sample4
      elif response == '6': sampleChoosen = examples.sample5
      elif response == '7': sampleChoosen = examples.sample6
      elif response == '8': sampleChoosen = examples.sample7
      elif response == '9': sampleChoosen = examples.sample8
      else: continue

      states, alphabet, transitionFunctions, initialState, finalStates = sampleChoosen()

      nfa = NFA(states, alphabet, transitionFunctions, initialState, finalStates)

      print('Loaded NFA:\n', nfa)
      while True:
        word = input('Word to test: ')
        print('\n', nfa.regognition(word))
        res = input('Do you want to test another word? (1-yes | 0-not) > ')
        if res == '0': break
    
    else: continue

print('End of program!')