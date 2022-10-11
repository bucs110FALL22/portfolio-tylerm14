rows = int(input('Number of Rows: '))

def star_pyramid():
  str = '*'
  for i in range(rows):
    print(str)
    str = str*rows

def rstar_pyramid():
  str = '*'*rows
  for i in range(rows):
    print(str)
    str = str[:-1]

star_pyramid()
rstar_pyramid()