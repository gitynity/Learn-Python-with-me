open('newfile.txt','w')
print('newfile.txt created')

#permannent delete

import os
os.unlink('newfile.txt')		#os.unlink() delets a single file permanently
print('newfile.txt permanently deleted')


os.mkdir('/home/ubuntu/New folder')	#create new folder

#permanently delete an empty folder
os.rmdir('/home/ubuntu/New folder')


os.mkdir('/home/ubuntu/New folder')	#create new folder
os.system('cd ~/"New folder" && touch a.txt b.txt c.txt')

#permanently delete a folder which is not empty

import shutil
shutil.rmtree('/home/ubuntu/New folder')	#permanently deleted


#How to not permanently delete files folders and send them to trash

import send2trash
send2trash.send2trash('tcpdump.mp4')
os.mkdir('newfolder')
send2trash.send2trash('newfolder')
