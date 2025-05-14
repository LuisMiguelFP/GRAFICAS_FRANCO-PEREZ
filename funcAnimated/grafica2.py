import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración inicial
num_points = 50  # Número de partículas
x = np.random.rand(num_points) * 10  # Coordenadas iniciales en X
y = np.random.rand(num_points) * 10  # Coordenadas iniciales en Y

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # Límites del eje X
ax.set_ylim(0, 10)  # Límites del eje Y
ax.set_title("Partículas moviéndose aleatoriamente")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Crear el gráfico de dispersión (scatter)
scatter = ax.scatter(x, y, color='blue')

# Función de actualización
def update(frame):
    global x, y
    x += (np.random.rand(num_points) - 0.5)  # Movimiento aleatorio en X
    y += (np.random.rand(num_points) - 0.5)  # Movimiento aleatorio en Y
    scatter.set_offsets(np.c_[x, y])  # Actualizar posiciones
    return scatter,

# Crear la animación
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Guardar como GIF (opcional)
ani.save("puntos_aleatorios.gif", writer="pillow", fps=60)

# Mostrar la animación
plt.show()