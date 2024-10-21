#%%
# Import Dependencies
from pystdatm import (density, geometric_altitude, pressure, speed_of_sound,
                      temperature, viscosity)

#%%
# Example of ISA Properties at Altitude
alt = 14000.0 # metres above sea level
print(f'Altitude = {alt:.0f} m\n')

altz = geometric_altitude(alt)
print(f'Geometric Altitude = {altz:.0f} m\n')

temp = temperature(alt)
print(f'Temperature = {temp:.2f} K\n')

pres = pressure(alt)
print(f'Pressure = {pres:.6g} Pa\n')

rho_trop = density(alt)
print(f'rho_trop = {rho_trop:.4f} kg/m**3\n')

mu_trop = viscosity(temp)
print(f'mu_trop = {mu_trop:.5g} Pa.s\n')

a_trop = speed_of_sound(temp)
print(f'a_trop = {a_trop:.1f} m/s\n')
