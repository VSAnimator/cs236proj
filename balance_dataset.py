import os

count = 0
for filename in os.listdir('./PyTorch-CycleGAN/datasets/cloudy2notcloudy/train/A/'):
	if(count < 477):
		os.system('mv ./PyTorch-CycleGAN/datasets/cloudy2notcloudy/train/A/' + filename + ' ./cloudy_clean')
	count += 1
