import numpy as np
import matplotlib.pylab as plt
import random

N = 10**5

xk = np.loadtxt("valores.txt")
delta = 1

def probabilidad (sigma, xk):
    return (1/(sigma*(np.pi*2)**(1/2)))*np.exp(-xk**2/(2*sigma**2))
def todas(xk,sigma):
    a = [probabilidad(sigma,k) for k in xk]
    b = 1
    for i in a:
        b*=i
    return b

sigma = [random.random()]
for i in range(1, N):
    propuesta = sigma[-1] + (random.random()-0.5)*delta
    r = min(1, todas(xk, propuesta)/ todas(xk,sigma[-1]))
    alpha = random.random()
    if(alpha < r):
        sigma.append(propuesta)
    else:
        sigma.append(sigma[-1])

plt.hist(sigma, normed = True)
plt.savefig("sigma.png")
    