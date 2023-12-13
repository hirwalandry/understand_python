motorcycles = [] 
motorcycles.append('honda') 
motorcycles.append('yamaha') 
motorcycles.append('suzuki') 
print(motorcycles)
# modifying
motorcycles[0] = "ducati"
print(motorcycles)

# adding
motorcycles.append("kawasaki")
print(motorcycles)
# You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item.
motorcycles.insert(0, 'apache')
print(motorcycles)
# delete
del motorcycles[-1]
print(motorcycles)
# Sometimes you’ll want to use the value of an item after you remove it from a list. For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position. In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members. The pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list.
popped_motorcycles = motorcycles.pop() 
print(popped_motorcycles)
# You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.
last_owned = motorcycles.pop(-1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")
# Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove() method.
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
