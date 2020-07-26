import pp
from simphony.library import siepic
from simphony.netlist import Subcircuit

from gdslib.load import load


def load_netlist(component):
    """load netlist for a gdsfactory component and returns a circuit model

    Args:
        component: component factory or instance
    """
    n = component.get_netlist()

    circuit = Subcircuit(component.name)

    model_name_tuple = []

    for i in n.instances.keys():
        component_type = n.instances[i]["component"]
        c = pp.c.component_type2factory[component_type]()
        model = load(c)
        model_name_tuple.append((model, i))

    e = circuit.add(model_name_tuple)

    for k, v in n.connections.items():
        c1, p1 = k.split(",")
        c2, p2 = v.split(",")
        circuit.connect(c1, p1, c2, p2)

    return circuit


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from gdslib import sweep_simulation

    c = pp.c.mzi()
    cm = load_netlist(c)
    cm.elements["mmi1x2_12_0"].pins["W0"] = "input"
    cm.elements["mmi1x2_88_0"].pins["W0"] = "output"

    sweep_simulation(cm)
    plt.show()
