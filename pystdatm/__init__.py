"""The pystdatm package contains functions for various
International Standard Atmosphere balues at different altitudes.
It currently only supports the Troposphere."""

from math import exp, sqrt

T_0 = 288.16 # K
p_0 = 101325.0 # Pa
rho_0 = 1.225 # kg/m^3
a_0 = 340.0 # m/s
mu_0 = 1.7758e-5 # kg/m/s
delta = 22.5577e-6 # /m
lamda = 5.225874
dlnmudT = 2.56E-3 # /K

def check_troposphere(altitude: float=0.0) -> bool:
    """ This function checks if the input altitude is in the Troposphere."""
    if -610.0 <= altitude <= 11000.0:
        return True
    else:
        return False

def temperature(altitude: float=0.0) -> float:
    """This function returns the temperature given input altitude."""
    if check_troposphere(altitude):
        return T_0*(1-delta*altitude)
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def pressure(altitude: float=0.0) -> float:
    """This function returns the pressure given input altitude."""
    if check_troposphere(altitude):
        return p_0*(1-delta*altitude)**lamda
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def density_ratio(altitude: float=0.0) -> float:
    """This function returns the density ratio given input altitude."""
    if check_troposphere(altitude):
        return (1-delta*altitude)**(lamda-1)
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def density(altitude: float=0.0) -> float:
    """This function returns the density given input altitude."""
    if check_troposphere(altitude):
        return rho_0*density_ratio(altitude)
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def speed_of_sound(altitude: float=0.0) -> float:
    """This function returns the speed of sound given input altitude."""
    if check_troposphere(altitude):
        return a_0*sqrt(1-delta*altitude)
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def viscosity(altitude: float=0.0) -> float:
    """This function returns the viscosity given input altitude."""
    if check_troposphere(altitude):
        return mu_0*exp(dlnmudT*(-delta*altitude)*T_0)
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def equivalent_airspeed(altitude: float=0.0, vtas: float=0.0) -> float:
    """This function returns the equivalent airspeed for a given
    input altitude and true airspeed."""
    if check_troposphere(altitude):
        return sqrt(density_ratio(altitude)*vtas**2)
    else:
        raise ValueError('Altitude is not within the Troposphere.')

def true_airspeed(altitude: float=0.0, veas: float=0.0) -> float:
    """This function returns the true airspeed for a given
    input altitude and equivalent airspeed."""
    if check_troposphere(altitude):
        return sqrt(veas**2/density_ratio(altitude))
    else:
        raise ValueError('Altitude is not within the Troposphere.')
