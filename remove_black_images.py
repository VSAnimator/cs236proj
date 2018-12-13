import os
from PIL import Image
import numpy as np

def isBlack(x):
    if x[0] < 20 and x[1] < 20 and x[2] < 20:
        return 1
    return 0

def isBlack2(x):
    a,b,_ = x.shape
    return (isBlack(x[0,0,:]) + isBlack(x[0,b-1,:]) + isBlack(x[a-1,0,:]) + isBlack(x[a-1,b-1,:]) > 0)


count = 0
for filename in os.listdir('./cloudy3'):
	pic = Image.open("./cloudy3/" + filename)
	pix = np.array(pic)
	if(isBlack2(pix)):
		os.system('mv ' + './cloudy3/' + filename + ' ./cloudy3_black')

