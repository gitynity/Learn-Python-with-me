# itertools is a standard library that contains several functions that are useful in functional programming

#Example: The function count() counts up infinitely from a value
#		  The function cycle() infinitely iterates through an iterable(for instance : a list or a string)
#		  The function repeat() repeats an object , either infinitely or a specified number of times
#		  The function takewhile() takes items from an iterable while a predicate function remains true
#		  The fucntion chain() combines several iterables into one long one
#		  The function accumulate() returns a running total of the values in an iterable

from itertools import count , repeat , cycle , takewhile , chain , accumulate

import time

for i in count(5):
	if i == 11:
		break
	print(i)

t0 = time.clock()				#cpu-time before this function starts
for i in cycle("hello"):
	print(i,end=" ")
	t1 = time.clock()			#cpu-time now
	if t1 - t0 > 2:
		break					#this function runs for 2 seconds

print(list(repeat("Good things",5)))

nums = list(accumulate(range(8)))
print(nums)						#[0, 1, 3, 6, 10, 15, 21, 28]


print(list(takewhile(lambda x:x<=6 , nums)))	# [0, 1, 3, 6]


odds = [1,3,5,7,9]
evens = [2,4,6,8]

nums = list(chain(odds,evens))
print(nums)						# [1, 3, 5, 7, 9, 2, 4, 6, 8]
