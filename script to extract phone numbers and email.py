import pyperclip , re
text = pyperclip.paste()


#email regex

emailregex = re.compile(r'''
[\w\d\+]+	#name
@	#@
[\w\d\+]+	#domain
''',re.VERBOSE)

emails = emailregex.findall(text)
emails = '\n'.join(emails)



#phone number regex

phoneregex = re.compile('''
(
(\d\d\d)	# first 3 digits
-			# -
(\d\d\d)	# second 3 digits
-			# -
(\d\d\d\d)	# 4 digits
)
''',re.VERBOSE)

mo = phoneregex.findall(text)

phonenumbers = []

for numbers in mo:
	phonenumbers.append(numbers[0])	#get the outermost group

phonenumbers = '\n'.join(phonenumbers)


result = phonenumbers + '\n' + emails


pyperclip.copy(result)
