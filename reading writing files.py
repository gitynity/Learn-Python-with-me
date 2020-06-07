#reading text as written in the file

somefile = open('reading writing files.py')		#opened in read mode
text = somefile.read()							#stored file contents in text  variable
print(text)
somefile.close()

#reading text in the form of lists

somefile = somefile = open('reading writing files.py')
listtext = somefile.readlines()					#readlines() returns a list of string , whereas read() returns a single string
print(listtext)
somefile.close()

#appending to a file

somefile = open('reading writing files.py','a')
somefile.write('\nsomefile.close()		#this is appended text')	#write() returns the number of characters it wrote to the file

somefile.close()		#this is appended text

import os
print(os.getcwd())

import shelve			#used to store key-value pairs in files , like a dictionary

#The shelve module can store python values in a binary file

somefile = shelve.open('mydata.shelve')
somefile['cats'] = ['zophie' , 'pooka' , 'simon' , 'cleo']
somefile['dogs'] = ['alpha' , 'beta' , 'gama' , 'mona' , 'darling']
somefile.close()

somefile = shelve.open('mydata.shelve')

print(list(somefile.keys()))		#have to be conerted to list to view these keys
print(list(somefile.values()))		#have to be conerted to list to view these values


print('cats = ',somefile['cats'])
print('dogs = ',somefile['dogs'])



somefile.close()


somefile.close()		#this is appended text
somefile.close()		#this is appended text

#changing current working directory
os.chdir('/home/ubuntu/Documents/Programmes')
