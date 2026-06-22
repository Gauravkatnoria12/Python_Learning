'''
Reading multiple files wih for loop

'''
for i in range(1, 11):
  file = open(f"{i} table", "r")
  content = file.read()
  print(content)
  file.close()