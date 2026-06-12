try:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ValueError:
    print("Please enter a valid integer.")