import pp
from simphony.library import siepic
from simphony.netlist import Subcircuit

from gdslib.components.gc import gc1550te


def add_gc(circuit, gc=gc1550te, cpi="input", cpo="output", gpi="port 1", gpo="port 2"):
    """ add input and output gratings

    Args:
        circuit: needs to have `input` and `output` pins
        gc: grating coupler
        cpi: circuit pin input name
        cpo: circuit pin output name
        gpi: grating pin input name
        gpo: grating pin output name

    .. code::
                    _______
                   |       |
        gpi-> gpo--|cpi cpo|--gpo <-gpi
                   |_______|
    """
    gc = pp.call_if_func(gc)
    c = Subcircuit(f"{circuit.name}_{gc.name}")
    c.add([(gc, "gci"), (gc, "gco"), (circuit, "circuit")])
    c.connect_many([("gci", gpo, "circuit", cpi), ("gco", gpo, "circuit", cpo)])

    c.elements["gci"].pins[gpi] = "input"
    c.elements["gco"].pins[gpi] = "output"

    return c


def add_gc_siepic(circuit, gc=siepic.ebeam_gc_te1550):
    """ add input and output gratings

    Args:
        circuit: needs to have `input` and `output` pins
        gc: grating coupler
    """
    c = Subcircuit(f"{circuit}_gc")
    gc = pp.call_if_func(gc)
    c.add([(gc, "gci"), (gc, "gco"), (circuit, "circuit")])
    c.connect_many(
        [("gci", "n1", "circuit", "input"), ("gco", "n1", "circuit", "output")]
    )

    # c.elements["circuit"].pins["input"] = "input_circuit"
    # c.elements["circuit"].pins["output"] = "output_circuit"
    c.elements["gci"].pins["n2"] = "input"
    c.elements["gco"].pins["n2"] = "output"

    return c


if __name__ == "__main__":
    from gdslib import plot_circuit
    from gdslib.components import mzi

    c1 = mzi()
    c2 = add_gc(c1)
    print(c2.name)
    plot_circuit(c2)
