import os
from PIL import Image
import numpy as np
from skimage import color
from skimage import data

# RUN ON HSV IMAGE
def isBlue(x):
    # Just check hues
    # Cyan and Blue are 201 to 240 degrees. We are setting 210 to 235
    if (x[0] > 210/360.) and (x[0] < 235/360.):
        return 1
    return 0

count = 0
for filename in os.listdir('./cloudy2'):
	pic = Image.open("./cloudy2/" + filename)
	pix = np.array(pic)
	img_hsv = color.rgb2hsv(pix)
	blueFilter = np.apply_along_axis(isBlue, 2, img_hsv)
	if((blueFilter.sum()/blueFilter.size) > 0.40):
		# Remove images with too much water
		os.system('mv ' + './cloudy2/' + filename + ' ./cloudy2_water')
count = 0
for filename in os.listdir('./notcloudy2'):
	pic = Image.open("./notcloudy2/" + filename)
	pix = np.array(pic)
	img_hsv = color.rgb2hsv(pix)
	blueFilter = np.apply_along_axis(isBlue, 2, img_hsv)
	if((blueFilter.sum()/blueFilter.size) > 0.40):
		# Remove images with too much water
		os.system('mv ' + './notcloudy2/' + filename + ' ./notcloudy2_water')

