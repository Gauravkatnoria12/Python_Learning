import random

print("\n# Welcome to advance no. guessing game #\n")
try:
  low = int(input("Enter lower value: "))
  high = int(input("Enter higher Value: "))

  if low > high or low == high:
    print("Invalid Range.")
  else:
    r = random.randint(low, high)
    print("")
    userinp = int(input("Enter a number: "))
    if userinp > r:
      print("High, Try again.")
    elif userinp < r:
      print("Low, Try again.")
    else:
      print("Congratulations!")
    attempt = 1
    while(r != userinp):
      userinp = int(input("Enter a number: "))
      if userinp > r:
        print("High, Try again.")
      elif userinp < r:
        print("Low, Try again.")
      else:
        print("Congratulations!")
      attempt += 1
    print(f"You won in {attempt} attempts")
except ValueError:
  print("Invalid Value.")