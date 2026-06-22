n = 10

'''
* * * * * * * * * *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *

'''

for i in range(1, n):
  for j in range(1, n):
    if i == 1 or i == n - 1 or j == 1 or j == n - 1:
      print("*  ", end="")
    else :
        print("   ", end="")
  print()


print("\n")


'''
 1 1  1 2  1 3  1 4  1 5 

 2 1  2 2  2 3  2 4  2 5 

 3 1  3 2  3 3  3 4  3 5 

 4 1  4 2  4 3  4 4  4 5 

 5 1  5 2  5 3  5 4  5 5 

'''

for i in range(1, 6):
  for j in range(1, 6):
      print(f" {i} {j} ", end="")
  print("\n")