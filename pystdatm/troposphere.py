from typing import TYPE_CHECKING

from .constants import G_0, P_0, RHO_0, T_0, R

if TYPE_CHECKING:
    from numpy.typing import NDArray

L_0 = -6.5e-3 # K/m

lambda_0: float = -G_0/(L_0*R)

def temperature_troposphere(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return T_0 + L_0*altitude

def pressure_troposphere(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    temp = temperature_troposphere(altitude)
    return P_0*(temp/T_0)**lambda_0

def density_troposphere(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    temp = temperature_troposphere(altitude)
    return RHO_0*(temp/T_0)**(lambda_0 - 1.0)
