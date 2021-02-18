import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle

time = list(map(float, open('data//time.txt', 'r').read().split()))
velocity = list(map(float, open('data//velocity.txt', 'r').read().split()))
x, y = LombScargle(time, velocity).autopower(minimum_frequency=0.1, maximum_frequency=100, normalization=None, samples_per_peak=10)
yy = [float(_) for _ in y]
xx = [float(_) for _ in x]
print(1/xx[yy.index(max(yy))],"days")
plt.plot(1/x, y,color = 'purple')
plt.xlabel("Time Period")
plt.savefig("output//Lombscargle Astro", dpi=300)
plt.show()
