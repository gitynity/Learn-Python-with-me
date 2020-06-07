message = 'My telephone number is : 0761-2602998'
#How to extract my phone-number from this given message

import re	#regular expression

formula = re.compile(r'\d\d\d\d-\d\d\d\d\d\d\d')		#  /d is the regex for a numeric digit character
mo = formula.search(message)
print(mo.group())		#prints 0761-2602998

print(type(formula))	#prints <type '_sre.SRE_Pattern'>	: means that it is a regex-object

print(type(mo))		#prints <type '_sre.SRE_Match'>	: means that it is a match-object

print(type(mo.group()))		#prints <type 'str'>	: means it is of type string

#Now if we have a message which has more than one phone-numbers
message2 = 'My numbers are : 7441189789 , 7612602998'

regexphonenumber = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
mo = regexphonenumber.findall(message2)
print(mo)	#prints ['7441189789', '7612602998']

'''

Regular expressions are mini-language for specifying text-patterns. 
Writing code to do pattern matching without regular expressions is a huge pain.

Regex strings often use  backslash '\' (example:\d) , so they are often raw strings.

Steps to working with regular expressions:
.Import the re module
.Call the re.compile() function to create a regex object
.Call the regex objects search() method to create a match object 
.Cal the match object's group() method to get the matched string


'''
