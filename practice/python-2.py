# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Python - Output Variables
# print function
x = "Python is awesome"
print(x)
# different way
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# printing str intiger
x = 5
y = 10
print(x + y)  # correct sytax

x = 5
y = "John"
# print(x + y) # error