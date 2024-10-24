#%%
# Import Dependencies
from matplotlib.pyplot import figure
from numpy import linspace

from pystdatm import density, pressure, speed_of_sound, temperature, viscosity

#%%
# ISA Properties at Altitude
alt = linspace(-2000.0, 84000.0, 173)
temp = temperature(alt)
p = pressure(alt)
rho = density(alt)
mu = viscosity(alt)
a = speed_of_sound(alt)

#%%
# Plot ISA Properties
fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.set_title('ISA Temperature Profile')
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Altitude (m)')
ax.grid(True)
cp_temp = ax.plot(temp, alt)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.set_title('ISA Pressure Profile')
ax.set_xlabel('Pressure (Pa)')
ax.set_ylabel('Altitude (m)')
ax.grid(True)
cp_p = ax.plot(p, alt)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.set_title('ISA Density Profile')
ax.set_xlabel('Density (kg/m**3)')
ax.set_ylabel('Altitude (m)')
ax.grid(True)
cp_rho = ax.plot(rho, alt)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.set_title('ISA Viscosity Profile')
ax.set_xlabel('Viscosity (Pa.s)')
ax.set_ylabel('Altitude (m)')
ax.grid(True)
cp_mu = ax.plot(mu, alt)

fig = figure(figsize=(12, 8))
ax = fig.gca()
ax.set_title('ISA Speed of Sound Profile')
ax.set_xlabel('Speed of Sound (m/s)')
ax.set_ylabel('Altitude (m)')
ax.grid(True)
cp_a = ax.plot(a, alt)
