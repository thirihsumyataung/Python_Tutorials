message = input(">")
words = message.split(' ')

emojis = {
    "<3" : "❤️",
    ":)" : "😁",
    ";)" : "😅",
    ":(" : "🙁"
 }
#emoji.get(key, value)
# #i is the key
# --> if you dont have the value , just use the same

output = " "
for i in words :
    output += emojis.get(i,i) + " "

print(output)