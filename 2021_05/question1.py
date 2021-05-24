import os
import sys
from PIL import Image

def compressMe(file, verbose=False):
	filepath = os.path.join(os.getcwd(), 'originalFiles', file)
	size = os.stat(filepath).st_size
	mb = round(size / (1024 * 1024), 3)
	max_mbs = 2.0

	picture = Image.open(filepath)
	


	if mb > max_mbs:
		ratio = (max_mbs/mb)
		print(ratio)


		quality = 85

		print('quality should be the following')
		print(quality)
	else:
		quality = 85
		
	#dim = picture.size
	
	#set quality= to the preferred quality. 
	#I found that 85 has no difference in my 6-10mb files and that 65 is the lowest reasonable number
	newPath = os.path.join(os.getcwd(), 'compressedFiles', 'compressed_' + file)
	picture.save(newPath,"JPEG",optimize=True,quality=quality)
	

	
	return 0

def main():
	verbose = False
	#checks for verbose flag
	if (len(sys.argv)>1):
		if (sys.argv[1].lower()=="-v"):
			verbose = True

	#finds present working dir
	pwd = os.path.join(os.getcwd(), "originalFiles")

	tot = 0
	num = 0
	#Seems like this is where it is looking initially? to run the process
	for file in os.listdir(pwd):
		print(file)
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
			num += 1
			#this is running the compressMe function
			tot += compressMe(file, verbose)
	print("Average Compression: %d" % (float(tot)/num))
	print("Done")

if __name__ == "__main__":
	main()