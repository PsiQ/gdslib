from simphony.library import siepic
from simphony.netlist import Subcircuit

from gdslib.components import component_type2factory


def circuit_from_gdsfactory(component):
    """imports netlist from gdsfactory component and returns a Simphony circuit

    Args:
        component: component factory or instance
    """
    n = component.get_netlist()

    circuit = Subcircuit(component.name)

    model_name_tuple = []

    for i in n.instances.keys():
        component_type = n.instances[i]["component"]
        component_settings = n.instances[i]["settings"]
        model = component_type2factory[component_type](**component_settings)
        model_name_tuple.append((model, i))

    circuit.add(model_name_tuple)

    for k, v in n.connections.items():
        c1, p1 = k.split(",")
        c2, p2 = v.split(",")
        circuit.connect(c1, p1, c2, p2)

    return circuit


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from gdslib import plot_circuit
    import pp

    c = pp.c.mzi(DL=50)
    cm = circuit_from_gdsfactory(c)
    cm.elements["mmi1x2_12_0"].pins["W0"] = "input"
    cm.elements["mmi1x2_88_0"].pins["W0"] = "output"

    plot_circuit(cm)
    plt.show()
