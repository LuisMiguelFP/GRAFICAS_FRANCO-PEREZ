import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt .subplots()
ax.set_label("onda seno ")
ax.set_xlim(0,2*np.pi)
ax.set_ylim(-1.5,1.5)
ax.set_xlabel("x")
ax.set_ylabel("y")

x = np.linspace(0,2*np.pi,1000) 
line, =ax.plot(x,np.sin(x),lw = 2,color = 'purple')


def init():
    line.set_data(x,np.sin(x))
    return line,

def update(frame):
    t= frame*0.1
    y= np.sin(x+t)
    line.set_data(x,y)
    return line,


ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

ani.save("seno animado.gif",writer="pillow",fps=20)
plt.show()