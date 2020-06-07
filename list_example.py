#Lists are mutable

my_favorite_things = ["Singing" , "Coding" , "Watching TV" , "Sleeping"]

#change some elements of the list
my_favorite_things[2:] = ["Watching movies" , "Building muscles"]


copy = my_favorite_things
print(id(copy) == id(my_favorite_things))	#True


# Any changes made to copy will be reflected in my_favorite_things
#So copy here is not a new list , but an alias for the list my_favorite_things


other_list = my_favorite_things[:]
print(id(other_list) == id(my_favorite_things))	#False

#Any changes made to other_list will not be reflected in my_favorite_things

#So , other_list is a new list which has copied the elements of the list my_favorite_things

#Another way to make a copy of a list is by using copy function

another_list = other_list.copy()

print(id(another_list) == id(other_list))



copy[1] = "Learning"
print(other_list)			#NO CHANGE
print(my_favorite_things , copy)	#BOTH CHANGED




#Copying is of two types:
#1. Shallow Copy
#2. Deep Copy

#Shallow copy copies only the immutable data in a list. But for the mutable data an alias is made.

stuff = ["Google" , "Youtube" , ["Python" , "CPP" , "Project"]]

other_stuff = stuff.copy()

stuff[2][2] = "Internship"

print(stuff , other_stuff)

#As you see the result ,  in both the lists , Project is replaced by Internship

#This happened because , the mutable data i.e the nested list was not copied value by value. An alias was made for it. Thats why change in original list is reflected in the copy list.

#Let's test this:

print(id(stuff[2]) == id(other_stuff[2]))	#True


#So How to perform deep copy??

import copy

copied_stuff = copy.deepcopy(stuff)

stuff[2][2] = "Project"

print(stuff , copied_stuff)	#both are different

print(id(stuff[2]) == id(copied_stuff[2]))	#False


#Combining lists

stuff = stuff + ["Linux"]

print(stuff)

#OR you can use a function called append

stuff.append("Ubuntu")

print(stuff)


print(list(range(4)))

print(list(range(0,10,2)))

spam = list(range(10,100,5))
print(spam)

somethings = ['walk','talk','enjoy','achieve','try']
for words in range(len(somethings)):
	somethings[words] = somethings[words]+'ing'
print(somethings)

cat = ['fat' , 'orange' , 'big-tailed' , 'furry']

a,b,c,d = cat	#Multiple assignments in python

print(a)
print(b)
print(c)
print(d)

#swap two elements in pyton
a,b = b,a	#swapped
print(a)
print(b)

size , color , ethnicity = 'skinny' , 'brown' , 'hindu'

print(size , color , ethnicity)

#index in python list gives the index of the first occurence of an element in the list

print(cat.index('orange'))
cat.append('orange')
print(cat.index('orange'))

#insert in python list inserts an element ata given index 
cat.insert(1,'grey')
print(cat)

cat.remove('orange')	#removes the word at its first occurence
print(cat)

#remove function in python list
#remove finds the element in the list and then deletes it

#del function in python list
#del deletes a the element at a particular index position. It does not find the element to delete it.

del(cat[4])
print(cat)

del spam[5]
print(spam)

cat.append('Ziggler')
cat.sort()

print(cat)	#Ziggler is at index 0. Why? Because sort() uses ASCII-betical order and not alphabetical order to sort
			#Capital alphabets have smaller ASCII values than small alphabets

#How to sort in actual alphabetical order then??
cat.sort(key=str.lower)	#sort every string by considering it to be small alphabets
print(cat)		# ['big-tailed', 'fat', 'furry', 'grey', 'Ziggler']
			
mixed = ['abc' , 1 ,2 ,3 , 'dog']
print(mixed)
try:
	print(mixed.sort())			#error: dont know how to sort mixed values list
except:
	print("Cannot sort this list")

h = list("Hello")
print(h)

print('abc' in h)	#Returns false becuase 'abc' does not exist in h

name = "Zophie a cat"
newname = name[:7] + "the" + name[8:]
print(newname)
