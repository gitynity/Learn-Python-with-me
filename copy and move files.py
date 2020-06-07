import shutil
import os
src = os.path.abspath('copy and move files.py')

#copying a file

shutil.copy(src,'/home/ubuntu/')
shutil.copy(src,'/home/ubuntu/copiedfile.py')

#copying an entire folder

shutil.copytree('/home/ubuntu/Documents/Programmes/Python' , '/home/ubuntu/Python_Programmes')

#moving a file

src = os.path.abspath('/home/ubuntu/tcpdump.mp4')
dst = os.path.abspath('.')							#	. = current directory	.	..  = previous directory
shutil.move(src,dst)

#rename a file

shutil.move('./tcpdump.mp4' , './tcpdump_renamed.mp4')
shutil.move('./tcpdump_renamed.mp4' , './tcpdump.mp4')

