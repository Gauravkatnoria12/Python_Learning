result = 1
for index in range(3):
    result = result * 2
print(result)


n = int(input('Enter a number: '))

for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')

'''
Output :
If we enter 5, the output will be the multiplication table of 5 from 1 to 10
Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

'''