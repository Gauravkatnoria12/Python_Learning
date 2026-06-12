import sys

while(1):
  print("\n")
  print("# CALCULATOR #")
  print("1 - Additon")
  print("2 - Subtraction")
  print("3 - Multiplication")
  print("4 - Division")
  print("5 - Exit")

  choice = int(input("Enter your chioce: "))

  if choice == 1:
    a = int(input("Enter first no. : "))
    b = int(input("Enter second no. : "))
    print(f"😎 Result: {a + b}")
  if choice == 2:
    a = int(input("Enter first no. : "))
    b = int(input("Enter second no. : "))
    print(f"😎 Result: {a - b}")
  if choice == 3:
    a = int(input("Enter first no. : "))
    b = int(input("Enter second no. : "))
    print(f"😎 Result: {a * b}")
  if choice == 4:
    a = int(input("Enter first no. : "))
    b = int(input("Enter second no. : "))
    try:
      result = a / b
      print(f"😎 Result: {result}")
    except ZeroDivisionError:
      print("You cannot divide by zero!")
  if choice == 5:
    sys.exit()