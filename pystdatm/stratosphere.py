from typing import TYPE_CHECKING

from .constants import G_0, R
from .tropopause import density_tropopause as _density_before
from .tropopause import pressure_tropopause as _pressure_before
from .tropopause import temperature_tropopause as _temperature_before

if TYPE_CHECKING:
    from numpy.typing import NDArray

L_2 = 1.0e-3 # K/m
H_2 = 20000.0 # m
T_2 = _temperature_before(H_2) # K
P_2 = _pressure_before(H_2) # Pa
RHO_2 = _density_before(H_2) # kg/m^3

lambda_2: float = -G_0/(L_2*R)

def temperature_stratosphere_2(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return T_2 + L_2*(altitude - H_2)

def pressure_stratosphere_2(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    temp = temperature_stratosphere_2(altitude)
    return P_2*(temp/T_2)**lambda_2

def density_stratosphere_2(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    temp = temperature_stratosphere_2(altitude)
    return RHO_2*(temp/T_2)**(lambda_2 - 1.0)

L_3 = 2.8e-3 # K/m
H_3 = 32000.0 # m
T_3 = temperature_stratosphere_2(H_3) # K
P_3 = pressure_stratosphere_2(H_3) # Pa
RHO_3 = density_stratosphere_2(H_3) # kg/m^3

lambda_3: float = -G_0/(L_3*R)

def temperature_stratosphere_3(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return T_3 + L_3*(altitude - H_3)

def pressure_stratosphere_3(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    temp = temperature_stratosphere_3(altitude)
    return P_3*(temp/T_3)**lambda_3

def density_stratosphere_3(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    temp = temperature_stratosphere_3(altitude)
    return RHO_3*(temp/T_3)**(lambda_3 - 1.0)
