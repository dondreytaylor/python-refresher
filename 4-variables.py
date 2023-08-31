x = 5
y = "Dondrey Taylor"
# print(x)
# print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


print(type(x))
print(type(y))
print(type(z))


myvar = "Dondrey"
my_var = "Dondrey"
_my_var = "Dondrey"
myVar = "Dondrey"
MYVAR = "Dondrey"
myvar2 = "Dondrey"

# Assign to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign to the same variable
x = y = z = "Orange"

# Unpack 
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Combine strings
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


# Global variables (any variable defined outside the function)
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()