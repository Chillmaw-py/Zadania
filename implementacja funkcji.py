
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,10,1000)
def f(x):
    if x >= -5 and x < 1/3:
        return 3*x + 15
    elif x >= 1/3 and x <= 9:
        return np.sqrt(10*x) + 10
    elif x > 9 and x <= 10:
        return x**2 + x + 1
lista_argumenty = []
for argument in x:
    lista_argumenty.append(f(argument))
plt.plot(x,lista_argumenty)
plt.show()