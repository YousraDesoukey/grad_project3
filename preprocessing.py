import cv2
import numpy as np
from matplotlib import pyplot as plt
#
#
# img = cv2.imread('cartouche.jpg')
#
# hist,bins = np.histogram(img.flatten(),256,[0,256])
#
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max()/ cdf.max()
# plt.plot(cdf_normalized, color = 'b')
# plt.hist(img.flatten(),256,[0,256], color = 'r')
# plt.xlim([0,256])
# plt.legend(('cdf','histogram'), loc = 'upper left')
# plt.show()


img = cv2.imread('012.jpg', 0)

equ = cv2.equalizeHist(img)

#res = np.hstack((img, equ))  # stacking images side-by-side
cv2.imshow('result', equ)
cv2.imwrite('res.png', equ)
cv2.waitKey(0)