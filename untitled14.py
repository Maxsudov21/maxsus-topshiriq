# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_kujLpQOizor2QN2ruBbsySHURVdBfkT
"""

import matplotlib.pyplot as plt
import numpy as np
# make data
x = np.linspace(0, 10, 100)
print(x)
y = 4 + 2 * np.sin(2 * x)
print (y)
#plot
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
plt.show

import matplotlib.pyplot as plt
import numpy as np
x= np.array([0,1,2,3,4,5])
y= np.array([0,2,8,1,14,7])
plt.scatter(x,y,color='red')
x= np.array([12,6,8,11,8,3])
y= np.array([5,6,3,7,17,19])
plt.scatter(x,y,color='green')
plt.show()