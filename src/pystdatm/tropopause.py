from typing import TYPE_CHECKING

from numpy import exp, full, shape

from .constants import G_0, R
from .troposphere import density_troposphere as _density_before
from .troposphere import pressure_troposphere as _pressure_before
from .troposphere import temperature_troposphere as _temperature_before

if TYPE_CHECKING:
    from numpy.typing import NDArray

H_1 = 11000.0 # m
T_1: float = _temperature_before(H_1) # K
P_1: float = _pressure_before(H_1) # Pa
RHO_1: float = _density_before(H_1) # kg/m^3

delta_1: float = -G_0/(R*T_1)

def temperature_tropopause(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return full(shape(altitude), T_1)

def pressure_tropopause(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    return P_1*exp(delta_1*(altitude - H_1))

def density_tropopause(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    return RHO_1*exp(delta_1*(altitude - H_1))
