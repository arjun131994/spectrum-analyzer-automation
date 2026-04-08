from sa_control import measure_power

def test_power_limit():

    freq = 1e9

    power = measure_power(freq)

    assert power < 0
