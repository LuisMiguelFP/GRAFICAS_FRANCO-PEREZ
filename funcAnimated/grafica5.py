import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración inicial
num_planets = 3  # Número de planetas
radii = [1, 1.5, 2]  # Radios de las órbitas
angular_speeds = [0.05, 0.03, 0.02]  # Velocidades angulares (rad/s)
colors = ['blue', 'green', 'orange']  # Colores de los planetas

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_xlim(-2.5, 2.5)  # Límites del eje X
ax.set_ylim(-2.5, 2.5)  # Límites del eje Y
ax.set_title("Sistema Planetario Simple")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Dibujar la estrella central
star = plt.Circle((0, 0), 0.1, color='yellow', label='Estrella')
ax.add_artist(star)

# Crear los planetas y sus trayectorias
planets = []
trails = []
for i in range(num_planets):
    planet, = ax.plot([], [], 'o', color=colors[i], label=f'Planeta {i+1}')
    trail, = ax.plot([], [], '-', color=colors[i], lw=1, alpha=0.5)  # Trayectoria
    planets.append(planet)
    trails.append(trail)

# Inicializar las trayectorias
x_trails = [[] for _ in range(num_planets)]
y_trails = [[] for _ in range(num_planets)]

# Función de inicialización
def init():
    for planet, trail in zip(planets, trails):
        planet.set_data([], [])
        trail.set_data([], [])
    return planets + trails

# Función de actualización
def update(frame):
    for i, (radius, speed) in enumerate(zip(radii, angular_speeds)):
        # Calcular la posición del planeta
        angle = frame * speed
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        # Actualizar la posición del planeta
        planets[i].set_data([x], [y])

        # Actualizar la trayectoria
        x_trails[i].append(x)
        y_trails[i].append(y)

        # Limitar la longitud de la trayectoria
        if len(x_trails[i]) > 100:  # Mantener solo los últimos 100 puntos
            x_trails[i].pop(0)
            y_trails[i].pop(0)

        trails[i].set_data(x_trails[i], y_trails[i])

    return planets + trails

# Crear la animación
ani = FuncAnimation(fig, update, frames=500, init_func=init, blit=True, interval=50)

# Guardar como GIF (opcional)
ani.save("sistema_planetario.gif", writer="pillow", fps=20)

# Mostrar la animación
plt.legend()
plt.show()