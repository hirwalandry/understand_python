# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
# Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time. However, most approaches to sorting will build directly on what you learned in this section.

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original:")
print(cars)
print("\nHere is the reversed order:")
cars.reverse()
print(cars)
# Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
# The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time

# Finding the Length of a List
length = f"the length of cars is: {len(cars)}".title()
print(length)

