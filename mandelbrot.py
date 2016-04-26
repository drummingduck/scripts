import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def mandelbrot( h, w, maxit = 20):
	#Returns a 2d array w x h with number of iteration till divergence
	y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
	c = x + y * 1j
	z = c
	divtime = maxit + np.zeros(z.shape, dtype = int)

	for i in range(maxit):
		z = z**2 + c
		diverge = z*np.conj(z) > 2**2
		div_now = diverge & (divtime==maxit)
		divtime[div_now] = i
		z[diverge] = 2

	return divtime



fig1 = plt.figure(frameon=False)



ims = []

for i in range(25):
	im = plt.imshow(mandelbrot(1000,1000,i))
	cur_axes = plt.gca()
	cur_axes.axes.get_xaxis().set_visible(False)
	cur_axes.axes.get_yaxis().set_visible(False)
	ims.append([im])
reversed_arr = ims[::-1]
imsf = ims + reversed_arr


im_ani = animation.ArtistAnimation(fig1, imsf, interval=70, repeat_delay=3000,
    blit=True)
im_ani.save('mandelbrot.gif', writer='imagemagick')


import os
os.system("open -a 'Google Chrome' mandelbrot.gif")
