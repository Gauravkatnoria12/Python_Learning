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

''' 
Output :
if we add 2 and 3, the output will be 5.0
Enter the operation (+, -, *, /): +
Enter the first number: 2
Enter the second number: 3
Result = 5.0

Also, if we divide 10 by 2, the output will be 5.0
Enter the operation (+, -, *, /): /
Enter the first number: 10
Enter the second number: 2
Result = 5.0

''' 
