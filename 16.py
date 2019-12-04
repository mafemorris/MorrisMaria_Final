import numpy as np
import matplotlib.pylab as plt

solares = np.loadtxt("monthrg.dat")
solares = solares[solares[:,0]>=1990]
anio = solares[:,0]
mes = solares[:,1]
dias = solares[:,2]
manchas = solares[:,3] #siempre hubo mediciones


N= len(manchas)

# def fourier(n,k,N):
#     return np.exp(-2*np.pi*1j*n*k/N)

def xk(lista):
    N=len(lista)
    lis = [0]*N
    for k in range(N):
        suma = 0
        for n in range(N):
            suma += np.exp(-2*np.pi*1j*n*k/N)*lista[n]
        lis[k]=abs(suma)
    return np.array(lis)/N

# fouri = [(1/N)*np.abs(sum([fourier(n,k,N)*manchas[n] for n in range(N)])) for k in range(N)]
xs = xk(manchas)
# for i in range(N):
#     plt.plot(manchas[i]*xs[i]*np.linspace(0,70,70))
plt.plot(np.arange(N), manchas, '-o', label = "Numero de manchas")
plt.stem(np.arange(N), xs, label = 'Transformada de Fourier')
plt.xlabel("tiempo(meses) desde 1990 hasta 1995")
plt.ylabel("cantidad de manchas")
plt.legend()
plt.savefig("solar.png")



