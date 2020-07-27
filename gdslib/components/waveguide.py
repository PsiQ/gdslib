from typing import Any
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

import numpy as np
import pp
from SiPANN.nn import straightWaveguide_S

from gdslib import plot_model
from gdslib.autoname import autoname
from gdslib.model_from_sparameters import model_from_sparameters


@autoname
def waveguide(
    length: float = 10.0,
    width: float = 0.5,
    thickness: float = 0.22,
    sw_angle: float = 90.0,
    wavelength: Optional = None,
    **kwargs,
):
    """Returns simphony Model for a Straight waveguide"""
    if wavelength is None:
        wavelength = np.linspace(1200, 1600) * 1e-9
    s = straightWaveguide_S(
        wavelength=wavelength,
        width=width,
        thickness=thickness,
        sw_angle=sw_angle,
        length=length,
    )
    return model_from_sparameters(wavelength, s, pins=("E0", "W0"))


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    c = waveguide()
    print(c)
    # plot_model(c)
    # plt.show()
