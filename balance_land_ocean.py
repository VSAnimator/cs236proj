import os
from PIL import Image
import numpy as np

def isOcean(x):
    if x[0] > 230 and x[1] > 230 and x[2] > 230:
        return 1
    return 0

# EDIT ALL FILE PATHS TO APPROPRIATE LOCATIONS

count = 0
for filename in os.listdir('./PyTorch-CycleGAN/datasets/cloudy2notcloudy/train/A'):
	pic = Image.open("./PyTorch-CycleGAN/datasets/cloudy2notcloudy/train/A/" + filename)
	pix = np.array(pic)
	whiteFilter = np.apply_along_axis(isWhite, 2, pix)
	if((whiteFilter.sum()/whiteFilter.size) > 0.40):
		# Remove images with too much white
		os.system('mv ' + './PyTorch-CycleGAN/datasets/cloudy2notcloudy/train/A/' + filename + ' ./cloudy')

