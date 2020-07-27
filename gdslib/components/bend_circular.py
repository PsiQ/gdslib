from typing import Any
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

import numpy as np
import pp
from SiPANN.nn import bentWaveguide_S

from gdslib import plot_model
from gdslib.autoname import autoname
from gdslib.model_from_sparameters import model_from_sparameters


@autoname
def bend_circular(
    radius: float = 10.0,
    width: float = 0.5,
    thickness: float = 0.22,
    angle: int = 90,
    sw_angle: float = 90.0,
    wavelength: Optional = None,
    **kwargs,
):
    """Returns simphony Model for a bend

    Args:
        radius: Radius of waveguide in microns.
        width: Width of the waveguides in microns
        thickness: Thickness of the waveguides in microns
        angle: Number of deg of circle that bent waveguide transverses
        sw_angle: Sidewall angle from horizontal in degrees, ie 90 makes a square. Defaults to 90.
        wavelength:  Wavelength points to evaluate

    """
    angle = np.deg2rad(angle)
    if wavelength is None:
        wavelength = np.linspace(1200, 1600) * 1e-9
    s = bentWaveguide_S(
        wavelength=wavelength,
        width=width,
        thickness=thickness,
        radius=radius,
        angle=angle,
        sw_angle=sw_angle,
    )
    return model_from_sparameters(wavelength, s, pins=("W0", "N0"))


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    c = bend_circular()
    plot_model(c)
    plt.show()
