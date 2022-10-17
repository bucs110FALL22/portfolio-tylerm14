def percentage_to_letter(score=0):
  score = int(input('Input Numerical Score: '))
  letter = None
  if (score >= 90):
    letter = 'A'
  elif (score >= 80):
    letter = 'B'
  elif (score >= 70):
    letter = 'C'
  elif (score >= 60):
    letter = 'D'
  else:
    letter = 'F'
  return letter

def is_passing(letter):
  if (letter == 'A') or (letter == 'B') or (letter == 'C'):
    print('Pass')
    return True
  else:
    print('Fail')
    return False
    
is_passing(percentage_to_letter())