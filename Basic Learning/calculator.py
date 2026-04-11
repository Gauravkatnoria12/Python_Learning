operation = input("Enter the operation (+, -, *, /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if operation == "+" :
  print(f"Result = {a + b}")
elif operation == "-" :
  print(f"Result = {a - b}") 
elif operation == "*" :
  print(f"Result = {a * b}")
elif operation == "/" :
  print(f"Result = {a / b}")