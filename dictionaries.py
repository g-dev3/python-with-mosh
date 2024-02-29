# Name: John Smith
# Email: john@gmail.com
# Phone: 3301


customber = {
  "name": "John Smith",
  "age": 30,
  "is_verified": True
}

print(customber["name"])

print(customber.get("Birthdate","Jan 6 2003"))

customber["name"] = "jack Smith"

print(customber["name"])

customber["age"] = 21

print(customber["age"])


phone = input("phone: ")

digits = {
  "1":"One",
  "2": "Two",
  "3": "Three"
}

output = ""
for call in phone:
 output += digits.get(call, "!") + " "

print(output)