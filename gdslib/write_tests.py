from gdslib import _circuits, _elements


def write_test_elements():
    """ writes a regression test for all the elements Sparameters dict"""
    with open("test_elements.py", "w") as f:
        f.write("# this code has been automatically generated from write_tests.py\n")
        f.write("import numpy as np\n\n")
        f.write("import gdslib as gl\n\n")

        for c in _elements:
            f.write(
                f"""
def test_{c}(data_regression):
    c = gl.{c}()
"""
                + """
    wav = np.linspace(1520, 1570, 3) * 1e-9
    f = 3e8 / wav
    s = c.s_parameters(freq=f)
    _, rows, cols = np.shape(s)
    sdict = {f'S{i+1}{j+1}': np.abs(s[:, i, j]).tolist() for i in range(rows) for j in range(cols)}
    data_regression.check(sdict)

"""
            )


def write_test_circuits():
    with open("test_circuits.py", "w") as f:
        f.write("# this code has been automatically generated from write_tests.py\n")
        f.write("import numpy as np\n\n")
        f.write("import gdslib as gl\n\n")

        for c in _circuits:
            f.write(
                f"""
def test_{c}(data_regression):
    c = gl.{c}()
    r = gl.get_transmission(c, num=3)
    data_regression.check(dict(w=r['wavelength_nm'].tolist(), s=r['s'].tolist()))

"""
            )


if __name__ == "__main__":
    write_test_elements()
    write_test_circuits()
