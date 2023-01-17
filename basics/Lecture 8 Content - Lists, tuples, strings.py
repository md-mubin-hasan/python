
#import turtle

#turtle.speed(0)

for word in ["a", "b", "c"]:
    print(word, end=" ")

colors = ["abc", "bcd", "cde", "def"]
#for a in colors:
    #print(a)

funnylist = [True, 24, "Abc"]
funny = [2, 2, 3, 24, 3]
#print(funnylist)

for b in funnylist:    #Going through everything in the list
    print(b)

funnylist.insert(0,4) #adds where
funnylist.remove(24)
funnylist.append("Mubin")
len(funnylist) #what is the length of the list, funnylist

for index in range(len(funnylist)):  #Going through everything in the list
    print(funnylist[index])

funnylist.reverse()

print(funnylist)

funny.sort()
colors.sort()
print(funny)
print(colors)
print(funny.count(2)) #prints how many times it is present in the list
print(funny.index(24)) #prints the index where this number is stored

funny.extend([23, 3 , 4, 6])
print(funny)

#2D lists

things = [[1,2],[3,4],[5,6]]
print(things[1][1])

#tuples

mubin = ("a","b","c","d","e") #we can not change the content later
#len(), count(), index() works just fine in tuples
#insert(), remove(), append(), sort(), reverse(), extend() does not work in tuples

#string is just simple text
abc = "abc"
print(abc[2])
#String is similar to a tuple of letters, we can not change the content of the string
#abc[1] = "d" will not work
#len(), count(), index() works just fine in string
#insert(), remove(), append(), sort(), reverse(), extend() does not work in string





#for m in range(0, 300, 2):
    #turtle.forward(m)
    #turtle.right(75)

#for n in range(300, 2, -2):
    #turtle.forward(n)
    #turtle.right(75)
#turtle.done()

