"""
The pystdatm package contains functions for various
International Standard Atmosphere (ISA) properties
at different altitudes.
"""

from typing import TYPE_CHECKING

from numpy import asarray, full, logical_and, sqrt

from .constants import (BETA_S, GAMMA, H_0, H_1, H_2, H_3, H_4, H_5, H_6, H_7,
                        R_0, RHO_0, R, S)
from .mesosphere import (density_mesosphere_5, density_mesosphere_6,
                         pressure_mesosphere_5, pressure_mesosphere_6,
                         temperature_mesosphere_5, temperature_mesosphere_6)
from .stratopause import (density_stratopause, pressure_stratopause,
                          temperature_stratopause)
from .stratosphere import (density_stratosphere_2, density_stratosphere_3,
                           pressure_stratosphere_2, pressure_stratosphere_3,
                           temperature_stratosphere_2,
                           temperature_stratosphere_3)
from .tropopause import (density_tropopause, pressure_tropopause,
                         temperature_tropopause)
from .troposphere import (density_troposphere, pressure_troposphere,
                          temperature_troposphere)

if TYPE_CHECKING:
    from numpy.typing import NDArray

def geometric_altitude(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns the geometric altitude
    for the given input geopotential altitude.
    """
    altitude = asarray(altitude)
    return R_0*altitude/(R_0 - altitude)

def check_layer(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns boolean arrays
    checking which layer the altitude is in.
    """
    altitude = asarray(altitude)
    # Troposphere
    chk_0 = logical_and(altitude >= H_0 ,altitude <= H_1)
    # Tropopause
    chk_1 = logical_and(altitude > H_1 ,altitude <= H_2)
    # Stratosphere 2
    chk_2 = logical_and(altitude > H_2 ,altitude <= H_3)
    # Stratosphere 3
    chk_3 = logical_and(altitude > H_3 ,altitude <= H_4)
    # Stratopause
    chk_4 = logical_and(altitude > H_4 ,altitude <= H_5)
    # Mesosphere 5
    chk_5 = logical_and(altitude > H_5 ,altitude <= H_6)
    # Mesosphere 6
    chk_6 = logical_and(altitude > H_6 ,altitude <= H_7)
    # Return the boolean arrays
    return chk_0, chk_1, chk_2, chk_3, chk_4, chk_5, chk_6

def filter_layer(altitude: 'NDArray', chks: tuple['NDArray']) -> 'NDArray':
    """
    This function returns the altitudes filtered by layer.
    """
    altitude = asarray(altitude)
    chk_0, chk_1, chk_2, chk_3, chk_4, chk_5, chk_6 = chks
    alt_0 = altitude[chk_0]
    alt_1 = altitude[chk_1]
    alt_2 = altitude[chk_2]
    alt_3 = altitude[chk_3]
    alt_4 = altitude[chk_4]
    alt_5 = altitude[chk_5]
    alt_6 = altitude[chk_6]
    return alt_0, alt_1, alt_2, alt_3, alt_4, alt_5, alt_6

def temperature(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns the temperature for a given
    geopotential altitude.
    """
    altitude = asarray(altitude)
    chks = check_layer(altitude)
    chk_0, chk_1, chk_2, chk_3, chk_4, chk_5, chk_6 = chks
    alts = filter_layer(altitude, chks)
    alt_0, alt_1, alt_2, alt_3, alt_4, alt_5, alt_6 = alts
    temp = full(altitude.shape, float('nan'))
    temp[chk_0] = temperature_troposphere(alt_0)
    temp[chk_1] = temperature_tropopause(alt_1)
    temp[chk_2] = temperature_stratosphere_2(alt_2)
    temp[chk_3] = temperature_stratosphere_3(alt_3)
    temp[chk_4] = temperature_stratopause(alt_4)
    temp[chk_5] = temperature_mesosphere_5(alt_5)
    temp[chk_6] = temperature_mesosphere_6(alt_6)
    return temp

def pressure(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns the pressure for a given
    geopotential altitude.
    """
    altitude = asarray(altitude)
    chks = check_layer(altitude)
    chk_0, chk_1, chk_2, chk_3, chk_4, chk_5, chk_6 = chks
    alts = filter_layer(altitude, chks)
    alt_0, alt_1, alt_2, alt_3, alt_4, alt_5, alt_6 = alts
    pres = full(altitude.shape, float('nan'))
    pres[chk_0] = pressure_troposphere(alt_0)
    pres[chk_1] = pressure_tropopause(alt_1)
    pres[chk_2] = pressure_stratosphere_2(alt_2)
    pres[chk_3] = pressure_stratosphere_3(alt_3)
    pres[chk_4] = pressure_stratopause(alt_4)
    pres[chk_5] = pressure_mesosphere_5(alt_5)
    pres[chk_6] = pressure_mesosphere_6(alt_6)
    return pres

def density(altitude: 'NDArray', deviation: float = 0.0) -> 'NDArray':
    """
    This function returns the density for a given
    geopotential altitude.
    """
    if deviation == 0.0:
        altitude = asarray(altitude)
        chks = check_layer(altitude)
        chk_0, chk_1, chk_2, chk_3, chk_4, chk_5, chk_6 = chks
        alts = filter_layer(altitude, chks)
        alt_0, alt_1, alt_2, alt_3, alt_4, alt_5, alt_6 = alts
        dens = full(altitude.shape, float('nan'))
        dens[chk_0] = density_troposphere(alt_0)
        dens[chk_1] = density_tropopause(alt_1)
        dens[chk_2] = density_stratosphere_2(alt_2)
        dens[chk_3] = density_stratosphere_3(alt_3)
        dens[chk_4] = density_stratopause(alt_4)
        dens[chk_5] = density_mesosphere_5(alt_5)
        dens[chk_6] = density_mesosphere_6(alt_6)
    else:
        dens = density_deviation(altitude, deviation)
    return dens

def density_deviation(altitude: 'NDArray', deviation: float) -> 'NDArray':
    """
    This function returns the density for a given
    geopotential altitude and temperature deviation.
    """
    altitude = asarray(altitude)
    temp = temperature(altitude) + deviation
    pres = pressure(altitude)
    # Calculate the density using the ideal gas law
    # rho = p/(R*T)
    rho = pres/(R*temp)
    return rho

def density_ratio(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns the density ratio for a given
    geopotential altitude.
    """
    altitude = asarray(altitude)
    return density(altitude)/RHO_0

def speed_of_sound(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns the speed of sound for a given
    geopotential altitude.
    """
    altitude = asarray(altitude)
    return speed_of_sound_temperature(temperature(altitude))

def viscosity(altitude: 'NDArray') -> 'NDArray':
    """
    This function returns the viscosity for a given
    geopotential altitude.
    """
    altitude = asarray(altitude)
    return viscosity_temperature(temperature(altitude))

def viscosity_temperature(temperature: 'NDArray') -> 'NDArray':
    """
    This function returns the viscosity given input temperature.
    """
    temperature = asarray(temperature)
    return BETA_S*temperature**1.5/(temperature + S)

def speed_of_sound_temperature(temperature: 'NDArray') -> 'NDArray':
    """
    This function returns the speed of sound given input temperature.
    """
    temperature = asarray(temperature)
    return sqrt(GAMMA*R*temperature)

def equivalent_airspeed(altitude: 'NDArray', vtas: 'NDArray') -> 'NDArray':
    """
    This function returns the equivalent airspeed for a given
    input altitude and true airspeed.
    """
    altitude = asarray(altitude)
    return sqrt(density_ratio(altitude)*vtas**2)

def true_airspeed(altitude: 'NDArray', veas: 'NDArray') -> 'NDArray':
    """
    This function returns the true airspeed for a given
    input altitude and equivalent airspeed.
    """
    altitude = asarray(altitude)
    return sqrt(veas**2/density_ratio(altitude))
