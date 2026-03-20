from numpy import isclose, isnan

from pystdatm import density

def test_density_0():
    assert isclose(density(0.0), 1.225, atol=1e-12)

def test_density_1():
    print(density(11000.0))
    assert isclose(density(11000.0), 0.363917, atol=1e-6)

def test_density_2():
    print(density(20000.0))
    assert isclose(density(20000.0), 0.088034, atol=1e-6)

def test_density_3():
    print(density(32000.0))
    assert isclose(density(32000.0), 0.013224, atol=1e-6)

def test_density_4():
    print(density(47000.0))
    assert isclose(density(47000.0), 0.001427, atol=1e-6)

def test_density_5():
    print(density(51000.0))
    assert isclose(density(51000.0), 0.000861, atol=1e-6)

def test_density_6():
    assert isclose(density(71000.0), 0.000064, atol=1e-6)

def test_density_7():
    print(density(84852.0))
    assert isclose(density(84852.0), 0.000006, atol=1e-6)

def test_density_8():
    assert isnan(density(90000.0))

def test_density_9():
    assert isnan(density(-5000.0))
