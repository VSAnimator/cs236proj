import os
import csv
import glymur
import subprocess
import numpy as np
from PIL import Image

FNULL = open(os.devnull, 'w')
with open('sentinel_granules.csv', 'r') as f:
	reader = csv.reader(f)
	counter = 0
	for row in reader:
		counter += 1
		if(counter < 14000):
			continue
		base_url = row[0]
		complete_url = base_url + '/GRANULE/*/IMG_DATA/*TCI.jp2' 
		command = 'gsutil cp -r ' + complete_url + ' .'
		a = subprocess.call(command.split(' '), stdout = FNULL, stderr = subprocess.STDOUT)
		if(not a):
			print("Processed image " + str(counter))
			try:
				filename = os.popen('ls *.jp2').read()
				img = glymur.Jp2k(filename[:-1])
				thumbnail = img[::16, ::16]
				os.system('rm -rf ' + filename)

				def isWhite(x):
					if x[0] > 230 and x[1] > 230 and x[2] > 230:
						return 1
					return 0

				img = Image.fromarray(thumbnail, 'RGB')
				img.save('image' + str(counter) + '.jpg', "JPEG")
				filter = np.apply_along_axis(isWhite, 2, thumbnail)
				if((filter.sum()/filter.size) < 0.05):
					os.system('mv ' + 'image' + str(counter) + '.jpg ' + './notcloudy3')
				elif((filter.sum()/filter.size) <= 0.4):
					os.system('mv ' + 'image' + str(counter) + '.jpg ' + './cloudy3')
				# We are now tossing out all images with > 0.4 cloud
				else:
					os.system('rm ' + 'image' + str(counter) + '.jpg')
			except:
				continue
		
