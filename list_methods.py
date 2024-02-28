numbers = [5,2,1,7,4]

numbers.append(20)

print(numbers)

numbers.insert(-1,0)

print(numbers)

numbers.remove(0)

print(numbers)

numbers.pop()

print(numbers.index(5))

print(numbers.count(7))

print(7 in numbers)

print(numbers.sort())

print(numbers.reverse())

print(numbers)

number2 = numbers.copy()

number2.sort()
print(number2)

numbers.clear()

print(numbers)

# remove duplicate numbers
numbers2 = [2,2,4,6,3,4,6,1]
unique = []
for number in numbers2:
  if number not in unique:
    unique.append(number)

print(unique)

