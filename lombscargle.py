import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal

time = list(map(float, open('time.txt', 'r').read().split()))
velocity = list(map(float, open('velocity.txt', 'r').read().split()))
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
print("Dominant Angular Frequency =", blaa, "radians / day")
print("Time Period = ", 2 * np.pi / blaa, "days")
plt.savefig("LombScargle", dpi=200)
plt.show()

