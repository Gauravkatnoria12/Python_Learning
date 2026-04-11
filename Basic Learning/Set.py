fruits = {"apple", "banana", "cherry"}

fruits.add("orange")           # Add one item
fruits.update(["mango", "grape"])  # Add multiple items
fruits.remove("banana")        # Remove (raises error if not found)
fruits.discard("kiwi")         # Removing item (without any error if not found)

print(fruits)

'''
Output :
{'cherry', 'mango', 'grape', 'apple', 'orange'}

'''