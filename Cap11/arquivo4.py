import matplotlib.pyplot as plt
from pylab import *

### Gráficos de linha com diferentes escalas
x = linspace(0,5,10)
y = x ** 2

# cria os subplots
fig, axes = plt.subplots(nrows=1,ncols=2, figsize=(10,4))

# Cria o plot1
axes[0].plot(x, x**2, x, exp(x))
axes[0].set_title('Escala Padrão')

# Cria o plot2
axes[1].plot(x, x**2, x, exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logarítmca (y)')
plt.show()

### Grid
x1 = linspace(0,5,10)
y1 = x ** 2

# cria os subplots
fig, axes = plt.subplots(1,2, figsize=(10,3))

# Grid padrão
axes[0].plot(x1, x1**2, x1, x1**3, lw=2)
axes[0].grid(True)

# Grid customizado
axes[1].plot(x1, x1**2, x1, x1**3, lw=2)
axes[1].grid(color='b', alpha=0.7, linestyle='dashed', linewidth=0.8)
plt.show()

### Diferentes estilos de Plots
# Dados
xx = np.linspace(-0.75, 1., 100)
n = np.array([0,1,2,3,4,5])

# Subplots
fig, axes = plt.subplots(1, 4, figsize=(12,3))

# Plot1
axes[0].scatter(xx, xx+0.25*randn(len(xx)), color='black')
axes[0].set_title('Scatter')

# Plot2
axes[1].step(n, n**2, lw=2, color='blue')
axes[1].set_title('Step')

# Plot3
axes[2].bar(n, n**2, align='center', width=0.5, alpha=0.5, color='magenta')
axes[2].set_title('Bar')

# Plot4
axes[3].fill_between(x, x**2, x**3, alpha=0.5, color='green')
axes[3].set_title('Fill Between')
plt.show()

