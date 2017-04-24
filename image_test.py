import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('PNLB3990.png')
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img, cmap = 'nipy_spectral',clim = (0.0,0.7))
plt.colorbar()
plt.show()