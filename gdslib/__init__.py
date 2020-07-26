""" This package contains parameterized circuit models for https://github.com/gdsfactory/gdsfactory components
"""
from gdslib.add_gc import add_gc
from gdslib.coupler_ring import coupler_ring
from gdslib.load import load
from gdslib.mmi1x2 import mmi1x2
from gdslib.mmi2x2 import mmi2x2
from gdslib.mzi import mzi
from gdslib.ring_double import ring_double

from gdslib.plot_sparameters import plot_sparameters
from gdslib.sweep_simulation import get_transmission
from gdslib.sweep_simulation import sweep_simulation
from gdslib.sweep_simulation_montecarlo import sweep_simulation_montecarlo
from gdslib.autoname import autoname


component_type2factory = dict(
    coupler_ring=coupler_ring,
    mmi1x2=mmi1x2,
    mmi2x2=mmi2x2,
    mzi=mzi,
    ring_double=ring_double,
)


_elements = ["mmi1x2", "mmi2x2", "coupler_ring"]
_circuits = ["mzi"]
_functions = [
    "add_gc",
    "autoname",
    "load",
    "plot_sparameters",
    "get_transmission",
    "sweep_simulation",
    "sweep_simulation_montecarlo",
]
__all__ = _elements + _circuits + _functions
__version__ = "0.0.1"
