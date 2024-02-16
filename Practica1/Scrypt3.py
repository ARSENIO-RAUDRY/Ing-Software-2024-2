import math
import numpy as np
import matplotlib.pyplot as plt
"""
    Funcion transcrita de internet que intentaba replicar la forma de un muercielago, aparenteme la transcripcion fue defectuosa
    """
x = np.arange(-8,8,1)
y1 = abs(x)/x * (.3 *abs(x) + .2 *(abs(abs(x)-1)) + 2.2*(abs(abs(x)-2)) - 2.7*(abs(abs(x)-3)) - 3*(abs(abs(x)-5)) + 3*(abs(abs(x)-7)) + 5*np.sin( (math.pi/4) * (abs(abs(x)-3) - abs(abs(x)-4) +1 )) + (5/4)*(abs(abs(x)-4) - abs(abs(x)-5) -1)**3 - 5.3*np.cos( ((math.pi/2) + np.arcsin(47/53)) * ((abs(abs(x)-7)) - abs((abs(x)-8))-1)/2) +2.8)

plt.plot(x,y1)
plt.show()
