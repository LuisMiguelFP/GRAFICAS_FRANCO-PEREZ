import matplotlib.pyplot as plt
import pandas as pd 
import random
import numpy as np

# grafico de lineas tiringuistingis

""" data = pd.read_csv('clima.csv')

plt.plot(data['dia'], data['temperatura'], data['lluvia'])
plt.title('Gráfica de Clima')
plt.xlabel("Días")
plt.ylabel("Temperatura / Lluvia")
plt.grid(True)
plt.show()
 """

# Leer el archivo CSV
""" data = pd.read_csv('clima.csv')

# Graficar histogramas superpuestos
plt.hist(data['dia'], bins=10, alpha=0.5, label='Día', color='blue')
plt.hist(data['temperatura'], bins=10, alpha=0.5, label='Temperatura', color='red')
plt.hist(data['lluvia'], bins=10, alpha=0.5, label='Lluvia', color='green')

# Configurar el gráfico
plt.title("Histograma de Día, Temperatura y Lluvia")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()  # Mostrar la leyenda
plt.grid(True)
plt.show() """

#1. Gráfico de línea simple
""" valores = [3,7,1,5,12] 
plt.plot(valores,marker = 'o',color ='blue')

plt.plot(valores, marker='o', linestyle='-', color='blue')

# Configurar el gráfico
plt.title("Gráfico de Línea Simple")
plt.xlabel("Índice")
plt.ylabel("Valores")
plt.grid(True)  # Agregar cuadrícula

# Mostrar el gráfico
plt.show() """



#2. Gráfico de barras

""" cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]


plt.bar(cursos, cantidad, color='skyblue')


plt.title("Cantidad de Estudiantes por Curso")
plt.xlabel("Cursos")
plt.ylabel("Cantidad de Estudiantes")
plt.grid(axis='y', linestyle='--', alpha=0.7) 


plt.show() """

#3. Gráfico de dispersión (scatter plot)


""" x = [random.randint(1, 100) for _ in range(50)]
y = [random.randint(1, 100) for _ in range(50)]


plt.scatter(x, y, color='purple', alpha=0.7)


plt.title("Gráfico de Dispersión")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.grid(True)


plt.show() """



#4. Subplots

""" plt.figure(figsize=(10, 6))


x = np.linspace(0, 2 * np.pi, 100)  
y_seno = np.sin(x)  
plt.subplot(2, 1, 1)  
plt.plot(x, y_seno, color='blue', label='Seno')
plt.title("Línea Senoidal")
plt.xlabel("X")
plt.ylabel("sin(X)")
plt.grid(True)
plt.legend()

# Subgráfico 2: Función cuadrática
x = np.linspace(-10, 10, 100)  
y_cuadratica = x**2  
plt.subplot(2, 1, 2)  
plt.plot(x, y_cuadratica, color='red', label='Cuadrática')
plt.title("Función Cuadrática")
plt.xlabel("X")
plt.ylabel("X^2")
plt.grid(True)
plt.legend()


plt.tight_layout()


plt.show()
 """



#5. Generar datos y graficar una función

""" x = np.linspace(-10, 10, 100)

y = x**2 - 3*x + 2

plt.plot(x, y, color='green', label='y = x² - 3x + 2')

plt.title("Gráfico de la función y = x² - 3x + 2")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.grid(True)
plt.legend()


plt.show() """

#6. Comparación de funciones



""" x = np.linspace(0, 2 * np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)


plt.plot(x, y_sin, label='sin(x)', color='blue')
plt.plot(x, y_cos, label='cos(x)', color='red')


plt.title("Funciones sin(x) y cos(x)")
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.grid(True)
plt.legend()


plt.show() """

#7. Operaciones entre arrays

""" vector1 = np.random.randint(0, 101, 100)
vector2 = np.random.randint(0, 101, 100)


suma_total = np.sum(vector1) + np.sum(vector2)

valor_maximo = max(np.max(vector1), np.max(vector2))


desviacion_estandar = np.std(np.concatenate((vector1, vector2)))


print("Suma total:", suma_total)
print("Valor máximo:", valor_maximo)
print("Desviación estándar:", desviacion_estandar) """

#8. Histograma con NumPy


""" datos = np.random.normal(loc=0, scale=1, size=1000)  

plt.hist(datos, bins=30, color='blue', alpha=0.7, edgecolor='black')

plt.title("Histograma de Distribución Normal")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.show() """

# 9 Cargar archivo

""" data = pd.read_csv('ventas.csv')
print(data.head()) """

# 10 Estadísticas básicas




""" data = pd.read_csv('ventas.csv')


total_ventas = data[['producto_a', 'producto_b', 'producto_c']].sum()

promedio_ventas = data[['producto_a', 'producto_b', 'producto_c']].mean()

producto_mas_vendido = total_ventas.idxmax()


print("Total de Ventas por Producto:")
print(total_ventas)
print("\nPromedio de Ventas por Producto:")
print(promedio_ventas)
print("\nProducto más Vendido:", producto_mas_vendido) """


#11. Filtrar datos


""" data = pd.read_csv('ventas.csv')

ventas_enero = data[data['mes'] == 'Enero']
print("Ventas en el mes de Enero:")
print(ventas_enero) """

# 12. Gráfica de barras con Pandas

data = pd.read_csv('ventas.csv')

total_ventas = data[['producto_a', 'producto_b', 'producto_c']].sum()

total_ventas.plot(kind='bar', color=['blue', 'green', 'red'], alpha=0.7, edgecolor='black')


plt.title("Cantidad Total Vendida por Producto")
plt.xlabel("Productos")
plt.ylabel("Cantidad Vendida")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()