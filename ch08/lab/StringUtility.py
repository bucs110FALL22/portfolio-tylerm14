class StringUtility: 
  def __init__(self, string):
    self.newString = string

  def __str__(self):
    return self.newString

  
  def vowels(self):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(0, len(vowels)+1):
      vowels.append(vowels[i].upper())
    vowelCount = 0
    
    for character in range(0, len(self.newString)):
      if self.newString[character] in vowels:
        vowelCount += 1

    if vowelCount >= 5:
      return 'many'
    else:
      return str(vowelCount)

      
  def bothEnds(self):
    beStr = ''
    if len(self.newString) <= 2:
      return ''
    else:
      beStr+=(self.newString[0])
      beStr+=(self.newString[1])
      beStr+=(self.newString[len(self.newString)-2])
      beStr+=(self.newString[len(self.newString)-1])
      return beStr

      
  def fixStart(self):
    if self.newString != '':
      fChar = self.newString[0]
      fsStr = ''
      fsStr += fChar
      for char in range(1, len(self.newString)):
        if self.newString[char] == fChar:
          fsStr += '*'
        else:
          fsStr += self.newString[char]
      return fsStr
    else:
      return ''
    
  
  def asciiSum(self):
    sum = 0
    for char in range(0, len(self.newString)):
      sum += ord(self.newString[char])
    return sum

  def cipher(self):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperAlpha = [letter.upper() for letter in alphabet]
    cStr = ''
    numList = []
    if self.newString != '':
      for i in range(0, len(self.newString)):
        
        if self.newString[i] in alphabet:
          for alp in range(0, len(alphabet)):
            if self.newString[i] == alphabet[alp]:
              numList.append((alp+len(self.newString))%len(alphabet))
          cStr += alphabet[numList[i]]
          
        elif self.newString[i] in upperAlpha:
          for alp in range(0, len(upperAlpha)):
            if self.newString[i] == upperAlpha[alp]:
              numList.append((alp+len(self.newString))%len(upperAlpha))
          cStr += upperAlpha[numList[i]]
          
        elif self.newString[i].isspace() == True:
          numList.append(' ')
          cStr += self.newString[i]
        else:
          cStr += self.newString[i]
    else:
      cStr = ''
    return cStr
