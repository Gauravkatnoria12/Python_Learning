
'''
* * * * *
  * * * *
    * * *
      * *
        *
    
'''

for i in range(1, 6):
  for j in range(1, 6):
    if j >= i:
      print(f" * ", end="")
    else:
      print("   " , end="")
  print("\n")

'''
*
* *
* * *
* * * *
* * * * *

'''


for i in reversed(range(1, 6)):
  for j in reversed(range(1, 6)):
    if j >= i:
      print(f" * ", end="")
    else:
      print("   " , end="")
  print("\n")