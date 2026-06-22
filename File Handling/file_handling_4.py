'''
Write tables upto n

'''

n = 10

for i in range(1, n + 1):
  with open(f"{i} table", "w") as file:
    file.write(f"Table of {i}\n")
    file.write(f"\n")
    for j in range(1, 11):
      file.write(f"{j} x {i} = {j * i}\n")

print("Done")