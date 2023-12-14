squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. List comprehensions are not always presented to beginners, but I have included them here because you’ll most likely see them as soon as you start looking at other people’s code

squares = [value**2 for value in range(1, 11)]
print(squares)

