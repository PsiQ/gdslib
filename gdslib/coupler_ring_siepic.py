"""
           n2            n4
           |             |
            \           /
             \         /
           ---=========---
        n1    length_x    n3

"""


from gdslib import plot_sparameters
from simphony.library import siepic

if __name__ == "__main__":
    c = siepic.ebeam_dc_halfring_straight(
        gap=200e-9, radius=10e-6, width=500e-9, thickness=220e-9, couple_length=0.0
    )
    c = plot_sparameters(c)
