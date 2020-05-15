# this code has been automatically generated from write_tests.py
import gdslib as gl
import numpy as np


def test_mzi(data_regression):
    c = gl.mzi()
    r = gl.get_transmission(c, num=3)
    data_regression.check(dict(w=r["wavelength_nm"].tolist(), s=r["s"].tolist()))
