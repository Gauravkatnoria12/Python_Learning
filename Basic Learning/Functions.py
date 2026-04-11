def numbers(n) :
  i = 1
  if n <= 100 :
      while i <= n :
        print(i)
        i += 1
  else:
      print('Big number')


numbers(int(input('Enter a number btw 1 to 100: ')))

'''
Output :
If we enter 5, the output will be 1 to 5

Enter a number btw 1 to 100: 5
1
2
3
4
5

'''