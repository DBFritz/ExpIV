import time
import picamera
import picamera.array
import numpy as np

with picamera.PiCamera() as camera:
    with picamera.array.PiBayerArray(camera) as stream:
        camera.capture(stream, 'jpeg', bayer=True)
        # Demosaic data and write to output (just use stream.array if you
        # want to skip the demosaic step)
        output = stream.array
	with open('image.txt', 'w') as f:
		for i in len(output[0::2, 0::2, 1])
			f.write(str(output[0::2, 0::2, 1, i,j]))
