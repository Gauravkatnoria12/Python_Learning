def numbers(n) :
  i = 1
  if n <= 100 :
      while i <= n :
        print(i)
        i += 1
  else:
      print('Big number')


numbers(int(input('Enter a number btw 1 to 100: ')))

