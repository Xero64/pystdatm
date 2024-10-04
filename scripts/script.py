#%%
# Import Dependencies
from pystdatm import density, pressure, speed_of_sound, temperature, viscosity

#%%
# Sample Code
alt = 0.0 # metres above sea level

rho = density(alt)
print(f'rho = {rho:} kg/m**3 at Altitude = {alt:} m\n')

mu = viscosity(alt)
print(f'mu = {mu:} Pa.s at Altitude = {alt:} m\n')

p = pressure(alt)
print(f'p = {p:} Pa at Altitude = {alt:} m\n')

a = speed_of_sound(alt)
print(f'a = {a:} m/s at Altitude = {alt:} m\n')

temp = temperature(alt)
print(f'temp = {temp:} K at Altitude = {alt:} m\n')
