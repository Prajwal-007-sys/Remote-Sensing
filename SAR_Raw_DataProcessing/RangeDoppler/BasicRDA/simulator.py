import numpy as np
from parameters import *

def generate_raw_data():

    eta = np.arange(Naz) / PRF
    tau = np.arange(Nrg) / Fs

    raw = np.zeros(
        (Naz, Nrg),
        dtype=complex
    )

    eta0 = Naz / (2 * PRF)

    # (azimuth_position, slant_range)
    targets = [
        (0,    1000),
        (100,  1500),
        (-150, 2200)
    ]

    beam_width = 0.2

    for i in range(Naz):

        for x, y in targets:

            # Physical SAR geometry
            R = np.sqrt(
                y**2 +
                (x - V * (eta[i] - eta0))**2
            )

            tau_d = 2 * R / c

            carrier_phase = np.exp(
                -1j * 4 * np.pi * R / lam
            )

            beam = np.exp(
                -((eta[i] - eta0)**2) /
                (2 * beam_width**2)
            )

            mask = np.abs(
                tau - tau_d
            ) <= Tp/2

            chirp = mask * np.exp(
                1j * np.pi * Kr *
                (tau - tau_d)**2
            )

            raw[i, :] += (
                beam *
                carrier_phase *
                chirp
            )

    return raw