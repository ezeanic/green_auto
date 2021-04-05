import csv
import numpy as np
import pandas as pd
from pandas import read_csv
from numpy import isnan
from numpy import genfromtxt
import matplotlib.pyplot as pl
from matplotlib.pyplot import plot
from math import cos


in_filename = '02-24-21-Trip1 - Copy.csv'

def cleanIt(in_filename = 'Data.csv'):
    with open(in_filename, 'r') as input:
        data = list(csv.reader(input))
        res = []
        for i in range(1, len(data)):
            row = data[i][1:]
            if row != data[i-1][1:]:
                try:
                    d = list(map(float, data[i]))
                    if len(d) == 7:
                        res.append(d)
                except:
                    continue
    return (data[0],res)

def getAccel(sp, t):
    ds = sp-sp.shift(1)
    dt = t-t.shift(1)
    res = (ds/dt)
    res[0] = 0
    return abs(res),dt

def getPerc(a,t, n = 5):
    res = 0.0
    for i in t.index[:-1]:
        if a[i] > n:
            res += t[i]

    return res/t.sum() * 100

def plotPercFiltered(t, a, n = 0.5):
    step = t.index.step
    temp = a.ge(n)
    i = 0

    while i < t.size - 2 * step:

        if temp[i] == True:
            start = i
            while temp[i] == True and i < t.size-step:
                i += step
            end = i
            pl.axvspan(t[start], t[end], color = 'g', alpha = .5)
        else:i+= step

c, p = cleanIt(in_filename)
d = pd.DataFrame(p, columns = c)

t = d.time
sp = d.speed

a,dt = getAccel(sp, t)

plot(t, sp)
plot(t, a)
plotPercFiltered(t, a)
print(getPerc(a,t))