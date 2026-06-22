'''
Reading a file

'''

file = open("1 table", "r")
content = file.read()
print(content)
file.close()