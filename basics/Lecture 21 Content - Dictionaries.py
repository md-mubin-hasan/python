print("1) Create a fruit and colour mapping using lists")
print()

fruit = ["apple", "grapes", "mango", "orange"]
print("The fruit list is ", fruit)

colour = ["red", "purple", "yellow", "orange"]
print("The colour list is ", colour)
print()

q = input("Which fruit do you want to look at (apple, grapes, mango or orange)? ")
while q not in fruit:
    print("Please enter a valid fruit.")
    print()
    q = input("Which fruit do you want to look at (apple, grapes, mango or orange)? ")

print()

print("Getting the index of the fruit... ", end = "")
i = fruit.index(q)
print(i)
print()

c = colour[i]
print("The colour of the fruit is ", c)
print()

input("Please 'enter' to continue...")
print()

print("2) Create a fruit and colour mapping using a dictionary")
print()

mapping = {"apple":"red", "grapes":"purple", "mango":"yellow", "orange":"orange"}
print("The dictionary is ", mapping)
print()

q = input("Which fruit do you want to look at (apple, grapes, mango or orange)? ")
while q not in mapping:
    print("Please enter a valid fruit.")
    print()
    q = input("Which fruit do you want to look at (apple, grapes, mango or orange)? ")

print()
c = mapping[q]
print("The colour of the fruit is ", c)
print()

heads = {"David": (589, 106, 48, 63),
         "Gibson": (474, 102, 44, 58),
         "Jogesh": (438, 146, 45, 60),
         "Paul": (522, 162, 55, 68)}
print("Head and location mapping is: ")
print(heads)
print()

print("Where is Paul?")
where_is_paul = heads["Paul"]
print(where_is_paul)
print()

print("David has a smaller head...")
heads["David"]= (588, 104, 48, 57)
print(heads)
print()

print("Sean has joined us!")
heads["Sean"] = (628, 146, 46, 58)
print(heads)
print()

print("The president has left us now...")
del heads["Paul"]
print(heads)
print()

print("All the information in the dictionary:")
for key, value in heads.items():
    print(key, value)
print()

print("The people are:")
for key in heads.keys():
    print(key)
print()

print("The positions and dimensions are:")
for value in heads.values():
    print(value)
print()

print("Is David in the picture?")
if "David" in heads:
    print("He is there!")
