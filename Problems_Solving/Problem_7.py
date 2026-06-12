# Fabonacci Series

a = 0
b = 1
next = 0
print(a, b, end=" ")

for i in range(8):
  next = a + b
  a,b = b, next
  print(next,  end=" ")