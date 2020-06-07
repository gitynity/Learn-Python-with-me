def decorator(func):
	def wrap():
		print("=============")
		func()
		print("=============")
	return wrap
	
def print_hello():
	print("Hello world")

decorated = decorator(print_hello)
decorated()

#####################################################


@decorator							#using our readymade decorator with functions to modify/decorate them in a shortcut way
def print_name():
	print("Nityanand")
	
print_name()
	
	
