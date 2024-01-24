import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

### Histogramas
# Dados
n = np.random.randn(100000)

# Cria os subplots
fig, axes = plt.subplots(1,2, figsize=(12,4))

# Plot1
axes[0].hist(n)
axes[0].set_title('Histograma Padrão')
axes[0].set_xlim((min(n), max(n)))

# Plot2
axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title('Histograma Cumulativo')
axes[1].set_xlim((min(n), max(n)))
plt.show()

### Gráficos 3D
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Dados
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

# Função para um mapa de cores
def ColorMap(phi_m, phi_p):
    return(+ alpha - 2 * np.cos(phi_p)*cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p))

# Mais dados
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
x,y = np.meshgrid(phi_p, phi_m)
z = ColorMap(x,y).T

# Cria a Figura
fig = plt.figure(figsize=(14,6))

# Adiciona o subplot 1 com projeção 3D
ax = fig.add_subplot(1,2,1, projection='3d')
p = ax.plot_surface(x,y,z, rstride=4, cstride=4, linewidth=0)

# Adiciona o subplot2 com projeção 3D
ax = fig.add_subplot(1,2,2, projection='3d')
p = ax.plot_surface(x,y,z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Cria a barra de cores como legenda
cb = fig.colorbar(p, shrink=0.5)
plt.show()