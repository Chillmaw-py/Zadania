import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

data = np.rot90(np.loadtxt('dane.txt'))

plt.errorbar(data[3], data[1], xerr=data[2], yerr=data[0], color='black', marker='o', markersize=3)

reg = linregress(data[3], data[1])
#plt.plot(data[3], reg.intercept + reg.slope*np.array(data[3]), color='black')

print(f"a = {reg.slope} +- {reg.stderr}")
print(f"b = {reg.intercept} +- {reg.intercept_stderr}")
plt.xlabel('T(C)')
plt.ylabel('U(mV)')

plt.show()