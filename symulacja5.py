import numpy as np
import matplotlib.pyplot as plt
def f(x): return x**2
def g(x): return np.sqrt(x)
dziedzina = np.linspace(0,10,1000)
wartosci_f = list(map(f,dziedzina))
wartosci_g = list(map(g,dziedzina))
Max = max((max(wartosci_f),max(wartosci_g)))
n = 1000 #ilość punktów
punkty = list(zip(np.random.uniform(0,10,n),np.random.uniform(0,Max,n)))
suma = 0
for x,y in punkty:
    if (y<=f(x) and y>=g(x)) or (y>=f(x) and y<=g(x)):
        suma += 1
print(suma/n)

plt.plot(dziedzina,wartosci_f)
plt.plot(dziedzina,wartosci_g)

for x,y in punkty[0:1000]:
    plt.plot(x,y,marker='o', linestyle='none')
plt.show()


