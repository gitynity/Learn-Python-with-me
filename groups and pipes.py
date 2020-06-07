message = 'My telephone number is 0761-2602998'

import re
formula = re.compile('\d{4}-\d{7}')		# regex{n} = how many times that regex pattern appears in the message
mo = formula.search(message)
print(mo.group())


formula = re.compile('(\d{4})-(\d{7})')	#I have created two groups here by using () to separate them
mo = formula.search(message)

std_code = mo.group(1)		#first group
number = mo.group(2)		#second group

print("stdcode = %s and number = %s" %(std_code , number) )


message = "Batman Batmobile Batcopter Batbat"

batregex = re.compile(r'Bat(man|mobile|car)')
mo = batregex.search(message)
print(mo.group())	#prints Batman
print(mo.group(1))	#prints man


#mo = batregex.findall(message)
#print(mo.group(0))		#Attributeerror: list object does not have a method named group()

'''

Groups are created in regex strings with paranthesis
The first set of paranthesis is group 1 , the second is group 2 , and so on.
Calling the group() or group(0) returns the full matching string , group(1) returns the group 1's matching string , and so on.
Use '\(' to match literal paranthesis in regex string.
The | i.e. pipe can match one of many possible groups.

'''
