import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 501) #Grafik
ampl = np.exp(-x + 9)
#Contoh sinyal radio AM dengan cara fourier transform
y = np.sin((5*x) * 10) * ampl

plt.figure(figsize=(10,5))
plt.plot(x, y, label='sinyal')
plt.plot(x, ampl, ':', label='amplitude')
plt.xlabel('waktu')
plt.ylabel('nilai')
plt.legend()
plt.show()
