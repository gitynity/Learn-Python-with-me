#         #
# #     # #
#  #   #  #
#   # #   #
#    #    # APPING

def multiply2(x):
	return x*2


def mapping(nums):					#Note: Don't use () after function name in map and filter statements
	even = map(multiply2 , nums)	#using function and list ; list is iterable
	return even

l = [1,2,3,4,5,6]
	
ans = mapping(l)
print(list(ans))


def mapping_again(nums):
	even = map(lambda x:x*2 , nums)		#using lambda and list
	return even

ans = mapping_again(l)
print(list(ans))



#########
#
######
#
#        ILTERING




def detect_even(x):
	if x%2==0:
		return True
	else:
		return False

def filtering(nums):
	even = filter(detect_even , nums)
	return even

ans = filtering([1,2,3,4,5,6])
print(list(ans))

def filtering_again(nums):
	even = filter(lambda x:x%2==0 , nums)
	return even

ans = filtering_again([1,2,3,4,5,6])
print(list(ans))


