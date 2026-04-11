coordinate = (4, 5, 6, 7, 8)

# We can't Change the Value or Anything in Tuples but we can access them
# For Example

print(coordinate[0])

'''
Output :
4

'''


# Another Tuple
# But we can change tuple inside list

coordinates = [(1, 2), (2, 4), (4, 5)]
coordinates[1] = (2, 2)
print(coordinates)

'''
Output :
[(1, 2), (2, 2), (4, 5)]

'''


tuple_1 = ()

print(type(tuple_1))

'''
Output :
<class 'tuple'>

'''
