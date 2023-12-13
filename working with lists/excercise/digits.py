for value in range(1, 21):
    print(value)

digits = list(range(1, 1_000_000))
print(min(digits))
print(max(digits))
print(sum(digits))

for value in range(1, 21, 2):
    print(value)

multiplied_digits = []
for value in range(3, 31):
    multiplied_digits.append(value * 3)
print(multiplied_digits)

cube_digits = [value**3 for value in range(1, 11)]

print(cube_digits)
