#Due to the fact that they yield one item at a time , generators don't have the memory restrictions of lists.

def my_fun():
	for i in range(5):
		yield i*i

for i in my_fun():
	print(i)
	
print(list(my_fun()))

def infinite_sevens():
	while True:
		yield 7

for i in infinite_sevens():
	print(i)			  #keeps printing 7 infinite times , by yielding one 7 at a time
