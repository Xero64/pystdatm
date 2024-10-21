# pystdatm

## Python Package for Standard Atmosphere

The set of functions that follow International Standard Atmosphere model.

*Note*: Only SI units are supported.

Sample Code:
``` python
from pystdatm import density, pressure

alt = 1000.0 # metres above sea level

rho = density(alt)
print(f'rho = {rho:.3f} kg/m**3')

p = pressure(alt)
print(f'p = {p:.0f} Pa')

```

Sample Output:
```
rho = 1.112 kg/m**3
p = 89936 Pa
```
