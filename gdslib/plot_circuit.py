import matplotlib.pyplot as plt
import numpy as np
import pp
from simphony.simulation import SweepSimulation
from simphony.tools import freq2wl


def get_transmission(
    circuit, iport="input", oport="output", start=1500e-9, stop=1600e-9, num=2000
):

    circuit = pp.call_if_func(circuit)

    simulation = SweepSimulation(circuit, start, stop, num)
    result = simulation.simulate()

    f, s = result.data(iport, oport)
    w = freq2wl(f) * 1e9
    return dict(wavelength_nm=w, s=s)


def plot_circuit(
    circuit,
    iport="input",
    oport="output",
    start=1500e-9,
    stop=1600e-9,
    num=2000,
    logscale=True,
    **kwargs
):
    """ Plot Sparameter circuit transmission over wavelength

    Args:
        num: number of sampled points
    """
    circuit = pp.call_if_func(circuit)

    simulation = SweepSimulation(circuit, start, stop, num)
    result = simulation.simulate()

    f, s = result.data(iport, oport)
    w = freq2wl(f) * 1e9

    if logscale:
        s = 20 * np.log10(abs(s))
        ylabel = "|S| (dB)"
    else:
        ylabel = "|S|"

    f, ax = plt.subplots()
    ax.plot(w, s)
    plt.xlabel("wavelength (nm)")
    plt.ylabel(ylabel)
    plt.title(circuit.name)
    return ax


if __name__ == "__main__":
    from mzi import mzi

    c = mzi()
    print(c.name)
    plot_circuit(mzi, logscale=False)
