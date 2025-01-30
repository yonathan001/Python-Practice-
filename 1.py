a = "Hello, World!"
print(a[0])

for x in "banana":
  print(x)
  


  txt = "The best things in life are free!"
print("best" not in txt)

b = "Hello, World!"
print(b[-5:-2])

w = "Hello, World!"
print(w.replace("H", "J"))

age =43
txt = "My name is John, and I am  {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

thislist = ["apple", "banana", "cherry"]
tropical = ["apple", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)