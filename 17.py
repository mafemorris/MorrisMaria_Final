import numpy as np
import matplotlib.pylab as plt

t05 = np.loadtxt("solucion.txt")
t0 = np.loadtxt("condicion.txt")

plt.figure()
plt.plot(np.linspace(0,2,len(t0)), t0, label= "Condicion Inicial")
plt.plot(np.linspace(0,2,len(t0)), t05, label = "t = 0.5s")
plt.legend()
plt.savefig("resultado.png")