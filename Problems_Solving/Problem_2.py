# Total No. of Vowels

word = "Python is my favourite language"
vowels = "aeiou"
v = 0

for x in word:
  if x in vowels:
    v += 1

print(f"Total Vowels : {v}")