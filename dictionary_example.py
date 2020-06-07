cat = {'size':'small' , 'color':'grey' , 'disposition':'loud'}

#Dictionary have key-value pairs

#What is key function?
print(cat.keys)		#prints " <built-in method keys of dict object at 0x7f379d03eb90> "


print(cat.keys())	#prints ['color', 'disposition', 'size']

print(cat.values)	#prints "<built-in method values of dict object at 0x7f933f577b90>"

print(cat.values())	#prints ['grey', 'loud', 'small']

print(cat.items)	#prints <built-in method items of dict object at 0x7f3435e56b90>

print(cat.items())	#prints [('color', 'grey'), ('disposition', 'loud'), ('size', 'small')]

print(cat['size'])
print(cat["color"])

print("size" in cat)	#True
print("grey" in cat)	#False because in only checks keys and not values


#making list from dictionary

l = list(cat.keys())
print(l)

v = list(cat.values())
print(v)

a = list(cat.items())
print(a)


for k in cat.keys():
	print k

for v in cat.values():
	print v
	
for k,v in cat.items():
	print(k,v)

#print(cat['fat'])	#Keyerror: fat is not a  key 

if 'fat' in cat:	#this is long and tedious to do everytime
	print(cat['fat'])

#alternative: use get() function.
#in get() function you can set the default value to return if the key does not exist in the dictionary

print(cat.get('fat',0))	#prints 0

#but what if we want to add the key-value if it does not exist in dictionary
#use setdefault

cat.setdefault('fat',True)	#'fat' was not a key and now we made it a key with value True
print(cat)	#{'color': 'grey', 'fat': True, 'disposition': 'loud', 'size': 'small'}


#list of dictionaries
l = []
l.append(cat)

print(l)

dog = {'color':'white' , 'size':'small' , 'disposition':'loud'}

l.append(dog)

print(l)

	
