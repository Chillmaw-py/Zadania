import math
import random
from scipy import stats
import numpy as np
#Generator liczb pseudolosowych dla rozkładu jednostajnego(metoda middle square random)
seed = 88888
num_digits = 40
def middle_square_random_generator(seed:int, n: int) -> int: #Middle-square method
    x = []
    length = len(str(seed))//2
    for _ in range(n):
        seed_sq = seed**2
        y = len(str(seed_sq))//2
        rint = int(str(seed_sq)[y-length:y+length])
        x.append(rint)
        seed = rint
    return x


random_numbers = middle_square_random_generator(seed,100)
####
print("Middle-square method")
print("Test Shapiro-Wilka")
x = middle_square_random_generator(seed,100)
s = stats.shapiro(x)
if not s.pvalue < 0.05:
    print("Nie ma podstaw do odrzucenia H0")
else:
    print("Są podstawy do odrzucenia H0")
print("Test ChiSquared")
c = stats.chisquare(np.histogram(x)[0])
if s.pvalue < 0.05:
    print("Nie ma podstaw do odrzucenia H0")
else:
    print("Są podstawy do odrzucenia H0")


# Generator liczb pseudolosowych dla rozkładu normalnego(Marsaglia polar method)
def marsaglia_polar_normal_distribution(n):
    random_numbers_1 = []
    random_numbers_2 = []
    for i in range(n):
        while True:
            u1 = random.uniform(-100, 100)
            u2 = random.uniform(-100, 100)
            s = u1 * u1 + u2 * u2
            if 0 < s <= 1:
                break

        factor = math.sqrt(-2 * math.log(s) / s)
        z1 = u1 * factor
        z2 = u2 * factor
        random_numbers_1.append(z1)
        random_numbers_2.append(z2)
    return random_numbers_1 , random_numbers_2


random_numbers = marsaglia_polar_normal_distribution(100)
#####
z1,z2 = marsaglia_polar_normal_distribution(100)

print("Marsaglia polar method")
print("Test Wilcox")
w = stats.wilcoxon(z1,z2)
if not w.pvalue < 0.05:
    print("Nie ma podstaw do odrzucenia H0")
else:
    print("Są podstawy do odrzucenia H0")

print("Test Shapiro-Wilka")
s = stats.shapiro(z1)
if not s.pvalue < 0.05:
    print("Nie ma podstaw do odrzucenia H0")
else:
    print("Są podstawy do odrzucenia H0")

print("Test Shapiro-Wilka")
s = stats.shapiro(z2)
if not s.pvalue < 0.05:
    print("Nie ma podstaw do odrzucenia H0")
else:
    print("Są podstawy do odrzucenia H0")