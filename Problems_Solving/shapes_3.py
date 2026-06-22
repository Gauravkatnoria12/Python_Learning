'''
* * * * *
* * * *
* * *
* *
*

'''

for i in reversed(range(1, 6)):
  for j in reversed(range(1, 6)):
       if i >= j:
         print(f"  *  ", end="")
  print("\n")


for i in reversed(range(1, 6)):
  for j in reversed(range(1, i+1)):
       print(f"  *  ", end="")
  print("\n")