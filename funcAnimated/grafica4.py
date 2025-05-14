import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Leer el archivo CSV
df = pd.read_csv(r"c:\Users\ELIAS\Desktop\trabajos_graficas\graficas2\energia.csv")

# Filtrar datos para los países o regiones deseados
countries = ["Africa", "Asia", "Europe"]  # Lista de países o regiones
df_selected = df[df["Entity"].isin(countries)].copy()
df_selected = df_selected.sort_values(["Year"])  # Ordenar por año

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_title("Evolución de Energías Renovables")
ax.set_xlabel("País/Región")
ax.set_ylabel("Renovables (% energía primaria)")
ax.set_ylim(0, df_selected["Renewables (% equivalent primary energy)"].max() + 10)

# Inicializar las barras
bars = ax.bar(countries, [0] * len(countries), color=["blue", "green", "orange"])

# Función de inicialización
def init():
    for bar in bars:
        bar.set_height(0)  # Altura inicial de las barras
    return bars

# Función de actualización
def update(frame):
    year = df_selected["Year"].unique()[frame]  # Obtener el año actual
    data = df_selected[df_selected["Year"] == year]  # Filtrar datos del año actual

    for bar, country in zip(bars, countries):
        value = data[data["Entity"] == country]["Renewables (% equivalent primary energy)"].values
        bar.set_height(value[0] if len(value) > 0 else 0)  # Actualizar altura de la barra

    ax.set_title(f"Evolución de Energías Renovables - Año {year}")  # Actualizar título
    return bars

# Crear la animación
ani = FuncAnimation(fig, update, frames=len(df_selected["Year"].unique()), init_func=init, blit=True, interval=500)

# Guardar como GIF (opcional)
ani.save("evolucion_renovables.gif", writer="pillow", fps=2)

# Mostrar la animación
plt.show()