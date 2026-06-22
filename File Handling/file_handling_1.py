'''
Object data of file

'''

f = open("geek.txt", "r")
print(f)


#  Checking File Properties


print()

f = open("geek.txt", "r")
print("Filename:", f.name)
print("Mode:", f.mode)
print("Is Closed?", f.closed)

f.close()
print("Is Closed?", f.closed)