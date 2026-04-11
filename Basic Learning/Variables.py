'''
In Python, we can use the type() function to check the type of a variable. The type() function returns the type of the variable as a string. For example, if we have a variable x that is an integer, we can use type(x) to check its type and it will return <class 'int'>.
Similarly, if we have a variable y that is a string, we can use type(y) to check its type and it will return <class 'str'>. The type() function is useful for debugging and understanding the data types of variables in Python.
'''

a = 5
b = 10

print(f"Sum is:{a + b}, Sub:{a - b}, Multiply:{a * b}, Divide:{a / b}")


'''

Output:
Sum is:15, Sub:-5, Multiply:50, Divide:0.5

'''

# f strings are used to format the string and include variables in the string. The variables are enclosed in curly braces {} and prefixed with f before the string.

c = True
print(f"Value of c is: {c}")
print(f"Type of c is: {type(c)}")


'''

Output:
Value of c is: True
Type of c is: <class 'bool'>

'''


d = "Hello, World!"
print(f"Value of d is: {d}")
print(f"Type of d is: {type(d)}")

'''

Output:
Value of d is: Hello, World!
Type of d is: <class 'str'>

'''

e = 3.14
print(f"Value of e is: {e}")
print(f"Type of e is: {type(e)}")


'''

Output:
Value of e is: 3.14
Type of e is: <class 'float'>

'''

f = None
print(f"Value of f is: {f}")
print(f"Type of f is: {type(f)}")


'''

Output:
Value of f is: None
Type of f is: <class 'NoneType'>

'''