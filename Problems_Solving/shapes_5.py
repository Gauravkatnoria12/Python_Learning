'''
Visualizing the values of i and j

'''

for i in reversed(range(1, 6)):
  for j in reversed(range(1, i+1)):
       print(f" {i} {j} ", end="")
  print("\n")


for i in range(1, 6):
  for j in range(1, 6):
       if i >= j:
         print(f" {i} {j} ", end="")
  print("\n")
