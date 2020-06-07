import re

batRegex = re.compile(r'Bat(wo)?man')	# ? : means previous group may appear zero or once

mo = batRegex.search('the adventures of Batman')
print(mo.group())	#prints Batman

mo = batRegex.search('the adventures of Batwoman')
print(mo.group())	#prints Batwoman

batRegex = re.compile(r'Bat?man')		# t may appear 1 or 0 times
mo = batRegex.search('the adventures of Batman')
print(mo.group())


batRegex = re.compile(r'(Bat){3}man')		# Bat has to appear exactly 3 times
mo = batRegex.search('the adventures of BatBatBatman')
print(mo.group())


batRegex = re.compile(r'(Bat){0,3}man')		# Bat may appear 0 to 3 times			Greedy
mo = batRegex.search('the adventures of BatBatBatman')
print(mo.group())														#prints BatBatBatman


batRegex = re.compile(r'(Bat){0,3}?man')		# Bat may appear 0 to 3 times		'?' made it non-greedy
mo = batRegex.search('the adventures of man and Batman and BatBatBatman')
print(mo.group())														#prints man

batRegex = re.compile(r'(Bat)*man')
mo = batRegex.findall('the adventures of man and Batman and BatBatBatman')
print(mo)		#prints ['', 'Bat', 'Bat']	Why?	:	Read about non-capturing groups and findall() function




'''

? says previous group should occur 0 or 1 times
* says previous group should occur 0 or more times
+ says previous group should occur 1 or more times

{n} says previous group should appear exactly n times
{0,n} says previous group should appear atmost n times
{n,} says previous group should appear atleast n times

Greedy matching matches the longest string possible , non-greedy matching matches the shortest group possible

Putting a ? after {a,b} makes it do a non-greedy matching

'''

