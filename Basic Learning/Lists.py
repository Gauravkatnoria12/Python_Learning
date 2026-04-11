                                          # Lists In Python 

print("Top")

                                              # Lists  1
friend = ["Kevin", "Harsh", "Karen", ]
print(friend)
   

                                         # -ve Index Values  2
Friend = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
print(Friend[-1])


                                    # Changing the index Values  3
Friend = ["Kevin", "Harsh", "Jass","Toby"]
Friend[1] = "Mike"
print(Friend[1])


                                # Starting Lists from the given indexes  4
Friend = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
print(Friend[1:4])


                                          # Adding other list  5
lucky_numbers = [4, 8, 12, 5]
friends = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
friends.extend(lucky_numbers)
print(friends)


                                     #Adding other name of a friend  6
friends = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
friends.append("Creed")
print(friends)

                             # Extending + Adding a name at given index Value  7
friends = ["Kevin", "Harsh", "Jass", "Oscar","Toby", "Creed"]
friends.insert(0, "Kelly")
print(friends)


                                       # Removing name from List  8
friends = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
friends.remove("Jass")
print(friends)


                                       # Printing index of names  9
friends = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
print(friends.index("Harsh"))


                     # Counting the word how many times its written in the list  10 
friends = ["Kevin", "Harsh", "Jass", "Oscar", "Oscar","Toby"]
print(friends.count("Oscar"))


                                      # Sorting The List In Order  11
friends = ["Kevin", "Harsh", "Jass", "Oscar","Toby"]
friends.sort()
print(friends)


                                         # Reverse of a list  12
lucky_numbers = [4, 8, 12, 5]
lucky_numbers.reverse()
print(lucky_numbers)


                                        # Making copy of a list  13
lucky_numbers = [4, 8, 12, 5]
lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)


print("Bottom")


