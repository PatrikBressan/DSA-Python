### Gráfico de Linha
# Pylab combina funcionalidades do Numpy com Pyplot
import matplotlib.pyplot as plt
from pylab import *

x = linspace(0,5,10)
y = x**2

# Cria a figura
fig = plt.figure()

# Define a escala dos eixos
axes = fig.add_axes([0, 0, 0.8, 0.8])

# Cria o plot
axes.plot(x,y,'r')

# Labels e título
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')
plt.show()


# Gráficos de linha com duas figuras
x = linspace(0,5,10)
y = x ** 2

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

# Figura principal
axes1.plot(x,y,'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('Figura Principal')

# Figura secundária
axes2.plot(y,x,'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('Figura Secundária')
plt.show()

