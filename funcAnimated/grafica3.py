import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)  # Límites del eje X
ax.set_ylim(-1.5, 1.5)  # Límites del eje Y
ax.set_title("Punto girando en un círculo")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Dibujar el círculo de referencia
circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--')
ax.add_artist(circle)

# Crear el punto que se moverá
point, = ax.plot([], [], 'ro')  # Punto rojo
trail, = ax.plot([], [], 'b-', lw=1)  # Cola azul (trayectoria)

# Inicializar la trayectoria
x_trail, y_trail = [], []

# Función de inicialización
def init():
    point.set_data([], [])
    trail.set_data([], [])
    return point, trail

# Función de actualización
def update(frame):
    t = frame * 0.1  # Incremento del ángulo
    x = np.cos(t)  # Coordenada X del punto
    y = np.sin(t)  # Coordenada Y del punto

    # Actualizar el punto
    point.set_data([x], [y])  # Convertir x e y en listas

    # Actualizar la trayectoria (cola)
    x_trail.append(x)
    y_trail.append(y)

    # Limitar la longitud de la trayectoria
    if len(x_trail) > 50:  # Mantener solo los últimos 50 puntos
        x_trail.pop(0)
        y_trail.pop(0)

    trail.set_data(x_trail, y_trail)

    return point, trail

# Crear la animación
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=50)

# Guardar como GIF (opcional)
ani.save("circulo_girando.gif", writer="pillow", fps=60)

# Mostrar la animación
plt.show()