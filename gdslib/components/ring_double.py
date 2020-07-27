import pp
from simphony.library import siepic
from simphony.netlist import Subcircuit

from gdslib import plot_circuit
from gdslib.autoname import autoname
from gdslib.components.coupler_ring import coupler_ring


@autoname
def ring_double(
    wg_width=0.5,
    gap=0.2,
    length_x=4,
    bend_radius=5,
    length_y=2,
    coupler=coupler_ring,
    waveguide=siepic.ebeam_wg_integral_1550,
):
    """ double bus ring made of two couplers (ct: top, cb: bottom)
    connected with two vertical waveguides (wyl: left, wyr: right)

    .. code::

         --==ct==--
          |      |
          wl     wr length_y
          |      |
         --==cb==-- gap

          length_x


           ---=========---
        E0    length_x    W0
             /         \
            /           \
           |             |
           N1           N0

           N0            N1
           |             |
            \           /
             \         /
           ---=========---
        W0    length_x    E0



    .. plot::
      :include-source:

      import pp

      c = pp.c.ring_double(wg_width=0.5, gap=0.2, length_x=4, bend_radius=5, length_y=2)
      pp.plotgds(c)


    .. plot::
        :include-source:

        import gdslib as gl

        c = gl.ring_double()
        gl.plot_circuit(c)
    """

    waveguide = waveguide() if callable(waveguide) else waveguide
    coupler = (
        coupler(length_x=length_x, bend_radius=bend_radius, gap=gap, wg_width=wg_width)
        if callable(coupler)
        else coupler
    )

    # Create the circuit, add all individual instances
    circuit = Subcircuit("ring_double")
    circuit.add(
        [(coupler, "ct"), (coupler, "cb"), (waveguide, "wl"), (waveguide, "wr")]
    )

    # Circuits can be connected using the elements' string names:
    circuit.connect_many(
        [
            ("cb", "N0", "wl", "n1"),
            ("wl", "n2", "ct", "N1"),
            ("ct", "N0", "wr", "n1"),
            ("wr", "n2", "cb", "N1"),
        ]
    )
    circuit.elements["cb"].pins["W0"] = "input"
    circuit.elements["cb"].pins["E0"] = "output"
    circuit.elements["ct"].pins["E0"] = "drop"
    circuit.elements["ct"].pins["W0"] = "cdrop"
    return circuit


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    c = ring_double()
    plot_circuit(c)
    plt.show()
