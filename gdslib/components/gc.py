from gdslib.autoname import autoname
from gdslib.config import CONFIG
from gdslib.model_from_gdsfactory import model_from_gdsfactory


@autoname
def gc1550te(filepath=CONFIG.sp / "gc2dte" / "gc1550.dat", numports=2):
    m = model_from_gdsfactory(filepath=filepath, numports=numports)
    return m


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    wav = np.linspace(1520, 1570, 1024) * 1e-9
    f = 3e8 / wav
    c = gc1550te()
    s = c.s_parameters(freq=f)

    plt.plot(wav, np.abs(s[:, 1] ** 2))
    print(c.pins)
    plt.show()
