# class MyClass:
#     x = 5

# c = MyClass()
# print(c.x)


class MyClass:

    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

c = MyClass("Dondrey", 31)
print(c.name)
print(c.age)
print(c)