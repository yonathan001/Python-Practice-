i = 0
while i < 6:
  i += 1
  if i == 3:
    break
  print(i)


  z = 1
while z < 6:
  print(z)
  z += 1
else:
  print("z is no longer less than 6")

  
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")

  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)