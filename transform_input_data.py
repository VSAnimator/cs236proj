import os
import torch
import torchvision.transforms as transforms
import torchvision.transforms.functional as TF
from PIL import Image

# Experiment with pytorch rescaling
resize = transforms.Resize(int(256*1.12), Image.BICUBIC)
crop = transforms.RandomCrop(256)
pad = transforms.Pad(2)

for filename in os.listdir('./eval_cloudy_p2p'):
	pic = Image.open('./eval_cloudy_p2p/' + filename)
	newfile = filename[:-4]
	pic = resize(pic)
	pic = crop(pic)
	pic = pad(pic)
	pic.save('./eval_cloudy_p2p/' + newfile + '.png')
	
