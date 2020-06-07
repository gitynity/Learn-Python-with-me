# all() and any() take list as arguements

nums = [1,2,3,4,5,6]

if all([i>5 for i in nums]):		#using list comprehensions
	print("All greater than 5")
else:
	print("Not all greater than 5")
	
if any([i>5 for i in nums]):		#using list comprehensions
	print("Atleast one is greater than 5")
else:
	print("None is greater than 5")
