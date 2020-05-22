import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import speed_of_light


def get_sparameters(c, wavelengths=None):
    if wavelengths is None:
        wavelengths = c.wavelengths
    f = speed_of_light / wavelengths
    return c.s_parameters(freq=f)


def magnitude_square_per_cent(x):
    return 100 * np.abs(x ** 2)


def logscale(x):
    return 20 * np.log10(np.abs(x))


def plot_sparameters(
    c, wavelengths=None, pins=None, label=None, function=magnitude_square_per_cent
):
    """ plots sparameters from a model

    .. plot::
        :include-source:

        import gdslib as gl

        c = gl.mmi1x2()
        gl.plot_sparameters(c)
    """
    if callable(c):
        c = c()
    if wavelengths is None:
        wavelengths = c.wavelengths
    f = speed_of_light / wavelengths
    s = c.s_parameters(freq=f)

    pins = pins or c.pins
    assert isinstance(
        pins, (tuple, set, list)
    ), f"pins {pins} need to be a tuple, set or list"
    for pin in pins:
        assert pin in c.pins, f"{pin} not in {c.pins}"

    for i, pin in enumerate(c.pins):
        if pin in pins:
            plt.plot(wavelengths * 1e9, function(s[:, i, 0]), label=label or pin)
    plt.xlabel("wavelength (nm)")
    if function == magnitude_square_per_cent:
        plt.ylabel("S (%)")
    elif function == logscale:
        plt.ylabel("S (dB)")


if __name__ == "__main__":
    from simphony.library import siepic

    wavelengths = np.linspace(1520, 1570, 1024) * 1e-9
    coupler = siepic.ebeam_dc_halfring_straight(
        gap=200e-9, radius=10e-6, width=500e-9, thickness=220e-9, couple_length=0.0
    )
    plot_sparameters(coupler, wavelengths)
    plt.legend()
    plt.show()
