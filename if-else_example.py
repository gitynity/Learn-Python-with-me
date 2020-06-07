password = input("whats the password?")
if password=="swordfish":
	print("\nWelcome")
	name = input("\nWhat's your name?")
	if name:
		print("\nHi , " ,name)
	else:
		print("Okay Mr. anonymous!") 	
	age = int(input("\nWhat's your age?"))
	if(age<20):
		print("\nHi kiddo!")
	elif(age>20 and age<40):
		print("\nHi young person")
	else:
		print("\nHi oldie")
else:
	print("\nNO")
