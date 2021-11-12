import random
random.seed(199110)
from scipy import stats
from scipy.test import expon
import math
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


x = []
x = [(random.random()) for i in range(100)]
print(x)  
stats.kstest(x, 'uniform')

y = - np.log(x)
print(y)
stats.kstest(y, 'uniform')
stats.kstest(y, 'expon')
##
y = y-1
N = 100
#ii = int(input("Enter i: "))
ii = 9
#l = int(input("Enter l: "))
l = 1
a = (N-ii)/l
M = math.floor(a-1)
S = []
SS = []
T = 1/(M+1)
for k in range(M):
    sx = x[ii+(k*l)] * x[ii+((k+1))*l]
    S.append(sx)
    sy = y[ii+(k*l)] * y[ii+((k+1))*l]
    SS.append(sy)

Rhox = (T * sum(S)) - 0.25
num = math.sqrt((13 * M) + 7)
den = 12 * (M + 1)
g = num/den
Z0x = Rhox / g
print(Z0x)

Rhoy = (T * sum(SS)) - 0.25
Z0y = Rhoy / g
print(Z0y)

plt.hist(y, density=True, bins=10, label="Data Frequency")
mean = 1
loc = 0
Exp = np.linspace(stats.expon.ppf(0.01, loc, mean), stats.expon.ppf(0.99, loc, mean), 100)
Exppdf = stats.expon.pdf(Exp, loc, mean)
plt.plot(Exp, Exppdf,label="PDF")
plt.legend(loc="upper right")
plt.ylabel("Frequency as Percentage")
plt.xlabel("Interval of Generated Numbers")
plt.title("Histogram")
plt.show()

QQ = sm.qqplot(y, stats.norm, line="45")
plt.title("Normal Probability Plot")
plt.show()
QQ = sm.qqplot(y, stats.expon, line="45")
plt.title("Exponential Probability Plot")
plt.show()