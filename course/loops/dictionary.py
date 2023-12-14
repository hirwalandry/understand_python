numbers={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
phone_number = input("Phone: ")
output=""
for number in phone_number:
    output+= numbers.get(number, "!") + " "
print(output)
