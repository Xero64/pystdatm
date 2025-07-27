from typing import TYPE_CHECKING

from .constants import G_0, R
from .stratopause import density_stratopause as _density_before
from .stratopause import pressure_stratopause as _pressure_before
from .stratopause import temperature_stratopause as _temperature_before

if TYPE_CHECKING:
    from numpy.typing import NDArray

L_5 = -2.8e-3 # K/m
H_5 = 51000.0 # m
T_5 = _temperature_before(H_5) # K
P_5 = _pressure_before(H_5) # Pa
RHO_5 = _density_before(H_5) # kg/m^3

lambda_5: float = -G_0/(L_5*R)

def temperature_mesosphere_5(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return T_5 + L_5*(altitude - H_5)

def pressure_mesosphere_5(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    temp = temperature_mesosphere_5(altitude)
    return P_5*(temp/T_5)**lambda_5

def density_mesosphere_5(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    temp = temperature_mesosphere_5(altitude)
    return RHO_5*(temp/T_5)**(lambda_5 - 1.0)

L_6 = -2.0e-3 # K/m
H_6 = 71000.0 # m
T_6 = temperature_mesosphere_5(H_6) # K
P_6 = pressure_mesosphere_5(H_6) # Pa
RHO_6 = density_mesosphere_5(H_6) # kg/m^3

lambda_6: float = -G_0/(L_6*R)

def temperature_mesosphere_6(altitude: 'NDArray') -> 'NDArray':
    """This function returns the temperature given input altitude."""
    return T_6 + L_6*(altitude - H_6)

def pressure_mesosphere_6(altitude: 'NDArray') -> 'NDArray':
    """This function returns the pressure given input altitude."""
    temp = temperature_mesosphere_6(altitude)
    return P_6*(temp/T_6)**lambda_6

def density_mesosphere_6(altitude: 'NDArray') -> 'NDArray':
    """This function returns the density given input altitude."""
    temp = temperature_mesosphere_6(altitude)
    return RHO_6*(temp/T_6)**(lambda_6 - 1.0)
