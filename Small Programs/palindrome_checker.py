string = input("Enter a String: ")
reverse = string[::-1]
print("Reverse : ", string[::-1])

if string == reverse:
  print("Its Palindrome.")
else: 
  print("No, Its not a Palindrome.")