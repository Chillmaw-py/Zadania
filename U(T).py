import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
data = np.rot90(np.loadtxt('dane.txt'))

plt.errorbar(data[3], data[1], xerr=data[2], yerr=data[0], color='black', marker='o', linestyle='none', markersize=3)
plt.xlabel('T(C)')
plt.ylabel('U(mV)')
plt.show()


plt.show()