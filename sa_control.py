import pyvisa

def connect_sa():

    rm = pyvisa.ResourceManager()

    # change VISA address according to your instrument
    sa = rm.open_resource("USB0::0x0957::0x1234::MY123456::INSTR")

    return sa


def measure_power(freq):

    sa = connect_sa()

    sa.write("*RST")

    sa.write(f"SENS:FREQ:CENT {freq}")

    sa.write("INIT")

    power = sa.query("CALC:MARK:Y?")

    return float(power)
