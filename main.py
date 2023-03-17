from math import *
from scipy.misc import derivative
from numpy import linspace
import csv

def f(x):
    return x**2 + log(x)

def diff_func(x):
    return 2*x + 1/x

def polinom(x, n, arrayXValues):
    sum = 0
    for i in range(n):
        val = f(arrayXValues[i])
        val1 = 1
        for j in range(n):
            if i != j:
                val1 *= ((x - arrayXValues[j]) / (arrayXValues[i] - arrayXValues[j]))
        sum += (val * val1)
    return sum

def absoluteError(x, n, arrayXValues):
    return abs(polinom(x, n, arrayXValues) - f(x))

def relativeError(x, n, arrayXValues):
    return ((absoluteError(x, n, arrayXValues) / abs(f(x))) * 100)

def remainder(x, n, a, b):
    return (abs(derivative(diff_func, x, n=n, order =n + 2)) / factorial(n + 1)) * ((b - a) ** (n + 1))



arrN = [3, 5, 15, 33, 55, 81]
arrVal = [0.52, 0.42, 0.87, 0.67]
a = 0.4
b = 0.9

with open('TableOut.csv', 'w') as file:
    writer = csv.writer(file, delimiter=";", lineterminator='\n')
    for x in arrVal:
        print("Таблица для x = ", x)
        naming = ["n", "absoluteError", "relativeError", "remainder"]
        writer.writerow(naming)
        print("n", "absoluteError", "relativeError", "remainder")
        for n in arrN:
            arrXValues = linspace(a, b, num=n)
            res = [n, absoluteError(x, n, arrXValues), relativeError(x, n, arrXValues), remainder(x, n, a, b)]
            writer.writerow(res)
            print(res[0], res[1], res[2], res[3])



        
