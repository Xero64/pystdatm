# pystdatm

## Python Package for Standard Atmosphere

The set of functions that follow International Standard Atmosphere model.

*Note*: Only SI units are supported.

Sample Code:
``` python
from pystdatm import (density, geometric_altitude, pressure,
                      speed_of_sound, temperature, viscosity)

alt = 14000.0 # metres above sea level
print(f'Altitude = {alt:.0f} m\n')

altz = geometric_altitude(alt)
print(f'Geometric Altitude = {altz:.0f} m\n')

temp = temperature(alt)
print(f'Air Temperature = {temp:.2f} K\n')

pres = pressure(alt)
print(f'Air Pressure = {pres:.6g} Pa\n')

rho = density(alt)
print(f'Air Density = {rho:.4f} kg/m**3\n')

mu = viscosity(temp)
print(f'Air Viscosity = {mu:.5g} Pa.s\n')

a = speed_of_sound(temp)
print(f'Speed of Sound = {a:.1f} m/s\n')

# Example of ISA Properties at Altitude with Temperature Deviation
deviation = 10.0 # K

rho_dev = density(alt, deviation=deviation)
print(f'Density ISA+{deviation:.0f} = {rho_dev:.4f} kg/m**3\n')
```

Sample Output:
```
Altitude = 14000 m

Geometric Altitude = 14031 m

Air Temperature = 216.65 K

Air Pressure = 14101.8 Pa

Air Density = 0.2268 kg/m**3

Air Viscosity = 1.7826e-05 Pa.s

Speed of Sound = 339.5 m/s

Density ISA+10 = 0.2167 kg/m**3
```
