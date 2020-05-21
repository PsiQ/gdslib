import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import speed_of_light


def get_sparameters(c, wavelengths=None):
    if wavelengths is None:
        wavelengths = np.linspace(1520, 1570, 1024) * 1e-9
    f = 3e8 / wavelengths
    return c.s_parameters(freq=f)


def plot_sparameters(c, wavelengths=None, pins=None):
    """ plots sparameters from a model

    Args:
        c: circuit model
        wavelengths: wavelengths (m)
        pins: list of pins to plot

    .. plot::
        :include-source:

        from simphony.library import siepic
        from simphony.library.gdsfactory import plot_sparameters

        coupler = siepic.ebeam_dc_halfring_straight()
        plot_sparameters(coupler)
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
            plt.plot(wavelengths * 1e9, 100 * np.abs(s[:, i, 0] ** 2), label=pin)
    plt.xlabel("wavelength (nm)")
    plt.ylabel("Transmission (%)")


if __name__ == "__main__":
    from simphony.library import siepic

    wavelengths = np.linspace(1520, 1570, 1024) * 1e-9
    coupler = siepic.ebeam_dc_halfring_straight(
        gap=200e-9, radius=10e-6, width=500e-9, thickness=220e-9, couple_length=0.0
    )
    plot_sparameters(coupler, wavelengths)
    plt.legend()
    plt.show()
