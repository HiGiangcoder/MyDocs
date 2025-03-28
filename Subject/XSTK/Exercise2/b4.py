import numpy as np

# np.pi np.e

def Laplace(x):
    res = 0
    numrep = 10**7
    dt = x / numrep
    for i in range(numrep):
        t = i * dt
        f = np.e ** (-t * t / 2)
        res += f * dt
        
    res /= np.sqrt(2 * np.pi)
    return res
        
print(Laplace(1.96))