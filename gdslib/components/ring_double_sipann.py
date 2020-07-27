import numpy as np
import pp
from simphony.library import ebeam
from simphony.library import siepic
from simphony.netlist import Subcircuit

from gdslib import plot_circuit
from gdslib.autoname import autoname


@autoname
def ring_double_sipann(
    wg_width=0.5,
    gap=0.2,
    length_x=4,
    bend_radius=5,
    length_y=2,
    coupler=siepic.ebeam_dc_halfring_straight,
    waveguide=siepic.ebeam_wg_integral_1550,
    terminator=ebeam.ebeam_terminator_te1550,
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

    .. plot::
      :include-source:

      import pp

      c = pp.c.ring(wg_width=0.5, gap=0.2, length_x=4, bend_radius=5, length_y=2)
      pp.plotgds(c)


    .. plot::
        :include-source:

        import simphony.library.gdsfactory as cl
        c = cl.ring()
        cl.plot_circuit(c)
    """
    waveguide = waveguide() if callable(waveguide) else waveguide
    half_ring = coupler() if callable(coupler) else coupler
    term = coupler() if callable(coupler) else coupler

    circuit = Subcircuit()
    circuit.add([(half_ring, "input"), (half_ring, "output"), (term, "terminator")])

    circuit.elements["input"].pins = ("pass", "midb", "in", "midt")
    circuit.elements["output"].pins = ("out", "midt", "term", "midb")

    circuit.connect_many(
        [
            ("input", "midb", "output", "midb"),
            ("input", "midt", "output", "midt"),
            ("terminator", "n1", "output", "term"),
        ]
    )
    return circuit


if __name__ == "__main__":
    from SiPANN import scee
    from SiPANN.scee_int import SimphonyWrapper

    r = 10e3
    w = 500
    t = 220
    wavelength = np.linspace(1500, 1600)
    gap = 100
    hr = scee.HalfRing(w, t, r, gap)
    s_hr = SimphonyWrapper(hr)
    c = ring_double_sipann(coupler=s_hr)
    plot_circuit(c)
