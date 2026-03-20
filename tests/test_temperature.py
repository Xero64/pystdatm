from numpy import isclose, isnan

from pystdatm import temperature

def test_temperature_0():
    assert isclose(temperature(0.0), 288.15, atol=1e-12)

def test_temperature_1():
    assert isclose(temperature(11000.0), 216.65, atol=1e-12)

def test_temperature_2():
    assert isclose(temperature(20000.0), 216.65, atol=1e-12)

def test_temperature_3():
    assert isclose(temperature(32000.0), 228.65, atol=1e-12)

def test_temperature_4():
    assert isclose(temperature(47000.0), 270.65, atol=1e-12)

def test_temperature_5():
    assert isclose(temperature(51000.0), 270.65, atol=1e-12)

def test_temperature_6():
    assert isclose(temperature(71000.0), 214.65, atol=1e-12)

def test_temperature_7():
    print(temperature(84852.0))
    assert isclose(temperature(84852.0), 186.946, atol=1e-12)

def test_temperature_8():
    assert isnan(temperature(90000.0))

def test_temperature_9():
    assert isnan(temperature(-5000.0))
