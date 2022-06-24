string = input('>')
words = string.split(" ")
emojies = {
    ":(" : "🙃",
    ":)" : "😀" ,
}

output = ""
for word in words:
    output += emojies.get(word , word) + " "

print(output)
