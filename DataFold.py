import matplotlib.pyplot as plt
import numpy as np
from PyAstronomy.pyasl import foldAt

# Data
time = np.array(list(map(float, open('data//time.txt', 'r').read().split())))
velocity = np.array(list(map(float, open('data//velocity.txt', 'r').read().split())))
timeperiod = 4.230992235763096  # LombScargleScipy.py

# main
phases = foldAt(time, timeperiod)

# Plotting
plt.plot(phases, velocity, 'b+', color='r')
plt.xlabel("Phases")
plt.ylabel("Velocity")
plt.tight_layout()
plt.savefig("output//Folded.png",dpi=300)
plt.show()
