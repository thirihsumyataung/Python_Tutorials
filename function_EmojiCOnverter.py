def emoji_converter(message):
    words = message.split(" ")

    emoji = {
        ":)" :"😄" ,
        "<3" : "❤️",
        ":(" : "🙁"
    }
    output = " "
    for word in words:
        output += emoji.get(word, word) + " "

    #print(output)
    return output


words = input(">>")
result = emoji_converter(words)
print(result)



