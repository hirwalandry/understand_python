input_message = input(">")


def messages(message):
    words = input_message.split(" ")
    emojis = {
    ":)": "smiley",
    ":(": "sady"
     }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(messages(input_message))