import numpy as np
from scipy.stats import wilcoxon
#1
#Rozkład normalny:
x = np.random.normal(loc=0, scale=10, size=100).astype(int)
#Rozkład normalny:
y = np.random.normal(loc=10, scale=20, size=100).astype(int)
Min = min((min(x),min(y)))
Max = max((max(x),max(y)))
suma = 0
for i in range(Min,Max+1):
    P = np.count_nonzero(x == i)
    Q = np.count_nonzero(y == i)
    if Q != 0 and P != 0:
        suma += P*np.log(P/Q)
print("Kullback–Leibler divergence")
print(suma)
#2 Metoda Monte Carlo
def f(x): return x**2
przedzial = np.linspace(0,10,100)
wartosci = []
for x in przedzial:
    wartosci.append(f(x))
wysokosc = max(wartosci) # wsp y
szerokosc = 10 #wsp x
n = 1000
wsp_x = np.random.uniform(0,szerokosc,n)
wsp_y = np.random.uniform(0,wysokosc,n)
p = zip(wsp_x, wsp_y)
suma = 0
for x,y in p:
    if y<f(x):
        suma += 1
Pole = wysokosc*szerokosc*suma/n
print(Pole)
#3 metoda riemanna
dx = 0.001
punkty = [dx*i for i in range(int(10/dx))]
suma = 0
for punkt in punkty:
    wysokosc = f(punkt)
    suma += wysokosc*dx
print(suma)
#4
print("Test Wilcoxona")
w = wilcoxon([Pole], [suma])
print(w)
if not w.pvalue < 0.05:
    print("Nie ma podstaw do odrzucenia H0")
else:
    print("Sa podstawy do odrzucenia H0")







