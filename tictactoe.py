theboard = {'top-l':'' , 'top-m':'' , 'top-r':'' , 'mid-l':'' , 'mid-m':'' , 'mid-r':'' , 'low-l':'' , 'low-m':'' , 'low-r':'' }

import pprint
pprint.pprint(theboard)

def board_print():
	pprint.pprint(theboard['top-l'] + '|' + theboard['top-m'] + '|' + theboard['top-r'] )
	pprint.pprint('--')
	pprint.pprint(theboard['mid-l'] + '|' + theboard['mid-m'] + '|' + theboard['mid-r'] )
	pprint.pprint('--')
	pprint.pprint(theboard['low-l'] + '|' + theboard['low-m'] + '|' + theboard['low-r'] )

board_print()

for i in range(9):
	symbol = str(input("Chose your symbol , x or o" ))
	pos = str(input('Select position from: top-l , top-m , top-r , mid-l , mid-m , mid-r , low-l , low-m , low-r' ))
	theboard[pos] = symbol
	board_print()
