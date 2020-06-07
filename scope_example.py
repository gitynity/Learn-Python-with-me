def spam():
	global eggs	#access global eggs in this function
	eggs = "Hello"	#global eggs assigned "Hello"
	print(eggs)

eggs = 42	#global eggs

spam()

print(eggs)	#prints global eggs

#How to access both global and local variable in a python function?
#Ans: using a in built function called globals()

def somefunction():
	a = 5	#local variable
	print(a)	#prints local variable
	globals() ['a'] = 15 #access & modifies global variable


a = 10

somefunction()

print(a)	#prints global variable
