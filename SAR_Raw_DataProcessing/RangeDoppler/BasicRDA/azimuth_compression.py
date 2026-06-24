import numpy as np
from parameters import *

def azimuth_compress(RD):

    RDc = np.zeros_like(RD)

    fd = np.fft.fftshift(
        np.fft.fftfreq(Naz, d=1/PRF)
    )

    for r in range(Nrg):

        R = 300 + r

        Ka = -(2 * V**2) / (lam * R)

        Haz = np.exp(
            1j * np.pi * (fd**2) / Ka
        )

        RDc[:, r] = RD[:, r] * Haz

    return RDc