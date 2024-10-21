from typing import TYPE_CHECKING

from numpy import exp, full, shape

from .constants import G_0, R
from .stratosphere import density_stratosphere_3 as _density_before
from .stratosphere import pressure_stratosphere_3 as _pressure_before
from .stratosphere import temperature_stratosphere_3 as _temperature_before

if TYPE_CHECKING:
    from numpy.typing import NDArray

H_4 = 47000.0 # m
T_4: float = _temperature_before(H_4) # K
P_4: float = _pressure_before(H_4) # Pa
RHO_4: float = _density_before(H_4) # kg/m^3

delta_4: float = -G_0/(R*T_4)

def temperature_stratopause(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return full(shape(altitude), T_4)

def pressure_stratopause(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    return P_4*exp(delta_4*(altitude - H_4))

def density_stratopause(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    return RHO_4*exp(delta_4*(altitude - H_4))
