import numpy as np
import pp
from scipy.constants import speed_of_light
from simphony.elements import Model
from simphony.tools import freq2wl
from simphony.tools import interpolate
from simphony.tools import wl2freq

from gdslib.config import CONFIG


def model_from_sparameters(wavelengths, sparameters, pins=("E0", "W0")):
    """returns simphony model from Sparameters"""

    f = wl2freq(wavelengths)
    s = sparameters

    def interpolate_sp(freq):
        return interpolate(freq, f, s)

    m = Model()
    m.pins = pins
    m.s_params = (f, s)
    m.s_parameters = interpolate_sp
    m.freq_range = (m.s_params[0][-1], m.s_params[0][0])
    m.wavelength_range = freq2wl(np.array([m.s_params[0][0], m.s_params[0][-1]]))
    m.wavelengths = speed_of_light / np.array(f)
    m.s = s
    m.name = "model_from_sparameters"
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    c = model_from_sparameters(pp.c.mmi1x2())
    # wav = np.linspace(1520, 1570, 1024) * 1e-9
    # f = speed_of_light / wav
    # s = c.s_parameters(freq=f)

    wav = c.wavelengths
    s = c.s
    plt.plot(wav * 1e9, np.abs(s[:, 1] ** 2))

    plt.show()
