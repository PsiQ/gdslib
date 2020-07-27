import numpy as np
import pytest

from gdslib.components import _circuits
from gdslib.components import _elements
from gdslib.components import component_type2factory


@pytest.mark.parametrize("component_type", _elements)
def test_elements(component_type, data_regression):
    c = component_type2factory[component_type]()
    wav = np.linspace(1520, 1570, 3) * 1e-9
    f = 3e8 / wav
    s = c.s_parameters(freq=f)
    _, rows, cols = np.shape(s)
    sdict = {
        f"S{i+1}{j+1}": np.abs(s[:, i, j]).tolist()
        for i in range(rows)
        for j in range(cols)
    }
    data_regression.check(sdict)


# @pytest.mark.parametrize("component_type", _circuits)
# def test_circuits(component_type, data_regression):
#     c = component_type2factory[component_type]()
#     r = get_transmission(c, num=3)
#     data_regression.check(dict(w=r["wavelength_nm"].tolist(), s=r["s"].tolist()))
