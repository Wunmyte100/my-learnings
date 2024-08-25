x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

  x = "interesting"
  print("Python is " + x)

myfunc()
print("Python is " + x)
x=5
print(type(x))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))

print("Hello")
print('Hello')
print(5)
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[5])

for x in "apple":
  print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("bag" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("No, 'free' is present.")

  