#%%
# Import Dependencies
from IPython.display import display_markdown
from py2md.classes import MDTable

from pystdatm import (density, geometric_altitude, pressure, speed_of_sound,
                      temperature, viscosity)

#%%
# ISA Properties at Altitude
alt = [0.0, 11000.0, 20000.0, 32000.0, 47000.0, 51000.0, 71000.0, 84852.0]
altz = geometric_altitude(alt)
temp = temperature(alt)
p = pressure(alt)
rho = density(alt)
mu = viscosity(alt)
a = speed_of_sound(alt)

#%%
# Tabulate ISA Properties
table = MDTable()
table.add_column('Altitude (m)', '.0f', data=alt)
table.add_column('Geometric Altitude (m)', '.0f', data=altz.tolist())
table.add_column('Temperature (K)', '.2f', data=temp.tolist())
table.add_column('Pressure (Pa)', '.6g', data=p.tolist())
table.add_column('Density (kg/m**3)', '.4f', data=rho.tolist())
table.add_column('Viscosity (Pa.s)', '.5g', data=mu.tolist())
table.add_column('Speed of Sound (m/s)', '.1f', data=a.tolist())
display_markdown(table)
