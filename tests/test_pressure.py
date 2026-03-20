from numpy import isclose, isnan

from pystdatm import pressure

def test_pressure_0():
    assert isclose(pressure(0.0), 101325.0, atol=1e-12)

def test_pressure_1():
    assert isclose(pressure(11000.0), 22632.064, atol=1e-6)

def test_pressure_2():
    assert isclose(pressure(20000.0), 5474.889, atol=1e-6)

def test_pressure_3():
    assert isclose(pressure(32000.0), 868.019, atol=1e-6)

def test_pressure_4():
    assert isclose(pressure(47000.0), 110.906, atol=1e-6)

def test_pressure_5():
    assert isclose(pressure(51000.0), 66.938, atol=1e-6)

def test_pressure_6():
    assert isclose(pressure(71000.0), 3.956392, atol=1e-6)

def test_pressure_7():
    assert isclose(pressure(84852.0), 0.373380, atol=1e-6)

def test_pressure_8():
    assert isnan(pressure(90000.0))

def test_pressure_9():
    assert isnan(pressure(-5000.0))
