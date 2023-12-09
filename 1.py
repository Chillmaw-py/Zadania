from scipy.stats import skew
import numpy as np
import matplotlib.pyplot as plt
r=input("Enter number:\n")
l=len(str(r))
list = []
while len(list) == len(set(list)) :
    x=str(r*r)
    if l % 2 == 0:
        x = x.zfill(l*2)
    else:
        x = x.zfill(l)
    y=(len(x)-l)/2
    r=int(x[y:y+l])
    list.append(r)
    print r

