import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import pandas as pd

data = pd.read_csv('dataset.csv')

time = data['time']
velocity = data['velocity']

f = np.linspace(0.1, 10, 1000)

periodogram = signal.lombscargle(time, velocity, f, normalize=True, precenter=True)

plt.subplot(211)

plt.plot(f, periodogram, color='red')
plt.xlabel("Angular Frequency")
plt.ylabel("LombScargle Power")

plt.subplot(212)

plt.plot(2 * np.pi / f, periodogram, color='green')
plt.xlim(0, 10)
plt.xlabel("Period")
plt.ylabel("LombScargle Power")

plt.tight_layout()

blaa = f[np.argmax(periodogram)]
print("w = {} rads/day, T = {} days".format(blaa,2*np.pi/blaa))

plt.savefig("images/lombscipy", dpi=144)

plt.show()

