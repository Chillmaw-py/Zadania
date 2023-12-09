import random
import numpy as np
import matplotlib.pyplot as plt
teta = .5
teta2 = 50
n = 20
x_lim = 100

noise = np.random.normal(0, teta*2, n)
dane = np.random.uniform(1, x_lim, n)
y = dane*teta + noise + teta2

plt.plot(dane, y, marker = 'o', linestyle ='none')


avg_x = np.average(dane)
avg_y = np.average(y)

teta = sum(dane*y)/sum(dane**2)

a = (-(avg_y*sum(dane)) + sum(dane*y))/((1 - avg_x*sum(dane))*sum(dane*dane))
b = sum(a*dane-y)/n

print((avg_x*avg_y/n))
print(sum(dane*y))

print(a*dane-y)


print(teta)
print(a, b)

punkty = np.linspace(1,x_lim,n)

plt.plot(punkty, punkty*teta, label="teta*x")
plt.plot(punkty, punkty*a+b, label="ax+b", color="red")

plt.show()