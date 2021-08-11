import numpy as np
import matplotlib.pyplot as plt
k=4.2
t=np.linspace(0,8*np.pi,1000)
x=np.cos(k*t)*np.cos(t)
y=np.cos(k*t)*np.sin(t)
plt.plot(x,y,'m',linewidth=2)
plt.axis('square')
plt.axis('off')
plt.show()