from numpy import isclose, isnan

from pystdatm import density_deviation

def test_density_deviation_0():
    assert isclose(density_deviation(0.0, 10.0), 1.183913, atol=1e-6)

def test_density_deviation_1():
    assert isclose(density_deviation(11000.0, 10.0), 0.347861, atol=1e-6)

def test_density_deviation_2():
    assert isclose(density_deviation(20000.0, 10.0), 0.084150, atol=1e-6)

def test_density_deviation_3():
    assert isclose(density_deviation(32000.0, 10.0), 0.012670, atol=1e-6)

def test_density_deviation_4():
    assert isclose(density_deviation(47000.0, 10.0), 0.001376, atol=1e-6)

def test_density_deviation_5():
    assert isclose(density_deviation(51000.0, 10.0), 0.000830, atol=1e-6)

def test_density_deviation_6():
    assert isclose(density_deviation(71000.0, 10.0), 0.000061, atol=1e-6)

def test_density_deviation_7():
    assert isclose(density_deviation(84852.0, 10.0), 0.000006, atol=1e-6)

def test_density_deviation_8():
    assert isnan(density_deviation(0.0, -320.0))

def test_density_deviation_9():
    assert isclose(density_deviation(0.0, 320.0), 0.580422, atol=1e-6)
