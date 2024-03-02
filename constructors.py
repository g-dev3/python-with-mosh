class Point:
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10,20)
point.x = 11
print(point.x)

class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hii I am {self.name}")


john = Person("G dev")

bob = Person("bob")

print(john.name)
bob.talk()
john.talk()