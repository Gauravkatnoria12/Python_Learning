print("\n# Temperature Convertor #\n")
print("1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")
try:
  choice = float(input("Enter your choice (1 or 2): "))

  if choice == 1:
    user_input = float(input("Enter value: "))
    print(f"Temperature (Celsius to Fahrenheit): {(user_input * 9/5) + 32}°F")
  elif choice == 2:
    user_input = float(input("Enter value: "))
    print(f"Temperature (Fahrenheit to Celsius): {(user_input - 32) * 5/9}°C")
  else:
    print("Invalid Value")
except ValueError:
  print("Invalid Value")