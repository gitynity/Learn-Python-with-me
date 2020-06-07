def hello(name):
	print("hello",name)

hello(input())	#arguement passed as string by built-in input() function

def getage(age):
	print("You will be",age+1,"years old next year")

getage( int( input() ) )

def add(num1 , num2):
	return num1+num2
ans = add(int(input()) , int(input()) )
print(ans)
