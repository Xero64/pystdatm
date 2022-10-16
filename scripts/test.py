#%%
# Import Dependencies
from pystdatm import density, pressure

#%%
# Sample Code
alt = 1000.0 # metres above sea level

rho = density(alt)
print(f'rho = {rho:.3f} kg/m**3')

p = pressure(alt)
print(f'p = {p:.0f} Pa')
