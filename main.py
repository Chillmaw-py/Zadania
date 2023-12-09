from scipy.stats import skew
import numpy as np
import matplotlib.pyplot as plt
min = -1
max = 1
size = 100
u = np.random.uniform(min,max,size)
n = np.random.normal(min,max,size)
srednia_uniform = sum(u)/size
srednia_normal = sum(n)/size
mediana_uniform = np.median(u)
mediana_normal = np.median(n)
wartosc_oczekiwana_uniform = (min+max)/2
wartosc_oczekiwana_normal = (min+max)/2
skosnosc_uniform = print(skew(u))
skosnosc_normal = print(skew(n))
#histogram rozkładu jednostajnego
plt.hist(u)
plt.title("Rozkład jednostajny")
plt.axvline(x=srednia_uniform, color='r', linestyle='dashed', linewidth=2, label='Średnia')
plt.axvline(x=mediana_uniform, color='g', linestyle='dashed', linewidth=2, label='Mediana')
plt.axvline(x=wartosc_oczekiwana_uniform, color='k', linestyle='dashed', linewidth=2, label='Wartość oczekiwana')
plt.legend()
plt.show()
#histogram rozkładu normalnego
plt.hist(n)
plt.title("Rozkład normalny")
plt.axvline(x=srednia_normal, color='r', linestyle='dashed', linewidth=2, label='Średnia')
plt.axvline(x=mediana_normal, color='g', linestyle='dashed', linewidth=2, label='Mediana')
plt.axvline(x=wartosc_oczekiwana_normal, color='k', linestyle='dashed', linewidth=2, label='Wartość oczekiwana')
plt.legend()
plt.show()

