names = ['John','Bob','Mosh','Sarah','Mary']

print(names[1])

print(names[-1])

print(names[2:])

print(names[2:4])

print(names[:4])

print(names)

names[0] = 'Jon'

print(len(names))

numbers = [3,6,2,8,4,10]

max = numbers[0]

for number in numbers:
  if number > max:
    max = number

print(max)

min = numbers[0]
for number in numbers:
  if number < min:
    min = number

print(min)