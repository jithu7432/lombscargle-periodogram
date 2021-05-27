import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PyAstronomy.pyasl import foldAt

# Data
data = pd.read_csv('dataset.csv')

time = data['time']
velocity = data['velocity']

timeperiod = 4.230992235763096  # LombScargleScipy.py

# main
phases = foldAt(time, timeperiod)

# Plotting
plt.plot(phases, velocity, 'rX')

plt.xlabel("Phases")
plt.ylabel("Velocity")

plt.tight_layout()
plt.savefig("images/folded.png",dpi=144)
plt.show()
