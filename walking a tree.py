import os

#os.walk returns three values = foldername , subfolders , files
							   
						#		fodername is a string
						#		subfolders is a list of string
						#		files is a list of string
							   
#print(list(os.walk('.')))		# prints [('.', [], ['tcpdump.mp4', '1os module basics.mp4', 'copy and move files.py', 'delete files.py', '4deleting files.mp4', '5walking a tree (directory).mp4', 'walking a tree.py', 'reading writing files.py', 'mydata.shelve', '2reading and writing plain text fles.mp4', '3copy move files folders.mp4'])]
								#current directory has zero subfolders

os.chdir('/home/ubuntu/Documents/Programmes')
#rint(list(os.walk('.')))		#gives a messy list

#How to use this os.walk() so that it makes sense?

#Ans: Use loop

for foldername , subfolders , files in os.walk('/home/ubuntu/Documents/Programmes'):
	print('The folder is',str(foldername))
	print(foldername,'has folder',str(subfolders))
	
	for filenames in files:
		if filenames.endswith('.py'):
			print(foldername,'has python files',filenames)
	print()

#os.walk() can be used to delete/modify some specific files in a folder which has too many subfolders and too many subfiles. Also each subfolder may have its own subfoders and subfiles. 
