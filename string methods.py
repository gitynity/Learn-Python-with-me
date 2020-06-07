#upper() , lower() , title()
spam = "Hello World"
print(spam.upper())	#did not change the spam
print(spam)
spam = spam.lower()
print(spam)

print(spam.title())

#isupper() and islower()
print('12345'.isupper())	#False
print('12345'.islower())	#False

print(spam.islower())	#True

#isalpha() : letters only
#isalnum() : letters and alphabets
#isdecimal() : decimal number
#isspace()	:  whitespaces only
#istitle()	: titlecase only

print(spam.isalpha())	#False because has space
print('hello123'.isalnum())	#True
print('12345'.isdecimal())	#True
print('Hello World'[5].isspace())	#True
print('This Is Title Case'.istitle())	#True


#startswith() , endswith()
print(spam.startswith('hello'))	#True
print(spam.endswith('ld'))	#True

#join()	is used when you have a list of strings and you want to join them to make a single string
#join() is called on a string and is passed a list of strings and returns a string

pets = ' , '.join(['cats','dogs','parrot'])
print(pets)		#prints cats , dogs , parrots

activities = ['walk','talk','sleep']
doing = 'ing , '.join(activities)
print(doing)	#prints walking , talking , sleep	#Note that 'sleep' stayed 'sleep'


print('\n'.join(['cats','dogs','parrot']))

''' 
prints:
cats
dogs
parrots
'''
#split : when you have to split a string into list

animals = pets.split()
print(animals)		#prints ['cats', ',', 'dogs', ',', 'parrot']

#By default it splits on white space characters
#But we can make it split based on other characters also

animals = pets.split(',')
print(animals)	#prints ['cats ', ' dogs ', ' parrot']

text = pets.split('a')
print(text)		#prints ['c', 'ts , dogs , p', 'rrot']

'''
l = [1,2,'abc']
n = l.join()		#error: list object has no attribute join
#this is because join() works only for list of strings
'''

#ljust() , rjust()	: returns left-justified , right-justified string respectively
a = 'Hello'.rjust(10)
print(a)		#prints Hello
print(len(a))	#prints 10

a = 'Hello'.rjust(10,'*')
print(a)	#prints *****Hello


#center()	: center justified

b = 'Hello'.center(10,'*')
print(b)	#prints **Hello***

#strip()  , rstrip()  , lstrip()	: to strip some characters from a sides of a string

b = b.strip('*')
print(b)		#prints 'Hello'

a = a.lstrip('*')
print(a)		#prints 'Hello'

print('spamspamchessspamcarromspamspam'.strip('amps'))	#Note that I passed 'amps', i could pass characters in any order. it does not matter. it will remove all those characters
#prints chessspamcarro
#also note that strip() , strips from both left and right side but did not remove from the middle of the string


#replace()

spam = 'Hello there'
spam = spam.replace('e','xyz')

print(spam)			#prints Hxyzllo thxyzrxyz

