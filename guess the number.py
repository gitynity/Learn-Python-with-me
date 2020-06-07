import random
name = ("Hello there, Whats  your name?")
print("Hi",name,"I am thinking of a number between 1 and 100. Can you guess the number in 6 tries?")
print("Okay, lets start")
num = random.randint(0,100)
count = 0
while count<=6:
	guess = int( input() )
	count=count+1
	if guess>num:
		print("You guessed too high")
	elif guess<num:
		print("You guessed too low")
	if guess == num:
		print("You guessed in",count,"times")
		break
if guess!=num:
	print("You could not guess it.The number i was thinking was",num)
