from simphony.library import siepic
from simphony.netlist import Subcircuit

from gdslib import plot_circuit
from gdslib.autoname import autoname
from gdslib.components.mmi1x2 import mmi1x2


@autoname
def mzi(L0=1, DL=100, L2=10, y_model_factory=mmi1x2, wg=siepic.ebeam_wg_integral_1550):
    """ Mzi circuit model

    Args:
        L0 (um): vertical length for both and top arms
        DL (um): bottom arm extra length, delta_length = 2*DL
        L2 (um): L_top horizontal length

    Returns: mzi circuit model

    .. code::

               __L2__
               |      |
               L0     L0r
               |      |
     splitter==|      |==recombiner
               |      |
               L0     L0r
               |      |
               DL     DL
               |      |
               |__L2__|


    .. plot::
      :include-source:

      import pp

      c = pp.c.mzi(L0=0.1, DL=0, L2=10)
      pp.plotgds(c)


    .. plot::
        :include-source:

        import gdslib as gl

        c = gl.mzi()
        gl.plot_circuit(c)


    """
    y = y_model_factory() if callable(y_model_factory) else y_model_factory
    wg_long = wg(length=(2 * L0 + 2 * DL + L2) * 1e-6)
    wg_short = wg(length=(2 * L0 + L2) * 1e-6)

    # Create the circuit, add all individual instances
    circuit = Subcircuit("mzi")
    circuit.add(
        [
            (y, "splitter"),
            (y, "recombiner"),
            (wg_long, "wg_long"),
            (wg_short, "wg_short"),
        ]
    )

    # Circuits can be connected using the elements' string names:
    circuit.connect_many(
        [
            ("splitter", "E0", "wg_long", "n1"),
            ("splitter", "E1", "wg_short", "n1"),
            ("recombiner", "E0", "wg_long", "n2"),
            ("recombiner", "E1", "wg_short", "n2"),
        ]
    )
    circuit.elements["splitter"].pins["W0"] = "input"
    circuit.elements["recombiner"].pins["W0"] = "output"
    return circuit


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    c = mzi()
    plot_circuit(c)
    plt.show()
