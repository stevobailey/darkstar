#!/opt/local/bin/python

import numpy as np
import matplotlib.pyplot as plt

freq = [7.5, 7.75, 8, 8.25, 8.5, 8.75]
vel = [1.993, 1.834, 1.6403, 1.5103, 1.3939, 1.2775]

#plt.plot(freq, vel, 'o')
#plt.xlabel('Frequency (GHz)', fontsize=14)
#plt.ylabel('Velocity (Gm/s)', fontsize=14)
#plt.title('Waveguide Velocities', fontsize=20)
#plt.show()

freq = [7.5, 7.75, 8, 8.25, 8.5, 8.75]
wl = [7.972, 7.336, 6.5612, 6.0412, 5.5756, 5.11]
points = np.arange(7,8.75,0.01)
fit = -2.2984*points+25.107

plt.plot(freq, wl, 'o')
plt.plot(points, fit, '-r')
plt.xlabel('Frequency (GHz)', fontsize=14)
plt.ylabel('Wavelength (cm)', fontsize=14)
plt.title('Waveguide Wavelengths', fontsize=20)
plt.show()
