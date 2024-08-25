txt = "The best things in life are free!"
print("expensive" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[3:])

b = "Hello, World!"
print(b[-5:-2])

v = "Hello, World!"
print(v.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + " " +b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.4f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)