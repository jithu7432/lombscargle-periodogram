import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle

data = pd.read_csv('dataset.csv')

time = data['time']
velocity = data['velocity']
x, y = LombScargle(time, velocity).autopower(minimum_frequency=0.1, \
	maximum_frequency=100, normalization=None, samples_per_peak=30)

print("Period is {} days".format(1/x[np.argmax(y)]))

plt.plot(1/x, y,color = 'purple')
plt.xlabel("time")
plt.savefig("images/lombastro.png", dpi=144)
plt.show()
