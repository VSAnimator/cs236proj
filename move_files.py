import os

count = 1
for filename in os.listdir('./eval_cloudy_p2p'):
	os.system('mv ./eval_cloudy_p2p/' + filename + ' ./eval_cloudy_p2p/' + str(count).zfill(4) + '.jpg')
	count+=1
