import pp

from gdslib.autoname import autoname
from gdslib.model_from_gdsfactory import model_from_gdsfactory


@autoname
def mmi1x2(c=pp.c.mmi1x2, height_nm=220):
    """ mmi1x2 Sparameter model

    .. code::
            ____
           |   |_ E1
       W0 -|   |_ E0
           |___|

    .. plot::
        :include-source:

        import gdslib as gl

        c = gl.mmi1x2()
        gl.plot_model(c)
    """
    m = model_from_gdsfactory(c, height_nm=height_nm)
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    wav = np.linspace(1520, 1570, 1024) * 1e-9
    f = 3e8 / wav
    c = mmi1x2()
    s = c.s_parameters(freq=f)

    plt.plot(wav, np.abs(s[:, 1] ** 2))
    print(c.pins)
    print(c.settings)
    # plt.show()
