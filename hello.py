import numpy as np
import cv2 as cv
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib as mpl


img_IR = cv.imread('PICIR13.jpeg')
img_REG = cv.imread('PICREG13.jpeg')

b_IR,g_IR,r_IR = cv.split(img_IR)
b_REG,g_REG,r_REG = cv.split(img_REG)

(h, w) = img_REG.shape[:2]


temp = np.zeros((h, w))
np.seterr(divide='ignore', invalid='ignore')
r_IR_TEMP = r_IR 
r_IR = r_IR.astype('int32') 
r_REG = r_REG.astype('int32') 

for x in range(h):
    for y in range(w):
        temp[x][y] = (r_IR[x][y] - r_REG[x][y]) / (r_IR[x][y] + r_REG[x][y])


# Make plot with vertical (default) colorbar
fig, ax = plt.subplots()


cax = ax.imshow(temp, interpolation='none', cmap=cm.viridis)
ax.set_title('NDVI')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
v1 = np.linspace(temp.min(), temp.max(), 3, endpoint=True)
cbar=plt.colorbar(cax, ticks=v1)              
cbar.ax.set_yticklabels(["{:4.2f}".format(i) for i in v1]) # add the labels


plt.show()

