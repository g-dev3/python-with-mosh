massage = input(">")
words = massage.split(' ')
# Good morning :)
emojis = {
  ":)": "😀",
  ":(": "😔"
}
output = ""
for word in words:
 output += emojis.get(word,word) + " "

print(output)